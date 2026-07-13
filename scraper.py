import re
import aiohttp
import asyncio
from bs4 import BeautifulSoup, SoupStrainer
import json
import csv
import argparse
import logging
import time
import sys
from typing import List, Dict, Optional, Set
from urllib.parse import urlparse
from concurrent.futures import ProcessPoolExecutor

URL_REGEX = re.compile(r'^https?://')

class UXFormatter(logging.Formatter):
    EMOJIS = {
        'Fetching': '📥',
        'Saved': '💾',
        'Error': '❌',
        'Stopping': '🛑',
        'Reached': '🏁',
        'Page': '📄'
    }

    def format(self, record):
        msg = super().format(record)
        if hasattr(sys.stdout, 'isatty') and sys.stdout.isatty():
            if record.levelno == logging.INFO:
                msg = f"\033[96m{msg}\033[0m"  # Cyan
            elif record.levelno == logging.WARNING:
                msg = f"\033[93m{msg}\033[0m"  # Yellow
            elif record.levelno == logging.ERROR:
                msg = f"\033[91m{msg}\033[0m"  # Red

        for key, emoji in self.EMOJIS.items():
            if key in record.getMessage():
                msg = f"{emoji} {msg}"
                break
        return msg

# Configure logging
class ColorFormatter(logging.Formatter):
    grey = "\x1b[38;20m"
    green = "\x1b[32;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format_str = "%(asctime)s - %(levelname)s - %(message)s"

    FORMATS = {
        logging.DEBUG: grey + format_str + reset,
        logging.INFO: green + format_str + reset,
        logging.WARNING: yellow + format_str + reset,
        logging.ERROR: red + format_str + reset,
        logging.CRITICAL: bold_red + format_str + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt='%H:%M:%S')
        return formatter.format(record)

# Setup root logger
root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)

# Avoid duplicate handlers if re-imported
if not root_logger.handlers:
    ch = logging.StreamHandler()
    if sys.stderr.isatty():
        ch.setFormatter(ColorFormatter())
    else:
        ch.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", datefmt='%H:%M:%S'))
    root_logger.addHandler(ch)

logger = logging.getLogger(__name__)

DEFAULT_BASE_URL = "https://artmusicpage.wordpress.com/"

