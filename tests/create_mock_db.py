import sqlite3
import os
from datetime import datetime, timedelta

def create_mock_db(db_name="wishlist_data.db"):
    if os.path.exists(db_name):
        os.remove(db_name)

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create tables
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

    # Rankings table (inferred from report_generator.py queries)
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

    # Insert Posts
    # 1. Old post
    cursor.execute('''
        INSERT INTO posts (title, post_url, external_link, scraped_at)
        VALUES (?, ?, ?, ?)
    ''', ("Old Post", "http://example.com/old", "http://ext.com/old", (datetime.now() - timedelta(days=5)).isoformat()))

    # 2. New post (today)
    cursor.execute('''
        INSERT INTO posts (title, post_url, external_link, scraped_at)
        VALUES (?, ?, ?, ?)
    ''', ("New Design Trend: Minimalist", "http://example.com/new1", "http://ext.com/new1", datetime.now().isoformat()))

    # 3. Another New post (today)
    cursor.execute('''
        INSERT INTO posts (title, post_url, external_link, scraped_at)
        VALUES (?, ?, ?, ?)
    ''', ("Top 10 Color Palettes 2025", "http://example.com/new2", "http://ext.com/new2", datetime.now().isoformat()))

    # Insert Changes
    # Update for Old Post
    cursor.execute('''
        INSERT INTO changes (post_id, field, old_value, new_value, changed_at)
        VALUES (?, ?, ?, ?, ?)
    ''', (1, "title", "Old Post Title", "Old Post Updated", datetime.now().isoformat()))

    # Insert Rankings
    # Current rankings
    cursor.execute('''
        INSERT INTO rankings (query, rank, title, url, checked_at)
        VALUES (?, ?, ?, ?, ?)
    ''', ("design trends", 5, "Design Trends", "http://example.com", datetime.now().isoformat()))

    cursor.execute('''
        INSERT INTO rankings (query, rank, title, url, checked_at)
        VALUES (?, ?, ?, ?, ?)
    ''', ("minimalist web", 12, "Minimalist Web", "http://example.com/min", datetime.now().isoformat()))

    # Past rankings (for trend comparison)
    cursor.execute('''
        INSERT INTO rankings (query, rank, title, url, checked_at)
        VALUES (?, ?, ?, ?, ?)
    ''', ("design trends", 8, "Design Trends", "http://example.com", (datetime.now() - timedelta(days=2)).isoformat()))

    conn.commit()
    conn.close()
    print(f"Created mock DB: {db_name}")

if __name__ == "__main__":
    create_mock_db()
