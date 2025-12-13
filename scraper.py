import requests
from bs4 import BeautifulSoup
import json
import csv
import time
import logging
import argparse
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from urllib.parse import urljoin

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

def get_session():
    """
    Creates a requests Session with retry logic and a User-Agent.
    """
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    adapter = HTTPAdapter(max_retries=retries)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    })
    return session

def scrape_page(session, url):
    """
    Scrapes a single page for articles and the next page link.
    Returns a list of extracted data items and the next page URL.
    """
    logger.info(f"Scraping {url}...")
    response = session.get(url, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = soup.find_all('article')
    page_data = []

    for article in articles:
        # Extract Title
        title_tag = article.find('h2', class_='entry-title')
        title = title_tag.get_text(strip=True) if title_tag else "No Title"

        # Extract Date
        date_tag = article.find('time', class_='entry-date published')
        date = date_tag.get_text(strip=True) if date_tag else "No Date"

        # Extract External Link
        # We assume the external link is the first link in the entry-content div
        content_div = article.find('div', class_='entry-content')
        external_link = None
        if content_div:
            link_tag = content_div.find('a')
            if link_tag:
                external_link = link_tag.get('href')

        if external_link:
            page_data.append({
                'title': title,
                'date': date,
                'link': external_link
            })

    # Find next page
    next_url = None
    nav_previous = soup.find('div', class_='nav-previous')
    if nav_previous:
        link = nav_previous.find('a')
        if link:
            next_url = link['href']

    return page_data, next_url

def save_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    logger.info(f"Saved {len(data)} items to {filename}")

def save_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Title', 'Date', 'Link'])
        for item in data:
            writer.writerow([item['title'], item['date'], item['link']])
    logger.info(f"Saved data to {filename}")

def save_unique_links(data, filename):
    unique_links = sorted(list(set(item['link'] for item in data)))
    with open(filename, 'w', encoding='utf-8') as f:
        for link in unique_links:
            f.write(link + '\n')
    logger.info(f"Saved {len(unique_links)} unique links to {filename}")

def main():
    parser = argparse.ArgumentParser(description="Scraper for malubeach.wordpress.com")
    parser.add_argument('--json', default='links.json', help='Output JSON filename')
    parser.add_argument('--csv', default='links.csv', help='Output CSV filename')
    parser.add_argument('--txt', default='unique_links.txt', help='Output TXT filename for unique links')
    args = parser.parse_args()

    base_url = 'https://malubeach.wordpress.com'
    current_url = base_url
    all_data = []

    session = get_session()

    try:
        while current_url:
            data, next_url = scrape_page(session, current_url)
            all_data.extend(data)
            current_url = next_url

            # Be nice to the server
            time.sleep(1)

    except KeyboardInterrupt:
        logger.warning("Scraping interrupted by user. Saving collected data...")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}", exc_info=True)
    finally:
        save_json(all_data, args.json)
        save_csv(all_data, args.csv)
        save_unique_links(all_data, args.txt)

if __name__ == "__main__":
    main()
