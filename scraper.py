import aiohttp
import asyncio
from bs4 import BeautifulSoup
import json
import csv
import re
import argparse
import logging
import time
from typing import List, Dict, Optional, Set
from urllib.parse import urlparse

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

BASE_URL = "https://markposition.wordpress.com/"

class MarkPositionScraperAsync:
    def __init__(self, output_json: str, output_csv: str, output_txt: str, max_pages: Optional[int] = None, concurrency: int = 5):
        self.output_json = output_json
        self.output_csv = output_csv
        self.output_txt = output_txt
        self.max_pages = max_pages
        self.concurrency = concurrency
        self.session = None

    def clean_text(self, text: str) -> str:
        """Normalize whitespace and remove non-breaking spaces."""
        if not text:
            return ""
        text = text.replace('\xa0', ' ')
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

    def extract_domain(self, url: str) -> Optional[str]:
        """Extract domain from URL."""
        if not url:
            return None
        try:
            return urlparse(url).netloc.replace('www.', '')
        except:
            return None

    def sanitize_for_csv(self, value: str) -> str:
        """Sanitize a value for CSV to prevent formula injection."""
        if not value:
            return ""
        # If the value starts with any of the dangerous characters, prepend a single quote
        if value.startswith(('=', '+', '-', '@')):
            return "'" + value
        return value

    async def fetch_page(self, session: aiohttp.ClientSession, page_num: int) -> Optional[str]:
        url = f"{BASE_URL}page/{page_num}/" if page_num > 1 else BASE_URL
        try:
            async with session.get(url) as response:
                if response.status == 404:
                    return None
                response.raise_for_status()
                return await response.text()
        except aiohttp.ClientError as e:
            logger.error(f"Error fetching page {page_num}: {e}")
            return None

    async def parse_page(self, html: str) -> List[Dict]:
        soup = BeautifulSoup(html, 'html.parser')
        articles = soup.find_all('article', class_='post')
        page_posts = []

        if not articles:
            return []

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

            # External Link
            external_link = None
            content_div = article.select_one('.entry-content')

            if content_div:
                link_tag = content_div.select_one('a')
                if link_tag:
                    external_link = link_tag.get('href')

                if not external_link:
                    iframe_tag = content_div.select_one('iframe')
                    if iframe_tag:
                        external_link = iframe_tag.get('src')

            if not external_link and title_text and self.is_url(title_text):
                external_link = title_text

            post_data['external_link'] = external_link
            post_data['domain'] = self.extract_domain(external_link)

            # Post URL
            if title_tag:
                post_data['post_url'] = title_tag.get('href')

            page_posts.append(post_data)

        return page_posts

    async def scrape(self):
        all_posts = []
        page_num = 1
        sem = asyncio.Semaphore(self.concurrency)

        # Headers
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        async with aiohttp.ClientSession(headers=headers) as session:
            # We don't know the total pages, so we have to fetch sequentially or in chunks until we hit 404/empty.
            # Pure concurrent fetching of all pages requires knowing the max page.
            # Heuristic: fetch in batches of `concurrency`. If any page in batch returns 404 or empty, stop.

            # Actually, WordPress pages are sequential. If page N is 404, N+1 is likely 404 too.
            # But fetching 100 pages 1-by-1 is slow.
            # Let's try fetching chunks.

            active = True
            while active:
                tasks = []
                # Prepare a batch of pages
                batch_start = page_num
                # If max_pages is set, clamp the batch size
                current_concurrency = self.concurrency

                for i in range(current_concurrency):
                    current_page = batch_start + i
                    if self.max_pages and current_page > self.max_pages:
                        active = False
                        break

                    # We create a task that acquires semaphore (though sem is less useful if we just create batch size = concurrency)
                    tasks.append(self.fetch_and_parse(session, current_page, sem))

                if not tasks:
                    break

                logger.info(f"Fetching pages {batch_start} to {batch_start + len(tasks) - 1}...")
                results = await asyncio.gather(*tasks)

                # Check results
                batch_posts_count = 0
                stop_detected = False

                # Results are ordered by page number
                for idx, page_posts in enumerate(results):
                    page_idx = batch_start + idx
                    if page_posts is None:
                        # 404 or Error
                        logger.info(f"Page {page_idx} returned 404 or empty. Stopping.")
                        stop_detected = True
                        break # Don't process further pages in this batch effectively (though they were fetched)
                    elif len(page_posts) == 0:
                        logger.info(f"Page {page_idx} has no articles. Stopping.")
                        stop_detected = True
                        break
                    else:
                        all_posts.extend(page_posts)
                        batch_posts_count += len(page_posts)

                if stop_detected:
                    break

                if self.max_pages and (batch_start + len(tasks) - 1) >= self.max_pages:
                    logger.info("Reached max pages limit.")
                    break

                page_num += len(tasks)
                # Small delay between batches
                await asyncio.sleep(0.5)

        self.save_data(all_posts)

    async def fetch_and_parse(self, session, page_num, sem):
        async with sem:
            html = await self.fetch_page(session, page_num)
            if html:
                return await self.parse_page(html)
            return None

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
                writer.writerow(['Title', 'Date', 'Author', 'Categories', 'External Link', 'Domain', 'Post URL'])
                for post in posts:
                    writer.writerow([
                        self.sanitize_for_csv(post.get('title', '')),
                        self.sanitize_for_csv(post.get('date', '')),
                        self.sanitize_for_csv(post.get('author', '')),
                        self.sanitize_for_csv(", ".join(post.get('categories', []))),
                        self.sanitize_for_csv(post.get('external_link', '')),
                        self.sanitize_for_csv(post.get('domain', '')),
                        self.sanitize_for_csv(post.get('post_url', ''))
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
    parser = argparse.ArgumentParser(description="Async Scraper for markposition.wordpress.com")
    parser.add_argument("--json", default="links.json", help="Output JSON filename")
    parser.add_argument("--csv", default="links.csv", help="Output CSV filename")
    parser.add_argument("--txt", default="unique_links.txt", help="Output TXT filename for unique links")
    parser.add_argument("--limit", type=int, help="Limit number of pages to scrape")
    parser.add_argument("--concurrency", type=int, default=5, help="Number of concurrent requests")

    args = parser.parse_args()

    scraper = MarkPositionScraperAsync(
        output_json=args.json,
        output_csv=args.csv,
        output_txt=args.txt,
        max_pages=args.limit,
        concurrency=args.concurrency
    )

    asyncio.run(scraper.scrape())

if __name__ == "__main__":
    main()
