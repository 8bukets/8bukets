import requests
from bs4 import BeautifulSoup
import json
import time
import csv
import sys
import re
import logging
import argparse
from typing import List, Dict, Optional, Any, Set
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from dataclasses import dataclass, asdict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

@dataclass
class Post:
    title: str
    date: str
    external_link: Optional[str]
    post_url: Optional[str]

class WordPressScraper:
    def __init__(self, base_url: str, delay: int = 1):
        self.base_url = base_url
        self.delay = delay
        self.session = self._get_session()

    def _get_session(self) -> requests.Session:
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

    def is_url(self, text: str) -> bool:
        """Simple regex to check if text looks like a URL."""
        return re.match(r'^https?://', text.strip()) is not None

    def scrape(self) -> List[Post]:
        page_num = 1
        all_posts: List[Post] = []

        while True:
            url = f"{self.base_url}page/{page_num}/" if page_num > 1 else self.base_url
            logger.info(f"Scraping {url}...")

            try:
                response = self.session.get(url)
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
                post = self._parse_article(article)
                all_posts.append(post)

            # Pagination check
            if not self._has_next_page(soup, page_num):
                 logger.info("No next page link found.")
                 break

            page_num += 1
            time.sleep(self.delay)

        return all_posts

    def _parse_article(self, article: Any) -> Post:
        # Title
        title_text = ""
        title_tag = article.select_one('h1.entry-title a')
        if title_tag:
            title_text = title_tag.get_text(strip=True)

        # Date
        date_text = ""
        date_tag = article.select_one('time.entry-date')
        if date_tag:
            date_text = date_tag.get_text(strip=True)

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
        if not external_link and title_text and self.is_url(title_text):
            external_link = title_text

        # Post URL
        post_url = title_tag.get('href') if title_tag else None

        return Post(
            title=title_text,
            date=date_text,
            external_link=external_link,
            post_url=post_url
        )

    def _has_next_page(self, soup: BeautifulSoup, current_page: int) -> bool:
        nav_links = soup.select_one('.nav-links, .navigation')
        if nav_links:
            if 'Older posts' in nav_links.get_text() or 'Next' in nav_links.get_text():
                return True
            next_page_link = soup.find('a', href=lambda href: href and f"page/{current_page + 1}/" in href)
            if next_page_link:
                return True

        older_posts = soup.find('a', string=lambda text: text and "Older Posts" in text)
        if older_posts:
            return True

        if soup.select_one('.next.page-numbers') or soup.select_one('.nav-previous a'):
            return True

        return False

def save_data(posts: List[Post], output_prefix: str = 'links') -> None:
    # JSON
    json_path = f"{output_prefix}.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump([asdict(p) for p in posts], f, indent=4, ensure_ascii=False)
    logger.info(f"Saved {len(posts)} posts to {json_path}")

    # CSV
    csv_path = f"{output_prefix}.csv"
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Title', 'Date', 'External Link', 'Post URL'])
        for post in posts:
            writer.writerow([
                post.title,
                post.date,
                post.external_link or '',
                post.post_url or ''
            ])
    logger.info(f"Saved {len(posts)} posts to {csv_path}")

    # Unique Links TXT
    unique_links: Set[str] = set()
    for post in posts:
        if post.external_link:
            unique_links.add(post.external_link)

    sorted_links = sorted(list(unique_links))
    txt_path = f"unique_links.txt" # Keeping original name for compatibility or could change to {output_prefix}_unique.txt
    with open(txt_path, 'w', encoding='utf-8') as f:
        for link in sorted_links:
            f.write(link + '\n')
    logger.info(f"Saved {len(sorted_links)} unique links to {txt_path}")

def main():
    parser = argparse.ArgumentParser(description="Scrape a WordPress site for links.")
    parser.add_argument("--url", default="https://marketing1usa.wordpress.com/", help="Base URL of the WordPress site")
    parser.add_argument("--output", default="links", help="Prefix for output files (default: links)")
    parser.add_argument("--delay", type=int, default=1, help="Delay between requests in seconds")

    args = parser.parse_args()

    # Ensure URL ends with slash
    base_url = args.url if args.url.endswith('/') else f"{args.url}/"

    scraper = WordPressScraper(base_url, args.delay)
    logger.info(f"Starting scraper for {base_url}...")
    posts = scraper.scrape()
    save_data(posts, args.output)
    logger.info("Done.")

if __name__ == "__main__":
    main()
