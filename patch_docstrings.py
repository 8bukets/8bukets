import re

# Update scraper.py
with open('scraper.py', 'r') as f:
    code = f.read()

clean_text_old = """    def clean_text(self, text: str) -> str:
        \"\"\"Normalize whitespace and remove non-breaking spaces.\"\"\""""
clean_text_new = """    def clean_text(self, text: str) -> str:
        \"\"\"
        Normalize whitespace and remove non-breaking spaces from text.

        Args:
            text (str): The raw text to clean.

        Returns:
            str: The cleaned string with normalized whitespace.
        \"\"\""""
code = code.replace(clean_text_old, clean_text_new)

is_url_old = """    def is_url(self, text: str) -> bool:
        \"\"\"Check if text looks like a URL.\"\"\""""
is_url_new = """    def is_url(self, text: str) -> bool:
        \"\"\"
        Check if text looks like a valid URL.

        Args:
            text (str): The string to check.

        Returns:
            bool: True if it starts with http:// or https://, False otherwise.
        \"\"\""""
code = code.replace(is_url_old, is_url_new)

extract_cat_old = """    def extract_categories(self, article: BeautifulSoup) -> List[str]:
        \"\"\"Extract categories from article class names.\"\"\""""
extract_cat_new = """    def extract_categories(self, article: BeautifulSoup) -> List[str]:
        \"\"\"
        Extract categories from article class names.

        Args:
            article (BeautifulSoup): The parsed article HTML element.

        Returns:
            List[str]: A list of category names formatted as title case.
        \"\"\""""
code = code.replace(extract_cat_old, extract_cat_new)

extract_dom_old = """    def extract_domain(self, url: str) -> Optional[str]:
        \"\"\"Extract domain from URL.\"\"\""""
extract_dom_new = """    def extract_domain(self, url: str) -> Optional[str]:
        \"\"\"
        Extract domain from a given URL.

        Args:
            url (str): The full URL string.

        Returns:
            Optional[str]: The parsed domain name without 'www.', or None if invalid.
        \"\"\""""
code = code.replace(extract_dom_old, extract_dom_new)

fetch_page_old = """    async def fetch_page(self, session: aiohttp.ClientSession, page_num: int) -> Optional[str]:"""
fetch_page_new = """    async def fetch_page(self, session: aiohttp.ClientSession, page_num: int) -> Optional[str]:
        \"\"\"
        Asynchronously fetch the HTML content for a specific page number.

        Args:
            session (aiohttp.ClientSession): The active client session.
            page_num (int): The page number to fetch.

        Returns:
            Optional[str]: The raw HTML text, or None if 404 or an error occurs.
        \"\"\""""
code = code.replace(fetch_page_old, fetch_page_new)

parse_page_old = """    async def parse_page(self, html: str) -> List[Dict]:"""
parse_page_new = """    async def parse_page(self, html: str) -> List[Dict]:
        \"\"\"
        Parse the HTML content of a page and extract post data.

        Args:
            html (str): The raw HTML string.

        Returns:
            List[Dict]: A list of dictionaries, each containing extracted post metadata.
        \"\"\""""
code = code.replace(parse_page_old, parse_page_new)

scrape_old = """    async def scrape(self):"""
scrape_new = """    async def scrape(self):
        \"\"\"
        Main asynchronous method to manage the scraping process.
        Controls concurrency, pagination, and output writing.
        If dry_run is True, it processes pages without saving to files.
        \"\"\""""
code = code.replace(scrape_old, scrape_new)

fetch_parse_old = """    async def fetch_and_parse(self, session, page_num, sem):"""
fetch_parse_new = """    async def fetch_and_parse(self, session, page_num, sem):
        \"\"\"
        Helper method to fetch and parse a page while respecting concurrency limits.

        Args:
            session: The HTTP session.
            page_num: Page to fetch.
            sem: Semaphore for controlling concurrency.

        Returns:
            List of parsed posts, or None if failed.
        \"\"\""""
code = code.replace(fetch_parse_old, fetch_parse_new)

with open('scraper.py', 'w') as f:
    f.write(code)

# Update analytics.py
with open('analytics.py', 'r') as f:
    code = f.read()

ascii_old = """def create_ascii_bar(count, max_count, bar_length=20):
    \"\"\"Generate an ASCII progress bar.\"\"\""""
ascii_new = """def create_ascii_bar(count, max_count, bar_length=20):
    \"\"\"
    Generate an ASCII progress bar for visualizing distributions.

    Args:
        count (int): The current value.
        max_count (int): The maximum value for scaling.
        bar_length (int): Total character length of the bar.

    Returns:
        str: A string representing the progress bar visually.
    \"\"\""""
code = code.replace(ascii_old, ascii_new)

load_old = """def load_data(filepath):"""
load_new = """def load_data(filepath):
    \"\"\"
    Load scraped JSON data from a file.

    Args:
        filepath (str): Path to the JSON data file.

    Returns:
        List[Dict]: Parsed data. Exits the program if file is missing.
    \"\"\""""
code = code.replace(load_old, load_new)

domain_old = """def get_domain(url):"""
domain_new = """def get_domain(url):
    \"\"\"
    Extract domain from a given URL string.

    Args:
        url (str): The URL.

    Returns:
        str or None: The parsed domain or None if parsing fails.
    \"\"\""""
code = code.replace(domain_old, domain_new)

with open('analytics.py', 'w') as f:
    f.write(code)
