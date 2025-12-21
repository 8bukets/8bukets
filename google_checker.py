import requests
from bs4 import BeautifulSoup
import argparse
import logging
import sys
import random
import time
import sqlite3
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# A simplified user-agent that sometimes bypasses strict checks or prompts slightly simpler HTML
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
]

DB_NAME = "wishlist_data.db"

def init_rankings_db():
    """Initialize the rankings table in the database."""
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS rankings (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    query TEXT,
                    rank INTEGER,
                    title TEXT,
                    url TEXT,
                    checked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()
    except sqlite3.Error as e:
        logger.error(f"Database initialization error: {e}")

def save_rankings_to_db(results, query):
    """Save ranking results to the database."""
    if not results:
        return

    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            for res in results:
                cursor.execute('''
                    INSERT INTO rankings (query, rank, title, url)
                    VALUES (?, ?, ?, ?)
                ''', (query, res['rank'], res['title'], res['url']))
            conn.commit()
            logger.info(f"Saved {len(results)} rankings to database.")
    except sqlite3.Error as e:
        logger.error(f"Database insertion error: {e}")

def check_google_listings(query, num_results=10):
    """
    Perform a Google search using requests and BeautifulSoup.
    Note: This is fragile as Google actively blocks scrapers.
    """
    logger.info(f"Searching Google for: '{query}' (Limit: {num_results})")

    encoded_query = requests.utils.quote(query)
    url = f"https://www.google.com/search?q={encoded_query}&num={num_results}"

    headers = {
        'User-Agent': random.choice(USER_AGENTS),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
    }

    results = []

    try:
        # Create a session to handle cookies potentially
        session = requests.Session()
        response = session.get(url, headers=headers, timeout=15)

        if response.status_code == 429:
            logger.error("429 Too Many Requests. Google has blocked this IP temporarily.")
            return []

        if response.status_code != 200:
            logger.error(f"Status code: {response.status_code}")
            return []

        soup = BeautifulSoup(response.text, "html.parser")

        # Debug: Check for consent page or captcha
        if "Consent" in soup.get_text() or "CAPTCHA" in soup.get_text():
            logger.warning("Google returned a Consent or CAPTCHA page. Automation detected.")
            # We can't solve captcha here.

        # Try finding results with common selectors
        # 'g' class is standard for result container
        search_results_divs = soup.find_all("div", class_="g")

        if not search_results_divs:
            # Fallback for mobile/simplified view
            # Sometimes results are in different divs
            search_results_divs = soup.select("div.kCrYT") # Older mobile class

        rank = 1
        for div in search_results_divs:
            if rank > num_results:
                break

            title_tag = div.find("h3")
            link_tag = div.find("a")

            if title_tag and link_tag:
                title = title_tag.get_text()
                link = link_tag.get("href")

                # Clean google links if necessary (sometimes /url?q=...)
                if link.startswith("/url?q="):
                    link = link.split("/url?q=")[1].split("&")[0]

                if link.startswith("/") and "google" in link:
                    continue

                results.append({
                    "rank": rank,
                    "title": title,
                    "url": link
                })
                rank += 1

        # One last fallback generic search if structure is totally different
        if not results:
             logger.info("Attempting generic fallback parsing...")
             anchors = soup.find_all("a")
             for a in anchors:
                 if rank > num_results: break
                 h3 = a.find("h3")
                 if h3:
                     link = a.get("href")
                     if link and link.startswith("http") and "google" not in link:
                         results.append({
                             "rank": rank,
                             "title": h3.get_text(),
                             "url": link
                         })
                         rank += 1

    except Exception as e:
        logger.error(f"Error during search: {e}")

    return results

def main():
    parser = argparse.ArgumentParser(description="Check Google Listings")
    parser.add_argument("--query", default="site:wishlist.design.blog", help="Search query")
    parser.add_argument("--limit", type=int, default=10, help="Number of results")

    args = parser.parse_args()

    init_rankings_db()
    results = check_google_listings(args.query, args.limit)
    save_rankings_to_db(results, args.query)

    if not results:
        logger.warning("No results found. The IP might be blocked or HTML structure changed.")
    else:
        print("\n--- Google Search Results ---")
        for res in results:
            print(f"{res['rank']}. {res['title']}")
            print(f"   {res['url']}")
            print("-" * 20)

if __name__ == "__main__":
    main()