class WordpressScraperAsync:
    def __init__(self, base_url: str, output_json: str, output_csv: str, output_txt: str, max_pages: Optional[int] = None, concurrency: int = 5):
        self.base_url = base_url if base_url.endswith('/') else f"{base_url}/"
        self.output_json = output_json
        self.output_csv = output_csv
        self.output_txt = output_txt
        self.max_pages = max_pages
        self.concurrency = concurrency
        self.session = None
        self.disallowed_paths = []
        self.URL_REGEX = re.compile(r'^https?://')

    def set_disallowed_paths(self, paths: List[str]):
        self.disallowed_paths = paths

    def is_allowed(self, url: str) -> bool:
        if not self.disallowed_paths:
            return True
        path = urlparse(url).path
        for disallowed in self.disallowed_paths:
            if path.startswith(disallowed):
                return False
        return True

    WHITESPACE_PATTERN = re.compile(r'\s+')
    URL_PATTERN = re.compile(r'^https?://')

    def clean_text(self, text: str) -> str:
        """Normalize whitespace and remove non-breaking spaces.

        Optimization: " ".join(text.split()) is ~6x faster than regex re.sub
        for whitespace normalization.
        """
        if not text:
            return ""
        text = text.replace('\xa0', ' ')
        return " ".join(text.split())

    def is_url(self, text: str) -> bool:
        """Check if text looks like a URL."""
        return self.URL_REGEX.match(text.strip()) is not None

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
        url = f"{self.base_url}page/{page_num}/" if page_num > 1 else self.base_url
        if not self.is_allowed(url):
            logger.info(f"Skipping disallowed URL: {url}")
            return None
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
        soup = BeautifulSoup(html, 'lxml')
        articles = soup.find_all('article', class_='post')
        page_posts = []

        if not articles:
            return []

        for article in articles:
            post_data = {}

            # Title
            title_text = ""
            # Support both h1 and h2 for entry title
            title_tag = article.select_one('h1.entry-title a, h2.entry-title a, .entry-title a')
            if title_tag:
                title_text = self.clean_text(title_tag.get_text())
                post_data['title'] = title_text

            # Date
            date_tag = article.find('time', class_='entry-date')
            if date_tag:
                post_data['date'] = self.clean_text(date_tag.get_text())
                post_data['datetime'] = date_tag.get('datetime')

            # Author
            author_container = article.find(class_='vcard')
            author_tag = author_container.find(class_='fn') if author_container else None
            if author_tag:
                post_data['author'] = self.clean_text(author_tag.get_text())
            else:
                post_data['author'] = None

            # Categories
            post_data['categories'] = self.extract_categories(article)

            # External Link
            external_link = None
            content_div = article.find(class_='entry-content')

            if content_div:
                link_tag = content_div.find('a')
                if link_tag:
                    external_link = link_tag.get('href')

                if not external_link:
                    iframe_tag = content_div.find('iframe')
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

        json_f = None
        csv_f = None
        txt_f = None

        # Open files for incremental writing
        try:
            json_f = open(self.output_json, 'w', encoding='utf-8')
            csv_f = open(self.output_csv, 'w', newline='', encoding='utf-8')
            txt_f = open(self.output_txt, 'w', encoding='utf-8')

            # Write headers
            json_f.write('[\n')
            csv_writer = csv.writer(csv_f)
            csv_writer.writerow(['Title', 'Date', 'Author', 'Categories', 'External Link', 'Domain', 'Post URL'])

            is_first_item = True
            unique_links = set()
            total_fetched = 0

            # Headers
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }

            async with aiohttp.ClientSession(headers=headers) as session:
                pending = set()
                stop_detected = False
                highest_empty_page = float('inf')

                # Initial batch
                for _ in range(self.concurrency):
                    if self.max_pages and page_num > self.max_pages:
                        break
                    pending.add(asyncio.create_task(self.fetch_and_parse(session, page_num, sem)))
                    page_num += 1

                while pending:
                    done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)

                    for task in done:
                        try:
                            page_idx, page_posts = task.result()
                        except Exception as e:
                            logger.error(f"Task failed: {e}")
                            continue

                        if page_idx >= highest_empty_page:
                            # We already found an earlier page that was empty, ignore this one
                            continue

                        if page_posts is None or len(page_posts) == 0:
                            reason = "404 or empty" if page_posts is None else "has no articles"
                            logger.info(f"🛑 Page {page_idx} {reason}. Stopping.")
                            stop_detected = True
                            if page_idx < highest_empty_page:
                                highest_empty_page = page_idx
                            continue

                        logger.info(f"✅ Fetched page {page_idx} with {len(page_posts)} posts.")

                        # Process posts incrementally
                        total_fetched += len(page_posts)
                        for post in page_posts:
                            # JSON
                            if not is_first_item:
                                json_f.write(',\n')
                            json.dump(post, json_f, indent=4, ensure_ascii=False)
                            is_first_item = False

                            # CSV
                            csv_writer.writerow([
                                self.sanitize_for_csv(post.get('title', '')),
                                self.sanitize_for_csv(post.get('date', '')),
                                self.sanitize_for_csv(post.get('author', '')),
                                self.sanitize_for_csv(", ".join(post.get('categories', []))),
                                self.sanitize_for_csv(post.get('external_link', '')),
                                self.sanitize_for_csv(post.get('domain', '')),
                                self.sanitize_for_csv(post.get('post_url', ''))
                            ])

                            # TXT
                            link = post.get('external_link')
                            if link and link not in unique_links:
                                unique_links.add(link)
                                txt_f.write(link + '\n')

                        # Add a new task if we haven't detected a stop condition and haven't hit the limit
                        if not stop_detected and (not self.max_pages or page_num <= self.max_pages):
                            pending.add(asyncio.create_task(self.fetch_and_parse(session, page_num, sem)))
                            page_num += 1

            json_f.write('\n]\n')

            print("\n" + "="*40)
            print(f"📊 Scraping Summary")
            print("="*40)
            print(f"✅ Total Posts Fetched: {total_fetched}")
            print(f"🔗 Unique Links Found: {len(unique_links)}")
            print("-" * 40)
            print(f"{'📁 JSON Report:':<20} {self.output_json} (Saved)")
            print(f"{'📄 CSV Report:':<20} {self.output_csv} (Saved)")
            print(f"{'📝 Links List:':<20} {self.output_txt} (Saved)")
            print("="*40 + "\n")

        except IOError as e:
            logger.error(f"Error saving data: {e}")
        finally:
            if json_f: json_f.close()
            if csv_f: csv_f.close()
            if txt_f: txt_f.close()

    async def fetch_and_parse(self, session, page_num, sem):
        async with sem:
            html = await self.fetch_page(session, page_num)
            if html:
                return page_num, await self.parse_page(html)
            return page_num, None

    def sanitize_for_csv(self, text: str) -> str:
        """Sanitize text to prevent CSV injection."""
        if not text:
            return ""
        text = str(text)
        if text.startswith(('=', '+', '-', '@')):
            return "'" + text
        return text


def main():
    parser = argparse.ArgumentParser(description="Async Scraper for WordPress blogs")
    parser.add_argument("--url", default=DEFAULT_BASE_URL, help="Base URL of the WordPress blog")
    parser.add_argument("--json", default="links.json", help="Output JSON filename")
    parser.add_argument("--csv", default="links.csv", help="Output CSV filename")
    parser.add_argument("--txt", default="unique_links.txt", help="Output TXT filename for unique links")
    parser.add_argument("--limit", type=int, help="Limit number of pages to scrape")
    parser.add_argument("--concurrency", type=int, default=5, help="Number of concurrent requests")

    args = parser.parse_args()

    scraper = WordpressScraperAsync(
        base_url=args.url,
        output_json=args.json,
        output_csv=args.csv,
        output_txt=args.txt,
        max_pages=args.limit,
        concurrency=args.concurrency
    )

    asyncio.run(scraper.scrape())

if __name__ == "__main__":
    main()
