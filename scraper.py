import aiohttp
import asyncio
from bs4 import BeautifulSoup, Comment
import json
import csv
import re
import argparse
import logging
from typing import List, Dict, Optional
from urllib.parse import urlparse
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

BASE_URL = "https://www.oracle.com/news/"

class OracleNewsScraper:
    def __init__(self, output_json: str, output_csv: str, output_txt: str):
        self.output_json = output_json
        self.output_csv = output_csv
        self.output_txt = output_txt

    def clean_text(self, text: str) -> str:
        """Normalize whitespace and remove non-breaking spaces."""
        if not text:
            return ""
        text = text.replace('\xa0', ' ')
        return re.sub(r'\s+', ' ', text).strip()

    def sanitize_for_csv(self, text: str) -> str:
        """Prevent CSV formula injection."""
        if text and str(text).startswith(('=', '+', '-', '@')):
            return f"'{text}"
        return text

    def parse_date(self, date_text: str) -> Optional[Dict[str, str]]:
        """Parse date string like 'Oct 15, 2025' to ISO format."""
        try:
            dt = datetime.strptime(date_text, '%b %d, %Y')
            return {
                'display': dt.strftime('%b %d, %Y'),
                'iso': dt.isoformat()
            }
        except ValueError:
            logger.warning(f"Could not parse date: {date_text}")
            return {
                'display': date_text,
                'iso': None
            }

    async def fetch_page(self, session: aiohttp.ClientSession) -> Optional[str]:
        try:
            async with session.get(BASE_URL) as response:
                response.raise_for_status()
                return await response.text()
        except aiohttp.ClientError as e:
            logger.error(f"Error fetching page: {e}")
            return None

    def parse_page(self, html: str) -> List[Dict]:
        soup = BeautifulSoup(html, 'html.parser')

        # Find comments containing the news section
        comments = soup.find_all(string=lambda text: isinstance(text, Comment))
        news_html = None
        for c in comments:
            if 'rc92v0' in c and '<section' in c:
                news_html = c
                break

        if not news_html:
            logger.warning("Could not find hidden news section in HTML comments.")
            return []

        news_soup = BeautifulSoup(news_html, 'html.parser')
        articles = news_soup.find_all('li', class_='rc92w3')
        page_posts = []

        for article in articles:
            post_data = {}

            # Date
            date_tag = article.select_one('.rc92-dt')
            date_text = self.clean_text(date_tag.get_text()) if date_tag else ""
            parsed_date = self.parse_date(date_text)
            post_data['date'] = parsed_date['display']
            post_data['datetime'] = parsed_date['iso']

            # Title & Link
            title_text = ""
            external_link = None
            title_tag = article.select_one('h5 a')
            if title_tag:
                title_text = self.clean_text(title_tag.get_text())
                raw_link = title_tag.get('href')
                if raw_link:
                    if raw_link.startswith('/'):
                        external_link = f"https://www.oracle.com{raw_link}"
                    else:
                        external_link = raw_link

            post_data['title'] = title_text
            post_data['external_link'] = external_link
            post_data['post_url'] = external_link

            # Domain
            post_data['domain'] = 'oracle.com'
            if external_link:
                try:
                    post_data['domain'] = urlparse(external_link).netloc.replace('www.', '')
                except:
                    pass

            # Author (Default)
            post_data['author'] = "Oracle"

            # Categories (Default/Inferred)
            post_data['categories'] = ["News"]
            if external_link and '/announcement/' in external_link:
                 post_data['categories'].append("Announcement")

            page_posts.append(post_data)

        return page_posts

    async def scrape(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        async with aiohttp.ClientSession(headers=headers) as session:
            logger.info(f"Fetching {BASE_URL}...")
            html = await self.fetch_page(session)
            if html:
                posts = self.parse_page(html)
                logger.info(f"Extracted {len(posts)} posts.")
                self.save_data(posts)
            else:
                logger.error("Failed to retrieve content.")

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
    parser = argparse.ArgumentParser(description="Scraper for Oracle News")
    parser.add_argument("--json", default="links.json", help="Output JSON filename")
    parser.add_argument("--csv", default="links.csv", help="Output CSV filename")
    parser.add_argument("--txt", default="unique_links.txt", help="Output TXT filename for unique links")

    args = parser.parse_args()

    scraper = OracleNewsScraper(
        output_json=args.json,
        output_csv=args.csv,
        output_txt=args.txt
    )

    asyncio.run(scraper.scrape())

if __name__ == "__main__":
    main()
