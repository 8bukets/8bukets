import aiohttp
import asyncio
from bs4 import BeautifulSoup, SoupStrainer
import json
import csv
import re
import argparse
import logging
import time
import os
from typing import List, Dict, Optional, Set
from urllib.parse import urlparse
import concurrent.futures

# Configure logging
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class UXFormatter(logging.Formatter):
    def format(self, record):
        # Determine emoji and color
        if record.levelno == logging.INFO:
            if "Saved" in record.msg:
                emoji = "💾"
                color = Colors.GREEN
            elif "Fetching" in record.msg:
                emoji = "📥"
                color = Colors.BLUE
            else:
                emoji = "ℹ️ "
                color = Colors.BLUE
        elif record.levelno == logging.WARNING:
            emoji = "⚠️ "
            color = Colors.WARNING
        elif record.levelno == logging.ERROR:
            emoji = "❌"
            color = Colors.FAIL
        else:
            emoji = ""
            color = Colors.ENDC

        # Format time
        timestamp = self.formatTime(record, "%H:%M:%S")

        # Construct message
        return f"{color}{timestamp} {emoji} {record.getMessage()}{Colors.ENDC}"

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(UXFormatter())
logger.addHandler(handler)

BASE_URL = "https://markposition.wordpress.com/"

def clean_text(text: str) -> str:
    """Normalize whitespace and remove non-breaking spaces."""
    if not text:
        return ""
    text = text.replace('\xa0', ' ')
    return re.sub(r'\s+', ' ', text).strip()

def sanitize_for_csv(text: str) -> str:
    """Sanitize text to prevent CSV injection (formula injection)."""
    if not text:
        return ""
    # If the text starts with one of the trigger characters, prepend a single quote
    if text.startswith(('=', '+', '-', '@', '%')):
        return "'" + text
    return text

def is_url(text: str) -> bool:
    """Check if text looks like a URL."""
    return re.match(r'^https?://', text.strip()) is not None

def extract_categories(article: BeautifulSoup) -> List[str]:
    """Extract categories from article class names."""
    categories = []
    if article.get('class'):
        for cls in article['class']:
            if cls.startswith('category-'):
                cat_name = cls.replace('category-', '').replace('-', ' ').title()
                categories.append(cat_name)
    return categories

def extract_domain(url: str) -> Optional[str]:
    """Extract domain from URL."""
    if not url:
        return None
    try:
        return urlparse(url).netloc.replace('www.', '')
    except:
        return None

def parse_page(html: str) -> List[Dict]:
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
            title_text = clean_text(title_tag.get_text())
            post_data['title'] = title_text

        # Date
        date_tag = article.select_one('time.entry-date')
        if date_tag:
            post_data['date'] = clean_text(date_tag.get_text())
            post_data['datetime'] = date_tag.get('datetime')

        # Author
        author_tag = article.select_one('.author.vcard .fn')
        if author_tag:
            post_data['author'] = clean_text(author_tag.get_text())
        else:
            post_data['author'] = None

        # Categories
        post_data['categories'] = extract_categories(article)

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

        if not external_link and title_text and is_url(title_text):
            external_link = title_text

        post_data['external_link'] = external_link
        post_data['domain'] = extract_domain(external_link)

        # Post URL
        if title_tag:
            post_data['post_url'] = title_tag.get('href')

        page_posts.append(post_data)

    return page_posts

