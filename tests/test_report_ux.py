import unittest
import sqlite3
import os
import sys
from datetime import datetime, timedelta

# Add root directory to path to import report_generator
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from report_generator import ReportGenerator

class TestReportUX(unittest.TestCase):
    def setUp(self):
        self.db_name = "test_ux.db"
        self.report_dir = "test_reports"
        if not os.path.exists(self.report_dir):
            os.makedirs(self.report_dir)

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

            # Insert Data
            yesterday = (datetime.now() - timedelta(hours=12)).strftime("%Y-%m-%d %H:%M:%S")

            # 1. New Post
            cursor.execute('''
                INSERT INTO posts (title, post_url, scraped_at)
                VALUES (?, ?, ?)
            ''', ("New UX Post", "http://example.com/new", yesterday))

            # 2. Updated Post
            cursor.execute('''
                INSERT INTO posts (title, post_url, scraped_at)
                VALUES (?, ?, ?)
            ''', ("Old UX Post", "http://example.com/old", "2020-01-01 00:00:00"))
            post_id = cursor.lastrowid

            cursor.execute('''
                INSERT INTO changes (post_id, field, old_value, new_value, changed_at)
                VALUES (?, ?, ?, ?, ?)
            ''', (post_id, "title", "Old Title", "Old UX Post", yesterday))

            # 3. Rankings
            cursor.execute('''
                INSERT INTO rankings (query, rank, title, url, checked_at)
                VALUES (?, ?, ?, ?, ?)
            ''', ("ux design", 1, "Wishlist UX", "http://wishlist.design.blog", yesterday))

            conn.commit()

        self.reporter = ReportGenerator(db_name=self.db_name, report_dir=self.report_dir)

    def tearDown(self):
        # Cleanup
        if os.path.exists(self.db_name):
            os.remove(self.db_name)

        # Remove generated reports
        if os.path.exists(self.report_dir):
            for f in os.listdir(self.report_dir):
                os.remove(os.path.join(self.report_dir, f))
            os.rmdir(self.report_dir)

    def test_report_structure(self):
        self.reporter.generate_daily_report()

        report_date = datetime.now().strftime("%Y-%m-%d")
        report_file = os.path.join(self.report_dir, f"report_{report_date}.md")

        self.assertTrue(os.path.exists(report_file), "Report file was not created")

        with open(report_file, "r") as f:
            content = f.read()

        # Check for Table of Contents
        self.assertIn("# Table of Contents", content, "TOC header missing")
        self.assertIn("[💡 Recommendations](#recommendations)", content, "TOC link to Recommendations missing")
        self.assertIn('<a name="table-of-contents"></a>', content, "HTML anchor for TOC missing")

        # Check for Anchors
        self.assertIn('<a name="recommendations"></a>', content, "HTML anchor for Recommendations missing")

        # Check for Back to Top
        self.assertIn("[Back to Top](#table-of-contents)", content, "Back to Top link missing")

        # Verify specific sections exist
        self.assertIn("## 🆕 Recently Scraped Posts", content)
        self.assertIn('<a name="recently-scraped-posts"></a>', content)

        self.assertIn("## 🔄 Content Updates", content)
        self.assertIn('<a name="content-updates"></a>', content)
