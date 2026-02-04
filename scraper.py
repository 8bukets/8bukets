import requests
from bs4 import BeautifulSoup
import json
import time
import logging
import argparse
import sys
import sqlite3
from datetime import datetime

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
    def __init__(self, base_url, output_json="wishlist_data.json", db_name="wishlist_data.db"):
        self.base_url = base_url
        self.output_json = output_json
        self.db_name = db_name
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.data = []
        self.conn = None
        self.init_db()

    def init_db(self):
        """Initialize the SQLite database."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
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
                conn.commit()
        except sqlite3.Error as e:
            logger.error(f"Database initialization error: {e}")

    def save_to_db(self, item):
        """Save a single item to the database, handling updates."""
        close_conn = False
        if self.conn:
            conn = self.conn
        else:
            conn = sqlite3.connect(self.db_name)
            close_conn = True

        try:
            cursor = conn.cursor()

            # Check if post exists
            cursor.execute("SELECT id, title, external_link FROM posts WHERE post_url = ?", (item.get('post_url'),))
            existing_post = cursor.fetchone()

            if existing_post:
                post_id, old_title, old_link = existing_post
                updated = False

                # Check Title Change
                new_title = item.get('title')
                if old_title != new_title and new_title:
                    logger.info(f"Change detected for {item.get('post_url')}: Title changed.")
                    cursor.execute("INSERT INTO changes (post_id, field, old_value, new_value) VALUES (?, ?, ?, ?)",
                                   (post_id, 'title', old_title, new_title))
                    cursor.execute("UPDATE posts SET title = ? WHERE id = ?", (new_title, post_id))
                    updated = True

                # Check External Link Change
                new_link = item.get('external_link')
                if old_link != new_link and new_link:
                    logger.info(f"Change detected for {item.get('post_url')}: External Link changed.")
                    cursor.execute("INSERT INTO changes (post_id, field, old_value, new_value) VALUES (?, ?, ?, ?)",
                                   (post_id, 'external_link', old_link, new_link))
                    cursor.execute("UPDATE posts SET external_link = ? WHERE id = ?", (new_link, post_id))
                    updated = True

                if updated:
                    # Update scraped_at to reflect latest check
                    cursor.execute("UPDATE posts SET scraped_at = CURRENT_TIMESTAMP WHERE id = ?", (post_id,))
                    conn.commit()
                    return False # Not a "new" post, but an updated one

            else:
                # Insert new post
                cursor.execute('''
                    INSERT INTO posts (title, post_url, external_link, date_str, datetime_iso, author, categories)
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
                conn.commit()
                return True # New post

        except sqlite3.Error as e:
            logger.error(f"Database insertion/update error: {e}")
            conn.rollback()
            return False
        finally:
            if close_conn:
                conn.close()

        return False

    def fetch_page(self, url):
        logger.info(f"Fetching {url}...")
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.content
        except requests.RequestException as e:
            logger.error(f"Error fetching URL {url}: {e}")
            return None

    def parse_article(self, article):
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
        url = self.base_url
        new_items_count = 0

        # Performance optimization: Reuse DB connection
        self.conn = sqlite3.connect(self.db_name)

        try:
            while url:
                content = self.fetch_page(url)
                if not content:
                    break

                soup = BeautifulSoup(content, "html.parser")
                articles = soup.find_all("article")
                logger.info(f"Found {len(articles)} articles on this page.")

                if not articles:
                    logger.warning("No articles found on page.")

                for article in articles:
                    item = self.parse_article(article)
                    self.data.append(item)
                    if self.save_to_db(item):
                        new_items_count += 1

                next_page = self.get_next_page(soup)
                if next_page:
                    logger.info(f"Found next page: {next_page}")
                    url = next_page
                    time.sleep(1)
                else:
                    logger.info("No more pages found.")
                    url = None
        finally:
            if self.conn:
                self.conn.close()
                self.conn = None

        self.save_json()
        logger.info(f"Scraped {len(self.data)} articles in total.")
        logger.info(f"New items added to database: {new_items_count}")

    def save_json(self):
        try:
            with open(self.output_json, "w", encoding="utf-8") as f:
                json.dump(self.data, f, indent=2, ensure_ascii=False)
            logger.info(f"Data saved to {self.output_json}")
        except IOError as e:
            logger.error(f"Error saving data to {self.output_json}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Scrape wishlist.design.blog")
    parser.add_argument("--url", default="https://wishlist.design.blog", help="Base URL to scrape")
    parser.add_argument("--json", default="wishlist_data.json", help="Output JSON file")
    parser.add_argument("--db", default="wishlist_data.db", help="Output SQLite DB file")

    args = parser.parse_args()

    scraper = BlogScraper(args.url, args.json, args.db)
    scraper.run()

if __name__ == "__main__":
    main()
