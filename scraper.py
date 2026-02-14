import aiohttp
import asyncio
from bs4 import BeautifulSoup
import json
import csv
import re
import argparse
import logging
import time
import sys
import os
from typing import List, Dict, Optional, Set, Tuple
from urllib.parse import urlparse

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S',
    stream=sys.stdout
)
logger = logging.getLogger(__name__)

BASE_URL = "https://markposition.wordpress.com/"

class Colors:
    """ANSI color codes for CLI output."""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    BOX = '\033[94m'  # Blue for box borders

    @staticmethod
    def style(text: str, *styles) -> str:
        if not sys.stdout.isatty() and not os.environ.get('FORCE_COLOR'):
            return text
        return "".join(styles) + text + Colors.ENDC

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

    async def fetch_page(self, session: aiohttp.ClientSession, page_num: int) -> Tuple[Optional[str], int]:
        url = f"{BASE_URL}page/{page_num}/" if page_num > 1 else BASE_URL
        try:
            async with session.get(url, timeout=10) as response:
                if response.status == 404:
                    return None, 404
                response.raise_for_status()
                text = await response.text()
                return text, response.status
        except Exception as e:
            logger.error(f"Error fetching page {page_num}: {e}")
            return None, 0

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

    def print_summary(self, total_posts: int, unique_links: int, duration: float):
        """Print a beautiful summary box."""
        width = 50

        # Helper to create lines
        def make_line(label, value):
            text_value = str(value)
            # content: " label" + "spaces" + "value "
            # Visible length inside borders = width
            # We have " " (1) + label + padding + value + " " (1)
            # padding = width - 1 - len(label) - len(value) - 1
            padding = width - 2 - len(label) - len(text_value)
            return f"{Colors.BOX}║{Colors.ENDC} {label}{' ' * max(0, padding)}{Colors.BOLD}{text_value}{Colors.ENDC} {Colors.BOX}║{Colors.ENDC}"

        print(f"\n{Colors.BOX}╔{'═' * width}╗{Colors.ENDC}")
        # Title centering
        title = "🎉 Scrape Complete!"
        # We need to center 'title' in 'width' space
        padding_left = (width - len(title)) // 2
        padding_right = width - len(title) - padding_left
        print(f"{Colors.BOX}║{Colors.ENDC}{' ' * padding_left}{Colors.style(title, Colors.BOLD, Colors.GREEN)}{' ' * padding_right}{Colors.BOX}║{Colors.ENDC}")

        print(f"{Colors.BOX}╠{'═' * width}╣{Colors.ENDC}")
        print(make_line("📄 Total Posts:", total_posts))
        print(make_line("🔗 Unique Links:", unique_links))
        print(make_line("⏱️  Duration:", f"{duration:.2f}s"))
        print(make_line("📁 Output:", self.output_json))
        print(f"{Colors.BOX}╚{'═' * (width)}╝{Colors.ENDC}\n")

    async def scrape(self):
        start_time = time.time()
        all_posts = []

        # Headers
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        async with aiohttp.ClientSession(headers=headers) as session:
            tasks = set()
            next_page = 1
            results = []
            stop_scheduling = False

            # Initial fill of the queue
            while len(tasks) < self.concurrency and not stop_scheduling:
                if self.max_pages and next_page > self.max_pages:
                    stop_scheduling = True
                    break

                # Create task
                task = asyncio.create_task(self.fetch_and_parse(session, next_page))
                tasks.add(task)
                next_page += 1

            while tasks:
                # Wait for at least one task to complete
                done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
                tasks = pending

                for task in done:
                    try:
                        page_num, page_posts, status_code = await task

                        if page_posts is None:
                            if status_code == 404:
                                logger.info(f"Page {page_num} returned 404. End of content. Stopping new scheduling.")
                                stop_scheduling = True
                            else:
                                logger.warning(f"Page {page_num} failed (Status: {status_code}). Continuing...")
                                # Do NOT stop scheduling for transient errors
                        elif len(page_posts) == 0:
                            logger.info(f"Page {page_num} has no articles. Stopping new scheduling.")
                            stop_scheduling = True
                        else:
                            logger.info(f"Page {page_num} scraped ({len(page_posts)} posts).")
                            results.append((page_num, page_posts))
                    except Exception as e:
                        logger.error(f"Task failed: {e}")
                        pass

                # Schedule new tasks if slot is available and not stopping
                while len(tasks) < self.concurrency and not stop_scheduling:
                    if self.max_pages and next_page > self.max_pages:
                        stop_scheduling = True
                        break

                    task = asyncio.create_task(self.fetch_and_parse(session, next_page))
                    tasks.add(task)
                    next_page += 1

        # Sort results by page number to ensure order
        results.sort(key=lambda x: x[0])

        for _, posts in results:
            all_posts.extend(posts)

        unique_links_count = self.save_data(all_posts)
        duration = time.time() - start_time

        # Flush stdout to ensure logs are printed before summary
        sys.stdout.flush()
        self.print_summary(len(all_posts), unique_links_count, duration)

    async def fetch_and_parse(self, session, page_num) -> Tuple[int, Optional[List[Dict]], int]:
        html, status = await self.fetch_page(session, page_num)
        if html:
            posts = await self.parse_page(html)
            return page_num, posts, status
        return page_num, None, status

    def save_data(self, posts: List[Dict]) -> int:
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
                    # Sanitize CSV fields starting with special characters
                    row = [
                        post.get('title', ''),
                        post.get('date', ''),
                        post.get('author', ''),
                        ", ".join(post.get('categories', [])),
                        post.get('external_link', ''),
                        post.get('domain', ''),
                        post.get('post_url', '')
                    ]

                    sanitized_row = []
                    for field in row:
                        if field and isinstance(field, str) and field.startswith(('=', '+', '-', '@')):
                            sanitized_row.append("'" + field)
                        else:
                            sanitized_row.append(field)

                    writer.writerow(sanitized_row)
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

        return len(unique_links)

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
