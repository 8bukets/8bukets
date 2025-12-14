import json
import logging
import sys
import time
import random
import requests
from bs4 import BeautifulSoup

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

SEARCH_QUERY = "site:infogadgettech.wordpress.com"
OUTPUT_FILE = "google_listings.json"

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
]

def scrape_google_page_one(query):
    logger.info(f"Searching Google for: {query}")

    # Try using requests directly as googlesearch-python seems to be failing (likely due to environment/bot detection)
    # Note: Scraping Google directly is fragile and often blocked.

    url = "https://www.google.com/search"
    headers = {
        'User-Agent': random.choice(USER_AGENTS),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://www.google.com/'
    }
    params = {'q': query, 'num': 10}

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()

        if "sorry/index" in response.url:
            logger.warning("Google CAPTCHA encountered.")
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        results = []

        # Try to find results in standard containers
        # Class names change, but often 'div.g' is used.
        # Sometimes results are in 'div.tF2Cxc'

        search_results = soup.select('div.g')
        if not search_results:
             # Fallback for older/mobile structure
             search_results = soup.select('div.kCrYT')

        for result in search_results:
            try:
                link_tag = result.find('a')
                if not link_tag:
                    continue

                link = link_tag['href']

                # Filter out Google redirect links if present (rare in modern desktop view but possible)
                if link.startswith('/url?q='):
                    link = link.split('/url?q=')[1].split('&')[0]

                if not link.startswith('http'):
                    continue

                title_tag = result.find('h3')
                if not title_tag:
                    # Try finding h3 inside the anchor
                    title_tag = link_tag.find('h3')

                title = title_tag.get_text() if title_tag else "No Title"

                # Snippet
                snippet_tag = result.select_one('div.VwiC3b, div.BNeawe.s3v9rd.AP7Wnd')
                snippet = snippet_tag.get_text() if snippet_tag else "No Snippet"

                results.append({
                    "title": title,
                    "link": link,
                    "snippet": snippet
                })
            except Exception as e:
                continue

        if not results:
            logger.warning("No results parsed. Structure might have changed or page is empty.")
            # Log a snippet of the HTML for debugging (truncated)
            logger.debug(soup.prettify()[:500])

        return results

    except Exception as e:
        logger.error(f"Error scraping Google: {e}")
        return []

def main():
    results = scrape_google_page_one(SEARCH_QUERY)

    if results:
        logger.info(f"Found {len(results)} results.")
        with open(OUTPUT_FILE, 'w') as f:
            json.dump(results, f, indent=4)
        logger.info(f"Saved results to {OUTPUT_FILE}")
    else:
        logger.warning("No results found or scraping failed (likely blocked).")
        # Write an empty list or error object to indicate failure but valid JSON
        with open(OUTPUT_FILE, 'w') as f:
            json.dump([], f)

if __name__ == "__main__":
    main()
