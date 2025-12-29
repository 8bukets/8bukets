import aiohttp
import asyncio
from bs4 import BeautifulSoup, SoupStrainer
import json
import csv
import re
import argparse
import logging
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
        strainer = SoupStrainer('article', class_='post')
        soup = BeautifulSoup(html, 'html.parser', parse_only=strainer)
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
        page_num = 1
        sem = asyncio.Semaphore(self.concurrency)

        # Headers
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        # Open files for incremental writing
        with open(self.output_json, 'w', encoding='utf-8') as json_f, \
             open(self.output_csv, 'w', newline='', encoding='utf-8') as csv_f, \
             open(self.output_txt, 'w', encoding='utf-8') as txt_f:

            # Initialize CSV
            csv_writer = csv.writer(csv_f)
            csv_writer.writerow(['Title', 'Date', 'Author', 'Categories', 'External Link', 'Domain', 'Post URL'])

            # Initialize JSON
            json_f.write('[')
            first_json_item = True

            # Initialize Unique Links tracking
            seen_links = set()

            try:
                async with aiohttp.ClientSession(headers=headers) as session:
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

                            tasks.append(self.fetch_and_parse(session, current_page, sem))

                        if not tasks:
                            break

                        logger.info(f"Fetching pages {batch_start} to {batch_start + len(tasks) - 1}...")
                        results = await asyncio.gather(*tasks)

                        # Check results
                        stop_detected = False
                        total_batch_posts = 0

                        # Results are ordered by page number
                        for idx, page_posts in enumerate(results):
                            page_idx = batch_start + idx
                            if page_posts is None:
                                # 404 or Error
                                logger.info(f"Page {page_idx} returned 404 or empty. Stopping.")
                                stop_detected = True
                                break
                            elif len(page_posts) == 0:
                                logger.info(f"Page {page_idx} has no articles. Stopping.")
                                stop_detected = True
                                break
                            else:
                                # Write this page's posts incrementally
                                first_json_item = self.save_batch(page_posts, json_f, csv_writer, txt_f, seen_links, first_json_item)
                                total_batch_posts += len(page_posts)

                        if total_batch_posts > 0:
                            logger.info(f"Saved {total_batch_posts} posts from batch.")

                        if stop_detected:
                            break

                        if self.max_pages and (batch_start + len(tasks) - 1) >= self.max_pages:
                            logger.info("Reached max pages limit.")
                            break

                        page_num += len(tasks)
                        # Small delay between batches
                        await asyncio.sleep(0.5)
            finally:
                # Finalize JSON even on error
                json_f.write('\n]')

    def save_batch(self, posts: List[Dict], json_f, csv_writer, txt_f, seen_links: Set[str], is_first_item: bool) -> bool:
        for post in posts:
            # CSV
            csv_writer.writerow([
                post.get('title', ''),
                post.get('date', ''),
                post.get('author', ''),
                ", ".join(post.get('categories', [])),
                post.get('external_link', ''),
                post.get('domain', ''),
                post.get('post_url', '')
            ])

            # TXT
            link = post.get('external_link')
            if link and link not in seen_links:
                seen_links.add(link)
                txt_f.write(link + '\n')

            # JSON
            if not is_first_item:
                json_f.write(',\n')
            else:
                json_f.write('\n')
                is_first_item = False

            json.dump(post, json_f, indent=4, ensure_ascii=False)

        return is_first_item

    async def fetch_and_parse(self, session, page_num, sem):
        async with sem:
            html = await self.fetch_page(session, page_num)
            if html:
                return await self.parse_page(html)
            return None

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