class MarkPositionScraperAsync:
    # Compiled Regexes for performance
    CLEAN_TEXT_REGEX = re.compile(r'\s+')
    IS_URL_REGEX = re.compile(r'^https?://')

    def __init__(self, output_json: str, output_csv: str, output_txt: str, max_pages: Optional[int] = None, concurrency: int = 5):
        self.output_json = self.validate_path(output_json)
        self.output_csv = self.validate_path(output_csv)
        self.output_txt = self.validate_path(output_txt)
        self.max_pages = max_pages
        self.concurrency = concurrency
        self.session = None

    def validate_path(self, path: str) -> str:
        """Validate that the output path is within the current working directory."""
        if not path:
            raise ValueError("Output path cannot be empty")

        # Resolve absolute paths
        abs_path = os.path.abspath(path)
        cwd = os.path.abspath(os.getcwd())

        # Check if the path starts with the CWD
        # os.path.commonpath is the safest way to check path containment
        try:
            common = os.path.commonpath([abs_path, cwd])
        except ValueError:
             # commonpath raises ValueError if paths are on different drives (Windows)
             raise ValueError(f"Security Error: Output path '{path}' is invalid.")

        if common != cwd:
             raise ValueError(f"Security Error: Output path '{path}' attempts to traverse outside the working directory.")

        return abs_path

    def clean_text(self, text: str) -> str:
        """Normalize whitespace and remove non-breaking spaces."""
        if not text:
            return ""
        text = text.replace('\xa0', ' ')
        return self.CLEAN_TEXT_REGEX.sub(' ', text).strip()

    def sanitize_for_csv(self, text: str) -> str:
        """Sanitize text to prevent CSV injection (formula injection)."""
        if not text:
            return ""
        # If the text starts with one of the trigger characters, prepend a single quote
        if text.startswith(('=', '+', '-', '@', '%')):
            return "'" + text
        return text

    def is_url(self, text: str) -> bool:
        """Check if text looks like a URL."""
        return self.IS_URL_REGEX.match(text.strip()) is not None

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
        self.executor = concurrent.futures.ProcessPoolExecutor()

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

<<<<<<< bolt-optimize-scraper-12240886470808254228
    async def parse_page(self, html: str) -> List[Dict]:
        # Optimization: Use SoupStrainer to parse only article tags
        strainer = SoupStrainer('article')
        soup = BeautifulSoup(html, 'html.parser', parse_only=strainer)
        articles = soup.find_all('article', class_='post')
        page_posts = []

        if not articles:
            return []

        for article in articles:
            post_data = {}

            # Title
            # Optimization: Replace select_one with find for performance
            title_text = ""
            # Old: title_tag = article.select_one('h1.entry-title a')
            h1 = article.find('h1', class_='entry-title')
            title_tag = h1.find('a') if h1 else None

            if title_tag:
                title_text = self.clean_text(title_tag.get_text())
                post_data['title'] = title_text

            # Date
            # Old: date_tag = article.select_one('time.entry-date')
            date_tag = article.find('time', class_='entry-date')
            if date_tag:
                post_data['date'] = self.clean_text(date_tag.get_text())
                post_data['datetime'] = date_tag.get('datetime')

            # Author
            # Old: author_tag = article.select_one('.author.vcard .fn')
            # Optimization: 'fn' class is unique enough within the article context
            author_tag = article.find(class_='fn')
            if author_tag:
                post_data['author'] = self.clean_text(author_tag.get_text())
            else:
                post_data['author'] = None

            # Categories
            post_data['categories'] = self.extract_categories(article)

            # External Link
            external_link = None
            # Old: content_div = article.select_one('.entry-content')
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

=======
>>>>>>> sentinel-csv-injection-fix-6855106868508477486
    async def scrape(self):
        all_posts = []
        page_num = 1
        sem = asyncio.Semaphore(self.concurrency)

        # Headers
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        # Set a global timeout for all requests
        timeout = aiohttp.ClientTimeout(total=30)

<<<<<<< bolt-optimize-scraper-12240886470808254228
        async with aiohttp.ClientSession(headers=headers, timeout=timeout) as session:
            # We don't know the total pages, so we have to fetch sequentially or in chunks until we hit 404/empty.
            # Pure concurrent fetching of all pages requires knowing the max page.
            # Heuristic: fetch in batches of `concurrency`. If any page in batch returns 404 or empty, stop.

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
=======
        try:
            async with aiohttp.ClientSession(headers=headers, timeout=timeout) as session:
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
>>>>>>> sentinel-csv-injection-fix-6855106868508477486
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
                            break
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
        finally:
            self.executor.shutdown()

        self.save_data(all_posts)

    async def fetch_and_parse(self, session, page_num, sem):
        async with sem:
            html = await self.fetch_page(session, page_num)
            if html:
                loop = asyncio.get_running_loop()
                return await loop.run_in_executor(self.executor, parse_page, html)
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
                        sanitize_for_csv(post.get('title', '')),
                        sanitize_for_csv(post.get('date', '')),
                        sanitize_for_csv(post.get('author', '')),
                        sanitize_for_csv(", ".join(post.get('categories', []))),
                        sanitize_for_csv(post.get('external_link', '')),
                        sanitize_for_csv(post.get('domain', '')),
                        sanitize_for_csv(post.get('post_url', ''))
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
