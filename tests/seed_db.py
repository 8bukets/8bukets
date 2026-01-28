import sqlite3
import os
from datetime import datetime, timedelta

DB_NAME = "wishlist_data.db"

def init_db():
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        # Posts schema (from scraper.py)
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

        # Changes schema (from scraper.py)
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

        # Rankings schema (from google_checker.py)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS rankings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                query TEXT,
                rank INTEGER,
                title TEXT,
                url TEXT,
                checked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()

def seed_data():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        now = datetime.now()
        yesterday = now - timedelta(days=1)
        two_days_ago = now - timedelta(days=2)

        # 1. Old Posts (Stable)
        cursor.execute('''
            INSERT INTO posts (title, post_url, external_link, date_str, datetime_iso, scraped_at)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', ("Old Post 1", "http://example.com/1", "http://ext.com/1", "2023-01-01", "2023-01-01T00:00:00", two_days_ago))

        cursor.execute('''
            INSERT INTO posts (title, post_url, external_link, date_str, datetime_iso, scraped_at)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', ("Old Post 2", "http://example.com/2", "http://ext.com/2", "2023-01-02", "2023-01-02T00:00:00", two_days_ago))
        old_post_id = cursor.lastrowid

        # 2. New Posts (Scraped today) -> Triggers "New Posts" and "Keyword Trends"
        cursor.execute('''
            INSERT INTO posts (title, post_url, external_link, date_str, datetime_iso, scraped_at)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', ("New Design Trends 2024", "http://example.com/new1", "http://ext.com/new1", "2024-05-20", "2024-05-20T00:00:00", now))

        cursor.execute('''
            INSERT INTO posts (title, post_url, external_link, date_str, datetime_iso, scraped_at)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', ("Minimalist Design Principles", "http://example.com/new2", "http://ext.com/new2", "2024-05-21", "2024-05-21T00:00:00", now))

        # 3. Updated Posts -> Triggers "Content Updates"
        # We need an old post that has a change entry from today
        cursor.execute('''
            INSERT INTO changes (post_id, field, old_value, new_value, changed_at)
            VALUES (?, ?, ?, ?, ?)
        ''', (old_post_id, "title", "Old Post 2", "Updated Post 2 (Renamed)", now))

        # 4. SEO Rankings -> Triggers "SEO Trends"
        # Yesterday's rank
        cursor.execute('''
            INSERT INTO rankings (query, rank, title, url, checked_at)
            VALUES (?, ?, ?, ?, ?)
        ''', ("site:wishlist.design.blog", 5, "Wishlist Design", "http://wishlist.design.blog", two_days_ago))

        # Today's rank (Improved)
        cursor.execute('''
            INSERT INTO rankings (query, rank, title, url, checked_at)
            VALUES (?, ?, ?, ?, ?)
        ''', ("site:wishlist.design.blog", 3, "Wishlist Design", "http://wishlist.design.blog", now))

        # Another rank (Dropped)
        cursor.execute('''
            INSERT INTO rankings (query, rank, title, url, checked_at)
            VALUES (?, ?, ?, ?, ?)
        ''', ("design blog", 10, "Wishlist Design", "http://wishlist.design.blog", two_days_ago))

        cursor.execute('''
            INSERT INTO rankings (query, rank, title, url, checked_at)
            VALUES (?, ?, ?, ?, ?)
        ''', ("design blog", 12, "Wishlist Design", "http://wishlist.design.blog", now))

        conn.commit()
        print("Database seeded successfully.")

if __name__ == "__main__":
    init_db()
    seed_data()
