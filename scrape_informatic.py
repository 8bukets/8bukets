import requests
from bs4 import BeautifulSoup
import json
import time
import logging
from urllib.parse import urlparse
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

BASE_URL = "https://informaticmagazine.data.blog"

def get_session():
    """
    Creates a requests Session with retry logic and a user-agent.
    """
    session = requests.Session()

    # Retry strategy: 3 retries, exponential backoff
    retry_strategy = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    })

    return session

def is_external_link(link_url, base_url):
    """
    Checks if a link is external to the base domain.
    """
    if not link_url:
        return False

    parsed_link = urlparse(link_url)
    parsed_base = urlparse(base_url)

    # If netloc is empty (relative link), it's internal
    if not parsed_link.netloc:
        return False

    # Check if the domain is the same or a subdomain
    # simplistic check: link domain ends with base domain
    # However, data.blog is the host here.
    # informaticmagazine.data.blog

    return parsed_link.netloc != parsed_base.netloc

def scrape():
    session = get_session()
    all_posts = []
    page = 1
    current_url = BASE_URL

    while current_url:
        logging.info(f"Scraping {current_url}...")
        try:
            response = session.get(current_url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching {current_url}: {e}")
            break

        soup = BeautifulSoup(response.content, 'html.parser')

        posts = soup.find_all('article')
        logging.info(f"Found {len(posts)} posts on page {page}.")

        for post in posts:
            item = {}

            # Title
            title_tag = post.find('h2', class_='entry-title')
            if title_tag and title_tag.find('a'):
                item['title'] = title_tag.find('a').get_text(strip=True)
                item['post_url'] = title_tag.find('a')['href']
            else:
                item['title'] = None
                item['post_url'] = None

            # Date
            date_tag = post.find('time', class_='entry-date')
            if date_tag:
                item['date'] = date_tag.get('datetime')
                item['date_text'] = date_tag.get_text(strip=True)
            else:
                item['date'] = None
                item['date_text'] = None

            # Category
            cat_links = post.find('span', class_='cat-links')
            if cat_links:
                cats = [a.get_text(strip=True) for a in cat_links.find_all('a')]
                item['categories'] = cats
            else:
                item['categories'] = []

            # Content and External Links
            content_div = post.find('div', class_='entry-content')
            external_links = []
            content_text = ""

            if content_div:
                # Extract text
                content_text = content_div.get_text(separator="\n", strip=True)

                # Extract external links
                for link in content_div.find_all('a'):
                    href = link.get('href')
                    if href and is_external_link(href, BASE_URL):
                        external_links.append(href)

            item['content'] = content_text
            item['external_links'] = external_links

            # Image
            img = post.find('div', class_='featured-image')
            if img and img.find('img'):
                 item['image_url'] = img.find('img').get('src')
            else:
                item['image_url'] = None

            all_posts.append(item)

        # Pagination
        nav_previous = soup.find('div', class_='nav-previous')
        if nav_previous and nav_previous.find('a'):
            current_url = nav_previous.find('a')['href']
            page += 1
            time.sleep(1) # Polite delay
        else:
            current_url = None

    logging.info(f"Total posts scraped: {len(all_posts)}")

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(all_posts, f, indent=4, ensure_ascii=False)
    logging.info("Saved to data.json")

if __name__ == "__main__":
    scrape()
