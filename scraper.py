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
from typing import List, Dict, Optional, Set, Tuple
from urllib.parse import urlparse

# ANSI Colors
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

def colorize(text: str, color: str) -> str:
    """Apply ANSI color if stdout is a TTY."""
    if sys.stdout.isatty():
        return f"{color}{text}{Colors.RESET}"
    return text

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
            logger.error(colorize(f"✘ Error fetching page {page_num}: {e}", Colors.RED))
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
                        page_num, page_posts = await task

                        if page_posts is None:
                            # 404 or Error
                            logger.info(colorize(f"⚠ Page {page_num} returned 404 or error. Stopping new scheduling.", Colors.YELLOW))
                            stop_scheduling = True
                        elif len(page_posts) == 0:
                            logger.info(colorize(f"⚠ Page {page_num} has no articles. Stopping new scheduling.", Colors.YELLOW))
                            stop_scheduling = True
                        else:
                            logger.info(colorize(f"✔ Page {page_num} scraped ({len(page_posts)} posts).", Colors.GREEN))
                            results.append((page_num, page_posts))
                    except Exception as e:
                        logger.error(colorize(f"✘ Task failed: {e}", Colors.RED))
                        # If a task fails unpredictably, we generally might want to continue or retry.
                        # For now, we assume it's a transient error or a bad page, but don't stop everything unless necessary.
                        # But typically consistent failure implies we should stop or retry.
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

        self.save_data(all_posts)

        # Summary
        elapsed_time = time.time() - start_time
        total_pages = len(results)
        unique_links_count = len(set(p.get('external_link') for p in all_posts if p.get('external_link')))

        summary = [
            colorize("==================================================", Colors.BOLD),
            colorize(f"           🎉 SCRAPING COMPLETE 🎉", Colors.GREEN),
            colorize("==================================================", Colors.BOLD),
            f"  📄 Total Pages:      {total_pages}",
            f"  📝 Total Posts:      {len(all_posts)}",
            f"  🔗 Unique Links:     {unique_links_count}",
            f"  ⏱  Time Taken:       {elapsed_time:.2f}s",
            colorize("==================================================", Colors.BOLD)
        ]

        for line in summary:
            logger.info(line)

    async def fetch_and_parse(self, session, page_num) -> Tuple[int, Optional[List[Dict]]]:
        html = await self.fetch_page(session, page_num)
        if html:
            posts = await self.parse_page(html)
            return page_num, posts
        return page_num, None

    def save_data(self, posts: List[Dict]):
        # JSON
        try:
            with open(self.output_json, 'w', encoding='utf-8') as f:
                json.dump(posts, f, indent=4, ensure_ascii=False)
            logger.info(colorize(f"💾 Saved {len(posts)} posts to {self.output_json}", Colors.CYAN))
        except IOError as e:
            logger.error(colorize(f"✘ Failed to save JSON: {e}", Colors.RED))

        # CSV
        try:
            with open(self.output_csv, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Title', 'Date', 'Author', 'Categories', 'External Link', 'Domain', 'Post URL'])
                for post in posts:
                    writer.writerow([
                        post.get('title', ''),
                        post.get('date', ''),
                        post.get('author', ''),
                        ", ".join(post.get('categories', [])),
                        post.get('external_link', ''),
                        post.get('domain', ''),
                        post.get('post_url', '')
                    ])
            logger.info(colorize(f"💾 Saved {len(posts)} posts to {self.output_csv}", Colors.CYAN))
        except IOError as e:
            logger.error(colorize(f"✘ Failed to save CSV: {e}", Colors.RED))

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
            logger.info(colorize(f"💾 Saved {len(sorted_links)} unique links to {self.output_txt}", Colors.CYAN))
        except IOError as e:
            logger.error(colorize(f"✘ Failed to save TXT: {e}", Colors.RED))

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
