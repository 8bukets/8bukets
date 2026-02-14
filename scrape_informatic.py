import requests
from bs4 import BeautifulSoup
import json
import time
import logging
import argparse
import sys
from urllib.parse import urlparse
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from dataclasses import dataclass, asdict
from typing import List, Optional
from markdownify import markdownify as md

@dataclass
class Post:
    title: Optional[str]
    post_url: Optional[str]
    date: Optional[str]
    date_text: Optional[str]
    categories: List[str]
    content: str
    external_links: List[str]
    image_url: Optional[str]

BASE_URL = "https://informaticmagazine.data.blog"

class Colors:
    CYAN, GREEN, YELLOW, RED = '\033[96m', '\033[92m', '\033[93m', '\033[91m'
    BOLD, RESET = '\033[1m', '\033[0m'

    @staticmethod
    def style(text, color): return f"{color}{text}{Colors.RESET}"

def print_summary(count, outfile, duration):
    width = 50
    # Width (50) - Borders (2) - Padding/Labels (17) - Space (1) = 30 chars for value
    outfile_trunc = (outfile[:27] + '...') if len(outfile) > 30 else outfile

    print(f"\n{Colors.CYAN}┌{'─' * (width - 2)}┐{Colors.RESET}")
    print(f"{Colors.CYAN}│{Colors.RESET} {Colors.BOLD}Scrape Complete{Colors.RESET}{' ' * (width - 18)}{Colors.CYAN}│{Colors.RESET}")
    print(f"{Colors.CYAN}├{'─' * (width - 2)}┤{Colors.RESET}")
    print(f"{Colors.CYAN}│{Colors.RESET} Total Posts:    {Colors.GREEN}{count:<30}{Colors.RESET} {Colors.CYAN}│{Colors.RESET}")
    print(f"{Colors.CYAN}│{Colors.RESET} Duration:       {Colors.YELLOW}{duration:.2f}s{Colors.RESET}{' ' * (30 - len(f'{duration:.2f}s'))} {Colors.CYAN}│{Colors.RESET}")
    print(f"{Colors.CYAN}│{Colors.RESET} Output:         {Colors.BOLD}{outfile_trunc:<30}{Colors.RESET} {Colors.CYAN}│{Colors.RESET}")
    print(f"{Colors.CYAN}└{'─' * (width - 2)}┘{Colors.RESET}\n")

def configure_logging(verbose: bool):
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format=f'%(asctime)s - {Colors.BOLD}%(levelname)s{Colors.RESET} - %(message)s',
        stream=sys.stdout
    )

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

def is_external_link(link_url: str, base_url: str) -> bool:
    """
    Checks if a link is external to the base domain.
    """
    if not link_url:
        return False

    try:
        parsed_link = urlparse(link_url)
        parsed_base = urlparse(base_url)
    except Exception:
        return False

    # If netloc is empty (relative link), it's internal
    if not parsed_link.netloc:
        return False

    return parsed_link.netloc != parsed_base.netloc

def parse_post_html(post_soup, base_url: str) -> Post:
    """
    Parses a single article soup object and returns a Post object.
    """
    # Title
    title_tag = post_soup.find('h2', class_='entry-title')
    title = None
    post_url = None
    if title_tag and title_tag.find('a'):
        title = title_tag.find('a').get_text(strip=True)
        post_url = title_tag.find('a')['href']

    # Date
    date_tag = post_soup.find('time', class_='entry-date')
    date_iso = None
    date_text = None
    if date_tag:
        date_iso = date_tag.get('datetime')
        date_text = date_tag.get_text(strip=True)

    # Category
    cat_links = post_soup.find('span', class_='cat-links')
    categories = []
    if cat_links:
        categories = [a.get_text(strip=True) for a in cat_links.find_all('a')]

    # Content and External Links
    content_div = post_soup.find('div', class_='entry-content')
    external_links = []
    content_text = ""

    if content_div:
        # Convert HTML to Markdown
        content_text = md(str(content_div)).strip()

        # Extract external links
        for link in content_div.find_all('a'):
            href = link.get('href')
            if href and is_external_link(href, base_url):
                external_links.append(href)

    # Image
    img = post_soup.find('div', class_='featured-image')
    image_url = None
    if img and img.find('img'):
            image_url = img.find('img').get('src')

    return Post(
        title=title,
        post_url=post_url,
        date=date_iso,
        date_text=date_text,
        categories=categories,
        content=content_text,
        external_links=external_links,
        image_url=image_url
    )

def scrape(output_file: str, max_pages: int = 0):
    start_time = time.time()
    session = get_session()
    all_posts = []
    page = 1
    current_url = BASE_URL

    while current_url:
        if max_pages > 0 and page > max_pages:
            logging.info(f"Reached max pages limit ({max_pages}). Stopping.")
            break

        logging.info(f"Scraping page {page}: {Colors.CYAN}{current_url}{Colors.RESET}...")
        try:
            response = session.get(current_url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            logging.error(f"{Colors.RED}Error fetching {current_url}: {e}{Colors.RESET}")
            break

        soup = BeautifulSoup(response.content, 'html.parser')

        posts = soup.find_all('article')
        logging.info(f"Found {Colors.BOLD}{len(posts)}{Colors.RESET} posts on page {page}.")

        for post_soup in posts:
            try:
                post_obj = parse_post_html(post_soup, BASE_URL)
                all_posts.append(post_obj)
            except Exception as e:
                logging.error(f"Error parsing post on page {page}: {e}")

        # Pagination
        nav_previous = soup.find('div', class_='nav-previous')
        if nav_previous and nav_previous.find('a'):
            current_url = nav_previous.find('a')['href']
            page += 1
            time.sleep(1) # Polite delay
        else:
            current_url = None
            logging.info("No more pages found.")

    duration = time.time() - start_time
    logging.info(f"Total posts scraped: {len(all_posts)}")

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump([asdict(p) for p in all_posts], f, indent=4, ensure_ascii=False)
        logging.info(f"Saved to {Colors.GREEN}{output_file}{Colors.RESET}")
    except IOError as e:
        logging.error(f"{Colors.RED}Failed to save output to {output_file}: {e}{Colors.RESET}")

    print_summary(len(all_posts), output_file, duration)

def main():
    parser = argparse.ArgumentParser(description="Scrape informaticmagazine.data.blog")
    parser.add_argument("-o", "--output", default="data.json", help="Output JSON file path (default: data.json)")
    parser.add_argument("-n", "--pages", type=int, default=0, help="Maximum number of pages to scrape (0 for all)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose logging")

    args = parser.parse_args()

    configure_logging(args.verbose)
    scrape(args.output, args.pages)

if __name__ == "__main__":
    main()
