import requests
from bs4 import BeautifulSoup
import json
import time
import csv
import sys
import re
import logging
from typing import List, Dict, Optional, Any
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

BASE_URL = "https://marketing1usa.wordpress.com/"

def is_url(text: str) -> bool:
    """Simple regex to check if text looks like a URL."""
    return re.match(r'^https?://', text.strip()) is not None

def get_session() -> requests.Session:
    """Create a requests Session with retry logic."""
    session = requests.Session()
    retry = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[500, 502, 503, 504],
        allowed_methods=frozenset(['GET', 'POST'])
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    })
    return session

def scrape_site() -> List[Dict[str, Optional[str]]]:
    page_num = 1
    all_posts = []
    session = get_session()

    while True:
        url = f"{BASE_URL}page/{page_num}/" if page_num > 1 else BASE_URL
        logger.info(f"Scraping {url}...")

        try:
            response = session.get(url)
            if response.status_code == 404:
                logger.info("Reached end of pages (404).")
                break
            response.raise_for_status()
        except requests.RequestException as e:
            logger.error(f"Error fetching {url}: {e}")
            break

        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('article', class_='post')

        if not articles:
            logger.info("No articles found on this page. Stopping.")
            break

        for article in articles:
            post_data: Dict[str, Optional[str]] = {}

            # Title
            title_text = ""
            title_tag = article.select_one('h1.entry-title a')
            if title_tag:
                title_text = title_tag.get_text(strip=True)
                post_data['title'] = title_text

            # Date
            date_tag = article.select_one('time.entry-date')
            if date_tag:
                post_data['date'] = date_tag.get_text(strip=True)
                post_data['datetime'] = date_tag.get('datetime')

            # External Link Extraction Strategy
            external_link = None
            content_div = article.select_one('.entry-content')

            if content_div:
                # 1. Try to find the first <a> link in content
                link_tag = content_div.select_one('a')
                if link_tag:
                    external_link = link_tag.get('href')

                # 2. If no link, check for iframes (e.g. YouTube embeds)
                if not external_link:
                    iframe_tag = content_div.select_one('iframe')
                    if iframe_tag:
                        external_link = iframe_tag.get('src')

            # 3. If still no link, check if the title itself is a URL
            if not external_link and title_text and is_url(title_text):
                external_link = title_text

            post_data['external_link'] = external_link

            # Post URL (the blog post itself)
            if title_tag:
                post_data['post_url'] = title_tag.get('href')

            all_posts.append(post_data)

        # Pagination check
        nav_links = soup.select_one('.nav-links, .navigation')
        has_next = False
        if nav_links:
            if 'Older posts' in nav_links.get_text() or 'Next' in nav_links.get_text():
                has_next = True
            next_page_link = soup.find('a', href=lambda href: href and f"page/{page_num + 1}/" in href)
            if next_page_link:
                has_next = True

        older_posts = soup.find('a', string=lambda text: text and "Older Posts" in text)
        if not older_posts and not has_next:
             if not soup.select_one('.next.page-numbers') and not soup.select_one('.nav-previous a'):
                 logger.info("No next page link found.")

        page_num += 1
        time.sleep(1) # Be polite

    return all_posts

def save_data(posts: List[Dict[str, Optional[str]]]) -> None:
    # JSON
    with open('links.json', 'w', encoding='utf-8') as f:
        json.dump(posts, f, indent=4, ensure_ascii=False)
    logger.info(f"Saved {len(posts)} posts to links.json")

    # CSV
    with open('links.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Title', 'Date', 'External Link', 'Post URL'])
        for post in posts:
            writer.writerow([
                post.get('title', ''),
                post.get('date', ''),
                post.get('external_link', ''),
                post.get('post_url', '')
            ])
    logger.info(f"Saved {len(posts)} posts to links.csv")

    # Unique Links TXT
    unique_links = set()
    for post in posts:
        link = post.get('external_link')
        if link:
            unique_links.add(link)

    sorted_links = sorted(list(unique_links))
    with open('unique_links.txt', 'w', encoding='utf-8') as f:
        for link in sorted_links:
            f.write(link + '\n')
    logger.info(f"Saved {len(sorted_links)} unique links to unique_links.txt")

if __name__ == "__main__":
    logger.info("Starting scraper...")
    posts = scrape_site()
    save_data(posts)
    logger.info("Done.")
