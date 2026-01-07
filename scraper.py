"""
Scraper for wishlist.design.blog.
Collects articles and saves them to SQLite database and JSON file.
"""

import argparse
import json
import logging
import sqlite3
import sys
import time

import requests
from bs4 import BeautifulSoup

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class BlogScraper:
    """Scrapes wishlist.design.blog for articles and metadata."""

    def __init__(self, base_url, output_json="wishlist_data.json", db_name="wishlist_data.db"):
        self.base_url = base_url
        self.output_json = output_json
        self.db_name = db_name
        self.headers = {
            'User-Agent': (
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/91.0.4472.124 Safari/537.36'
            )
        }
        self.data = []

        # Performance: Reuse Session and DB Connection
        self.session = requests.Session()
        self.session.headers.update(self.headers)

        try:
            self.conn = sqlite3.connect(self.db_name)
            self.init_db()
        except sqlite3.Error as e:
            logger.error("Database connection error: %s", e)
            self.conn = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        """Close resources."""
        if self.session:
            self.session.close()
        if self.conn:
            self.conn.close()
            logger.info("Database connection closed.")

    def init_db(self):
        """Initialize the SQLite database."""
        if not self.conn:
            return

        try:
            cursor = self.conn.cursor()
            # Posts table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS posts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    post_url TEXT UNIQUE,
                    external_link TEXT,
                    date_str TEXT,
                    datetime_iso TEXT,
                    author TEXT,
                    categories TEXT,
                    scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')

            # Changes table for tracking updates
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS changes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    post_id INTEGER,
                    field TEXT,
                    old_value TEXT,
                    new_value TEXT,
                    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY(post_id) REFERENCES posts(id)
                )
            ''')
            self.conn.commit()
        except sqlite3.Error as e:
            logger.error("Database initialization error: %s", e)

    def save_to_db(self, item):
        """Save a single item to the database, handling updates."""
        if not self.conn:
            return False

        try:
            cursor = self.conn.cursor()

            # Check if post exists
            cursor.execute(
                "SELECT id, title, external_link FROM posts WHERE post_url = ?",
                (item.get('post_url'),)
            )
            existing_post = cursor.fetchone()

            if existing_post:
                post_id, old_title, old_link = existing_post
                updated = False

                # Check Title Change
                new_title = item.get('title')
                if old_title != new_title and new_title:
                    logger.info("Change detected for %s: Title changed.", item.get('post_url'))
                    cursor.execute(
                        "INSERT INTO changes (post_id, field, old_value, new_value) "
                        "VALUES (?, ?, ?, ?)",
                        (post_id, 'title', old_title, new_title)
                    )
                    cursor.execute("UPDATE posts SET title = ? WHERE id = ?", (new_title, post_id))
                    updated = True

                # Check External Link Change
                new_link = item.get('external_link')
                if old_link != new_link and new_link:
                    logger.info("Change detected for %s: External Link changed.",
                                item.get('post_url'))
                    cursor.execute(
                        "INSERT INTO changes (post_id, field, old_value, new_value) "
                        "VALUES (?, ?, ?, ?)",
                        (post_id, 'external_link', old_link, new_link)
                    )
                    cursor.execute(
                        "UPDATE posts SET external_link = ? WHERE id = ?",
                        (new_link, post_id)
                    )
                    updated = True

                if updated:
                    # Update scraped_at to reflect latest check
                    cursor.execute(
                        "UPDATE posts SET scraped_at = CURRENT_TIMESTAMP WHERE id = ?",
                        (post_id,)
                    )
                    self.conn.commit()
                    return False  # Not a "new" post, but an updated one

            else:
                # Insert new post
                cursor.execute('''
                    INSERT INTO posts (
                        title, post_url, external_link, date_str, datetime_iso, author, categories
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (
                    item.get('title'),
                    item.get('post_url'),
                    item.get('external_link'),
                    item.get('date'),
                    item.get('datetime'),
                    item.get('author'),
                    json.dumps(item.get('categories'))
                ))
                self.conn.commit()
                return True  # New post

        except sqlite3.Error as e:
            logger.error("Database insertion/update error: %s", e)
            return False

        return False

    def fetch_page(self, url):
        """Fetch the content of a page."""
        logger.info("Fetching %s...", url)
        try:
            # Use session for connection reuse
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            return response.content
        except requests.RequestException as e:
            logger.error("Error fetching URL %s: %s", url, e)
            return None

    def parse_article(self, article):
        """Parse an article element and extract data."""
        item = {}

        # Title and Post URL
        title_tag = article.select_one("header.entry-header h2.entry-title a")
        item['title'] = title_tag.get_text(strip=True) if title_tag else None
        item['post_url'] = title_tag.get('href') if title_tag else None

        # Link (External)
        content_div = article.select_one("div.entry-content")
        external_link = None
        if content_div:
            # Check for direct anchor tags
            link_tag = content_div.find("a")
            if link_tag:
                external_link = link_tag.get('href')
                if not external_link:
                    text_content = link_tag.get_text(strip=True)
                    if text_content.startswith('http'):
                        external_link = text_content

            # Fallback
            if not external_link:
                text_content = content_div.get_text(strip=True)
                if text_content.startswith('http'):
                    external_link = text_content.split()[0]

        item['external_link'] = external_link

        # Date
        time_tag = article.select_one(".entry-meta .posted-on time")
        if time_tag:
            item['date'] = time_tag.get_text(strip=True)
            item['datetime'] = time_tag.get('datetime')
        else:
            item['date'] = None
            item['datetime'] = None

        # Author
        author_tag = article.select_one(".entry-meta .byline .author a")
        item['author'] = author_tag.get_text(strip=True) if author_tag else None

        # Category
        cat_links = article.select("header.entry-header .cat-links a")
        item['categories'] = [cat.get_text(strip=True) for cat in cat_links] if cat_links else []

        return item

    def get_next_page(self, soup):
        """Extract the URL of the next page."""
        nav_previous = soup.find("div", class_="nav-previous")
        if nav_previous:
            a_tag = nav_previous.find("a")
            if a_tag:
                return a_tag.get('href')

        for a in soup.find_all("a", href=True):
            if "older posts" in a.get_text(strip=True).lower():
                return a['href']

        return None

    def run(self):
        """Run the scraper."""
        url = self.base_url
        new_items_count = 0

        try:
            while url:
                content = self.fetch_page(url)
                if not content:
                    break

                soup = BeautifulSoup(content, "html.parser")
                articles = soup.find_all("article")
                logger.info("Found %d articles on this page.", len(articles))

                if not articles:
                    logger.warning("No articles found on page.")

                for article in articles:
                    item = self.parse_article(article)
                    self.data.append(item)
                    if self.save_to_db(item):
                        new_items_count += 1

                next_page = self.get_next_page(soup)
                if next_page:
                    logger.info("Found next page: %s", next_page)
                    url = next_page
                    time.sleep(1)
                else:
                    logger.info("No more pages found.")
                    url = None
        finally:
            self.save_json()

        logger.info("Scraped %d articles in total.", len(self.data))
        logger.info("New items added to database: %d", new_items_count)

    def save_json(self):
        """Save collected data to JSON file."""
        try:
            with open(self.output_json, "w", encoding="utf-8") as f:
                json.dump(self.data, f, indent=2, ensure_ascii=False)
            logger.info("Data saved to %s", self.output_json)
        except IOError as e:
            logger.error("Error saving data to %s: %s", self.output_json, e)

def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Scrape wishlist.design.blog")
    parser.add_argument("--url", default="https://wishlist.design.blog", help="Base URL to scrape")
    parser.add_argument("--json", default="wishlist_data.json", help="Output JSON file")
    parser.add_argument("--db", default="wishlist_data.db", help="Output SQLite DB file")

    args = parser.parse_args()

    # Use context manager to ensure resources are closed
    with BlogScraper(args.url, args.json, args.db) as scraper:
        scraper.run()

if __name__ == "__main__":
    main()
