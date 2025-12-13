import requests
from bs4 import BeautifulSoup
import json
import time
import argparse
import logging
import sys
from typing import List, Optional
from datetime import datetime
from models import Post

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

DEFAULT_BASE_URL = "https://infogadgettech.wordpress.com"
DEFAULT_OUTPUT_FILE = "gadgets.json"
DEFAULT_MAX_PAGES = 5
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

class GadgetScraper:
    def __init__(self, base_url: str, max_pages: int, user_agent: str = USER_AGENT):
        self.base_url = base_url
        self.max_pages = max_pages
        self.headers = {'User-Agent': user_agent}
        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def fetch_page(self, url: str) -> Optional[str]:
        logger.info(f"Scraping {url}...")
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            return response.content
        except requests.RequestException as e:
            logger.error(f"Error fetching {url}: {e}")
            return None

    def parse_date(self, date_str: str) -> str:
        """Parses date string like 'October 12, 2022' to '2022-10-12'."""
        try:
            # Clean up the string just in case
            date_str = date_str.strip()
            dt = datetime.strptime(date_str, "%B %d, %Y")
            return dt.strftime("%Y-%m-%d")
        except ValueError:
            logger.warning(f"Could not parse date: {date_str}")
            return date_str

    def extract_posts_from_html(self, html_content: str) -> (List[Post], Optional[str]):
        soup = BeautifulSoup(html_content, 'html.parser')
        articles = soup.find_all('article', class_='post')
        posts = []

        for article in articles:
            # Title
            title_tag = article.find('h2', class_='entry-title')
            title = title_tag.find('a').get_text(strip=True) if title_tag and title_tag.find('a') else "No Title"
            original_url = title_tag.find('a')['href'] if title_tag and title_tag.find('a') else None

            # Date
            date_tag = article.find('time', class_='entry-date')
            date_str = date_tag.get_text(strip=True) if date_tag else "No Date"
            formatted_date = self.parse_date(date_str)

            # Author
            author_tag = article.find('span', class_='author')
            author = author_tag.get_text(strip=True) if author_tag else "Unknown"
            if not author_tag:
                 # Try finding it in 'by ...'
                 byline = article.find('span', class_='byline')
                 if byline:
                     author_link = byline.find('a', class_='url')
                     if author_link:
                         author = author_link.get_text(strip=True)

            # Categories and Tags
            categories = []
            tags = []
            cat_links = article.find('span', class_='cat-links')
            if cat_links:
                for link in cat_links.find_all('a'):
                    categories.append(link.get_text(strip=True))

            tag_links = article.find('span', class_='tags-links')
            if tag_links:
                for link in tag_links.find_all('a'):
                    tags.append(link.get_text(strip=True))

            # Image
            image_url = None
            featured_image = article.find('div', class_='featured-image')
            if featured_image:
                img_tag = featured_image.find('img')
                if img_tag:
                    image_url = img_tag.get('src')
                    # Remove query params for cleaner URL if needed, but often they handle resizing
                    if '?w=' in image_url:
                        image_url = image_url.split('?')[0]

            # External Link
            content_div = article.find('div', class_='entry-content')
            external_link = None
            if content_div:
                # Often the first link in the content is the external one for this type of blog
                link_tag = content_div.find('a')
                if link_tag:
                    external_link = link_tag.get('href')

            if external_link:
                post = Post(
                    title=title,
                    date=formatted_date,
                    external_link=external_link,
                    author=author,
                    categories=categories,
                    tags=tags,
                    image_url=image_url,
                    original_url=original_url
                )
                posts.append(post)

        # Pagination
        nav_previous = soup.find('div', class_='nav-previous')
        next_url = None
        if nav_previous and nav_previous.find('a'):
            next_url = nav_previous.find('a')['href']

        return posts, next_url

    def run(self) -> List[Post]:
        all_posts = []
        url = self.base_url
        page_count = 0

        while url and page_count < self.max_pages:
            html_content = self.fetch_page(url)
            if not html_content:
                break

            posts, next_url = self.extract_posts_from_html(html_content)

            logger.info(f"Found {len(posts)} posts on this page.")
            all_posts.extend(posts)

            url = next_url
            page_count += 1

            if url and page_count < self.max_pages:
                time.sleep(1) # Be polite

        return all_posts

def main():
    parser = argparse.ArgumentParser(description="Scrape gadget posts from infogadgettech.wordpress.com")
    parser.add_argument("--url", type=str, default=DEFAULT_BASE_URL, help="Base URL to start scraping from")
    parser.add_argument("--output", type=str, default=DEFAULT_OUTPUT_FILE, help="Output JSON file")
    parser.add_argument("--pages", type=int, default=DEFAULT_MAX_PAGES, help="Maximum number of pages to scrape")

    args = parser.parse_args()

    scraper = GadgetScraper(base_url=args.url, max_pages=args.pages)
    logger.info(f"Starting scrape. URL: {args.url}, Pages: {args.pages}")

    posts = scraper.run()

    posts_data = [post.to_dict() for post in posts]

    try:
        with open(args.output, 'w') as f:
            json.dump(posts_data, f, indent=4)
        logger.info(f"Scraped {len(posts_data)} posts. Saved to {args.output}")
    except IOError as e:
        logger.error(f"Error saving to file {args.output}: {e}")

if __name__ == "__main__":
    main()
