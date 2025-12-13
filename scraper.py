import requests
from bs4 import BeautifulSoup
import json
import csv
import time
import logging
import argparse
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from typing import List, Dict, Set, Optional, Tuple, Any
from urllib.parse import urlparse

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

class MalubeachScraper:
    """
    Scraper for malubeach.wordpress.com.
    """
    BASE_URL = 'https://malubeach.wordpress.com'

    def __init__(self, output_json: str = 'links.json', output_csv: str = 'links.csv', output_txt: str = 'unique_links.txt'):
        self.output_json = output_json
        self.output_csv = output_csv
        self.output_txt = output_txt
        self.session = self._get_session()
        self.all_data: List[Dict[str, Any]] = []
        self.unique_links: Set[str] = set()

    def _get_session(self) -> requests.Session:
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

    def is_external_link(self, link: str) -> bool:
        """
        Checks if a link is external (not belonging to malubeach.wordpress.com).
        """
        try:
            parsed = urlparse(link)
            # Check if domain ends with wordpress.com or is relative
            if not parsed.netloc:
                return False # Relative link
            if 'malubeach.wordpress.com' in parsed.netloc:
                return False
            # Optional: Filter out other wordpress artifacts like share links if desired,
            # but usually "external" means "not this site".
            return True
        except Exception:
            return False

    def parse_page(self, html_content: str) -> Tuple[List[Dict[str, Any]], Optional[str]]:
        """
        Parses the HTML content of a page.
        Returns a list of extracted data items and the next page URL.
        """
        soup = BeautifulSoup(html_content, 'html.parser')
        articles = soup.find_all('article')
        page_data = []

        for article in articles:
            # Extract Title
            title_tag = article.find('h2', class_='entry-title')
            title = title_tag.get_text(strip=True) if title_tag else "No Title"

            # Extract Date
            date_tag = article.find('time', class_='entry-date published')
            date = date_tag.get_text(strip=True) if date_tag else "No Date"

            # Extract External Links
            content_div = article.find('div', class_='entry-content')
            links_in_post = []
            if content_div:
                for a_tag in content_div.find_all('a', href=True):
                    href = a_tag['href']
                    if self.is_external_link(href):
                        links_in_post.append(href)

            # Create an entry for each external link found
            if links_in_post:
                for link in links_in_post:
                    page_data.append({
                        'title': title,
                        'date': date,
                        'link': link
                    })
            else:
                # Decide if we want to keep posts with no external links.
                # The requirement says "extract... external links found in the posts".
                # If no link, maybe we don't save it?
                # Let's save it with link=None or just skip it?
                # Previous implementation filtered `if external_link`. I will stick to that.
                pass

        # Find next page
        next_url = None
        nav_previous = soup.find('div', class_='nav-previous')
        if nav_previous:
            link = nav_previous.find('a')
            if link:
                next_url = link['href']

        return page_data, next_url

    def fetch_page(self, url: str) -> Optional[str]:
        """
        Fetches the content of a URL.
        """
        try:
            logger.info(f"Scraping {url}...")
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except Exception as e:
            logger.error(f"Error fetching {url}: {e}")
            return None

    def run(self):
        """
        Main execution loop.
        """
        current_url = self.BASE_URL

        try:
            while current_url:
                html = self.fetch_page(current_url)
                if not html:
                    break

                data, next_url = self.parse_page(html)
                self.all_data.extend(data)

                for item in data:
                    self.unique_links.add(item['link'])

                current_url = next_url

                # Be nice to the server
                time.sleep(1)

        except KeyboardInterrupt:
            logger.warning("Scraping interrupted by user. Saving collected data...")
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}", exc_info=True)
        finally:
            self.save_results()

    def save_results(self):
        """
        Saves the collected data to files.
        """
        # Save JSON
        with open(self.output_json, 'w', encoding='utf-8') as f:
            json.dump(self.all_data, f, indent=4, ensure_ascii=False)
        logger.info(f"Saved {len(self.all_data)} items to {self.output_json}")

        # Save CSV
        with open(self.output_csv, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Title', 'Date', 'Link'])
            for item in self.all_data:
                writer.writerow([item['title'], item['date'], item['link']])
        logger.info(f"Saved data to {self.output_csv}")

        # Save Unique Links
        sorted_links = sorted(list(self.unique_links))
        with open(self.output_txt, 'w', encoding='utf-8') as f:
            for link in sorted_links:
                f.write(link + '\n')
        logger.info(f"Saved {len(sorted_links)} unique links to {self.output_txt}")

def main():
    parser = argparse.ArgumentParser(description="Scraper for malubeach.wordpress.com")
    parser.add_argument('--json', default='links.json', help='Output JSON filename')
    parser.add_argument('--csv', default='links.csv', help='Output CSV filename')
    parser.add_argument('--txt', default='unique_links.txt', help='Output TXT filename for unique links')
    args = parser.parse_args()

    scraper = MalubeachScraper(output_json=args.json, output_csv=args.csv, output_txt=args.txt)
    scraper.run()

if __name__ == "__main__":
    main()
