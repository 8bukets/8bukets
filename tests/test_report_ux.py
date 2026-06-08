import unittest
import os
import sqlite3
import shutil
from datetime import datetime, timedelta
from report_generator import ReportGenerator

class TestReportUX(unittest.TestCase):
    def setUp(self):
        self.db_name = "test_ux.db"
        self.report_dir = "test_reports"
        if os.path.exists(self.report_dir):
            shutil.rmtree(self.report_dir)

        # Initialize DB
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

            # Changes table
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

            # Rankings table
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

            # Insert Dummy Data for Report sections

            # 1. New Post (scraped recently)
            cursor.execute('''
                INSERT INTO posts (title, post_url, scraped_at)
                VALUES (?, ?, datetime('now'))
            ''', ("New UX Post", "http://example.com/new"))

            # 2. Updated Post
            cursor.execute('''
                INSERT INTO posts (title, post_url, scraped_at)
                VALUES (?, ?, datetime('now', '-2 days'))
            ''', ("Old Post", "http://example.com/old"))
            post_id = cursor.lastrowid

            cursor.execute('''
                INSERT INTO changes (post_id, field, old_value, new_value, changed_at)
                VALUES (?, 'title', 'Old Title', 'New Title', datetime('now'))
            ''', (post_id,))

            # 3. Rankings
            cursor.execute('''
                INSERT INTO rankings (query, rank, title, url, checked_at)
                VALUES (?, 1, 'Top Rank', 'http://example.com', datetime('now'))
            ''', ("ux design",))

            conn.commit()

    def tearDown(self):
        if os.path.exists(self.db_name):
            os.remove(self.db_name)
        if os.path.exists(self.report_dir):
            shutil.rmtree(self.report_dir)

    def test_report_has_ux_features(self):
        generator = ReportGenerator(db_name=self.db_name, report_dir=self.report_dir)
        generator.generate_daily_report()

        # Find the generated file
        files = os.listdir(self.report_dir)
        self.assertTrue(len(files) > 0, "No report generated")
        report_path = os.path.join(self.report_dir, files[0])

        with open(report_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for Table of Contents
        self.assertIn("## 📋 Table of Contents", content, "TOC header missing")
        self.assertIn("[💡 Recommendations](#recommendations)", content, "TOC link missing")

        # Check for Anchors
        self.assertIn("<a id='recommendations'></a>", content, "Anchor tag for recommendations missing")
        self.assertIn("<a id='recently-scraped-posts'></a>", content, "Anchor tag for new posts missing")

        # Check for Back to Top
        self.assertIn("[⬆️ Back to Top](#table-of-contents)", content, "Back to Top link missing")

if __name__ == '__main__':
    unittest.main()
