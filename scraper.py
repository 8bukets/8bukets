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
from typing import List, Dict, Optional, Set
from urllib.parse import urlparse, urljoin

class Colors:
    """ANSI color codes for CLI output."""
    RESET = '\033[0m'
    BOLD = '\033[1m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    CYAN = '\033[36m'
    YELLOW = '\033[33m'
    RED = '\033[31m'
    MAGENTA = '\033[35m'

    @staticmethod
    def style(text, color_code):
        if sys.stdout.isatty() or os.environ.get('FORCE_COLOR'):
            return f"{color_code}{text}{Colors.RESET}"
        return text

    @staticmethod
    def strip(text):
        return re.sub(r'\x1b\[[0-9;]*m', '', text)

def print_summary(duration: float, articles_count: int, files: List[str]):
    c = Colors
    width = 50

    # Helper to calculate padding adjustment for double-width emojis
    # We assume each emoji is 1 char in Python string but 2 chars on screen.
    def pad_len(text, target_width):
        # Only count emojis that have len 1 but width 2
        # Rocket 🚀: len 1, width 2 -> Count it
        # Page 📄: len 1, width 2 -> Count it
        # Floppy 💾: len 1, width 2 -> Count it
        # Watch ⏱️: len 2, width 2 -> Do NOT count it (as len matches visual width)
        emoji_count = text.count('🚀') + text.count('📄') + text.count('💾')
        return target_width - 2 - emoji_count

    print(c.style(f"\n┌{'─' * (width - 2)}┐", c.BLUE))

    # Title
    title = " 🚀 Scrape Completed Successfully! "
    print(c.style(f"│{title:<{pad_len(title, width)}}│", c.GREEN))

    print(c.style(f"│{'─' * (width - 2)}│", c.BLUE))

    # Stats
    time_str = f" ⏱️  Time Elapsed: {duration:.2f}s"
    print(c.style(f"│{time_str:<{pad_len(time_str, width)}}│", c.RESET))

    count_str = f" 📄 Articles Found: {articles_count}"
    print(c.style(f"│{count_str:<{pad_len(count_str, width)}}│", c.RESET))

    # Outputs
    outputs_header = " 💾 Outputs:"
    print(c.style(f"│{outputs_header:<{pad_len(outputs_header, width)}}│", c.RESET))

    for f in files:
        line = f"    • {f}"
        print(c.style(f"│{line:<{width - 2}}│", c.CYAN))

    print(c.style(f"└{'─' * (width - 2)}┘\n", c.BLUE))

# Configure logging
# Use stdout to ensure logs and summary appear in correct order
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S',
    stream=sys.stdout
)
logger = logging.getLogger(__name__)

BASE_URL = "https://www.oracle.com/news/"

class OracleNewsScraper:
    def __init__(self, output_json: str, output_csv: str, output_txt: str, max_pages: Optional[int] = None, concurrency: int = 5):
        self.output_json = output_json
        self.output_csv = output_csv
        self.output_txt = output_txt
        self.max_pages = max_pages
        self.concurrency = concurrency
        self.base_url = BASE_URL

    def clean_text(self, text: str) -> str:
        """Normalize whitespace and remove non-breaking spaces."""
        if not text:
            return ""
        text = text.replace('\xa0', ' ')
        return re.sub(r'\s+', ' ', text).strip()

    def sanitize_for_csv(self, value: str) -> str:
        """Prevent CSV injection by prepending a single quote to risky fields."""
        if not value:
            return ""
        if value.startswith(('=', '+', '-', '@', '%')):
            return "'" + value
        return value

    async def fetch_page(self, session: aiohttp.ClientSession, url: str) -> Optional[str]:
        try:
            # 30 second global timeout
            timeout = aiohttp.ClientTimeout(total=30)
            async with session.get(url, timeout=timeout) as response:
                if response.status == 404:
                    return None
                response.raise_for_status()
                return await response.text()
        except aiohttp.ClientError as e:
            logger.error(f"Error fetching {url}: {e}")
            return None
        except asyncio.TimeoutError:
            logger.error(f"Timeout fetching {url}")
            return None

    async def parse_page(self, html: str) -> List[Dict]:
        soup = BeautifulSoup(html, 'html.parser')
        # Oracle news uses links in <h3> tags or <a> tags with specific classes or structures.
        # Based on curl output, we saw links like:
        # <a href="/news/announcement/..." data-lbl="..."><h3>Title</h3></a>

        articles = []

        # Find all links that look like announcements
        links = soup.find_all('a', href=True)

        seen_urls = set()

        for link in links:
            href = link.get('href')
            if not href or '/news/announcement/' not in href:
                continue

            # Filter for "google-cloud" as requested
            if 'google-cloud' not in href.lower():
                continue

            full_url = urljoin(self.base_url, href)

            if full_url in seen_urls:
                continue
            seen_urls.add(full_url)

            # Extract title
            title = self.clean_text(link.get_text())
            if not title:
                # Try finding nested h3 or similar
                h3 = link.find('h3')
                if h3:
                    title = self.clean_text(h3.get_text())

            # If still no title, use the URL slug as a fallback title
            if not title:
                slug = href.split('/')[-2] if href.endswith('/') else href.split('/')[-1]
                title = slug.replace('-', ' ').title()

            # Extract Date (heuristic from URL or nearby text)
            # URL format example: ...-2025-12-11/
            date_match = re.search(r'(\d{4}-\d{2}-\d{2})', href)
            date_str = date_match.group(1) if date_match else ""

            article_data = {
                'title': title,
                'date': date_str,
                'author': "Oracle News", # Default author
                'categories': ["Cloud", "Database", "Google Cloud"],
                'external_link': full_url, # The article itself is the link
                'domain': "oracle.com",
                'post_url': full_url
            }
            articles.append(article_data)

        return articles

    async def scrape(self):
        start_time = time.time()
        all_posts = []

        # Headers to mimic browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        async with aiohttp.ClientSession(headers=headers) as session:
            # We only really need to scrape the main news page for this specific task
            # unless there's pagination we can easily follow.
            # The current curl showed just the main page.
            # We'll stick to the main page for now as it contained the relevant future links.

            logger.info(f"Fetching {self.base_url}...")
            html = await self.fetch_page(session, self.base_url)
            if html:
                posts = await self.parse_page(html)
                all_posts.extend(posts)
                logger.info(f"Found {len(posts)} relevant articles.")
            else:
                logger.error("Failed to fetch main news page.")

        self.save_data(all_posts)

        duration = time.time() - start_time
        print_summary(duration, len(all_posts), [self.output_json, self.output_csv, self.output_txt])

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
    parser = argparse.ArgumentParser(description="Scraper for Oracle Database @ Google Cloud News")
    parser.add_argument("--json", default="links.json", help="Output JSON filename")
    parser.add_argument("--csv", default="links.csv", help="Output CSV filename")
    parser.add_argument("--txt", default="unique_links.txt", help="Output TXT filename for unique links")
    parser.add_argument("--limit", type=int, help="Limit number of pages (unused in single page mode)")
    parser.add_argument("--concurrency", type=int, default=5, help="Number of concurrent requests")

    args = parser.parse_args()

    scraper = OracleNewsScraper(
        output_json=args.json,
        output_csv=args.csv,
        output_txt=args.txt,
        max_pages=args.limit,
        concurrency=args.concurrency
    )

    asyncio.run(scraper.scrape())

if __name__ == "__main__":
    main()
