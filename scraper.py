import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from bs4 import BeautifulSoup
import json
import time
import csv
import sys
import re
import argparse
import logging
from typing import List, Dict, Optional, Set

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

BASE_URL = "https://markposition.wordpress.com/"

class MarkPositionScraper:
    def __init__(self, output_json: str, output_csv: str, output_txt: str, max_pages: Optional[int] = None):
        self.output_json = output_json
        self.output_csv = output_csv
        self.output_txt = output_txt
        self.max_pages = max_pages
        self.session = self._create_session()

    def _create_session(self) -> requests.Session:
        """Create a requests session with retry logic."""
        session = requests.Session()
        retry = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET"]
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        return session

    def clean_text(self, text: str) -> str:
        """Normalize whitespace and remove non-breaking spaces."""
        if not text:
            return ""
        # Replace non-breaking spaces with normal spaces and strip
        text = text.replace('\xa0', ' ')
        # Collapse multiple spaces into one
        return re.sub(r'\s+', ' ', text).strip()

    def is_url(self, text: str) -> bool:
        """Check if text looks like a URL."""
        return re.match(r'^https?://', text.strip()) is not None

    def extract_categories(self, article: BeautifulSoup) -> List[str]:
        """Extract categories from article class names."""
        categories = []
        if article.get('class'):
            for cls in article['class']:
                if cls.startswith('category-'):
                    cat_name = cls.replace('category-', '').replace('-', ' ').title()
                    categories.append(cat_name)
        return categories

    def scrape(self):
        page_num = 1
        all_posts = []

        while True:
            if self.max_pages and page_num > self.max_pages:
                logger.info(f"Reached max pages limit ({self.max_pages}). Stopping.")
                break

            url = f"{BASE_URL}page/{page_num}/" if page_num > 1 else BASE_URL
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
                post_data = {}

                # Title
                title_text = ""
                title_tag = article.select_one('h1.entry-title a')
                if title_tag:
                    title_text = self.clean_text(title_tag.get_text())
                    post_data['title'] = title_text

                # Date
                date_tag = article.select_one('time.entry-date')
                if date_tag:
                    post_data['date'] = self.clean_text(date_tag.get_text())
                    post_data['datetime'] = date_tag.get('datetime')

                # Author
                author_tag = article.select_one('.author.vcard .fn')
                if author_tag:
                    post_data['author'] = self.clean_text(author_tag.get_text())
                else:
                    post_data['author'] = None

                # Categories
                post_data['categories'] = self.extract_categories(article)

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
                     logger.info("No next page link found. Assuming end of content.")
                     # We break here to be safe, though 404 check is the ultimate backstop.
                     # But some WordPress configs redirect page/N to page/1 if N is too high, creating infinite loop.
                     # So explicit next link check is safer.
                     break

            page_num += 1
            time.sleep(1) # Be polite

        self.save_data(all_posts)

    def save_data(self, posts: List[Dict]):
        # JSON
        try:
            with open(self.output_json, 'w', encoding='utf-8') as f:
                json.dump(posts, f, indent=4, ensure_ascii=False)
            logger.info(f"Saved {len(posts)} posts to {self.output_json}")
        except IOError as e:
            logger.error(f"Failed to save JSON: {e}")

        # CSV
        try:
            with open(self.output_csv, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Title', 'Date', 'Author', 'Categories', 'External Link', 'Post URL'])
                for post in posts:
                    writer.writerow([
                        post.get('title', ''),
                        post.get('date', ''),
                        post.get('author', ''),
                        ", ".join(post.get('categories', [])),
                        post.get('external_link', ''),
                        post.get('post_url', '')
                    ])
            logger.info(f"Saved {len(posts)} posts to {self.output_csv}")
        except IOError as e:
            logger.error(f"Failed to save CSV: {e}")

        # Unique Links TXT
        unique_links = set()
        for post in posts:
            link = post.get('external_link')
            if link:
                unique_links.add(link)

        sorted_links = sorted(list(unique_links))
        try:
            with open(self.output_txt, 'w', encoding='utf-8') as f:
                for link in sorted_links:
                    f.write(link + '\n')
            logger.info(f"Saved {len(sorted_links)} unique links to {self.output_txt}")
        except IOError as e:
            logger.error(f"Failed to save TXT: {e}")

def main():
    parser = argparse.ArgumentParser(description="Scrape markposition.wordpress.com")
    parser.add_argument("--json", default="links.json", help="Output JSON filename")
    parser.add_argument("--csv", default="links.csv", help="Output CSV filename")
    parser.add_argument("--txt", default="unique_links.txt", help="Output TXT filename for unique links")
    parser.add_argument("--limit", type=int, help="Limit number of pages to scrape")

    args = parser.parse_args()

    scraper = MarkPositionScraper(
        output_json=args.json,
        output_csv=args.csv,
        output_txt=args.txt,
        max_pages=args.limit
    )
    scraper.scrape()

if __name__ == "__main__":
    main()
