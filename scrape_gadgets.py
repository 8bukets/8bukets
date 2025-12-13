import requests
from bs4 import BeautifulSoup
import json
import time
import argparse
import logging
import sys

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

def scrape_posts(base_url, max_pages):
    all_posts = []
    url = base_url
    page_count = 0
    headers = {
        'User-Agent': USER_AGENT
    }

    while url and page_count < max_pages:
        logger.info(f"Scraping {url}...")
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            logger.error(f"Error fetching {url}: {e}")
            break

        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('article', class_='post')

        posts_on_page = 0
        for article in articles:
            post_data = {}

            # Extract Title
            title_tag = article.find('h2', class_='entry-title')
            if title_tag and title_tag.find('a'):
                post_data['title'] = title_tag.find('a').get_text(strip=True)
            else:
                post_data['title'] = "No Title"

            # Extract Date
            date_tag = article.find('time', class_='entry-date')
            if date_tag:
                post_data['date'] = date_tag.get_text(strip=True)
            else:
                post_data['date'] = "No Date"

            # Extract External Link
            content_div = article.find('div', class_='entry-content')
            external_link = None
            if content_div:
                link_tag = content_div.find('a')
                if link_tag:
                    external_link = link_tag.get('href')

            post_data['external_link'] = external_link

            # Only add if we found a link
            if external_link:
                all_posts.append(post_data)
                posts_on_page += 1

        logger.info(f"Found {posts_on_page} posts on this page.")

        # Pagination
        nav_previous = soup.find('div', class_='nav-previous')
        if nav_previous and nav_previous.find('a'):
            url = nav_previous.find('a')['href']
            page_count += 1
            if page_count < max_pages:
                time.sleep(1) # Be polite
        else:
            logger.info("No more pages found.")
            url = None

    return all_posts

def main():
    parser = argparse.ArgumentParser(description="Scrape gadget posts from infogadgettech.wordpress.com")
    parser.add_argument("--url", type=str, default=DEFAULT_BASE_URL, help="Base URL to start scraping from")
    parser.add_argument("--output", type=str, default=DEFAULT_OUTPUT_FILE, help="Output JSON file")
    parser.add_argument("--pages", type=int, default=DEFAULT_MAX_PAGES, help="Maximum number of pages to scrape")

    args = parser.parse_args()

    logger.info(f"Starting scrape. URL: {args.url}, Pages: {args.pages}")
    data = scrape_posts(args.url, args.pages)

    try:
        with open(args.output, 'w') as f:
            json.dump(data, f, indent=4)
        logger.info(f"Scraped {len(data)} posts. Saved to {args.output}")
    except IOError as e:
        logger.error(f"Error saving to file {args.output}: {e}")

if __name__ == "__main__":
    main()
