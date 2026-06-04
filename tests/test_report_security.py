import unittest
import os
import sqlite3
from report_generator import ReportGenerator
from datetime import datetime

class TestReportSecurity(unittest.TestCase):
    def setUp(self):
        self.db_name = "test_security.db"
        self.report_dir = "test_reports"
        if not os.path.exists(self.report_dir):
            os.makedirs(self.report_dir)

        self.generator = ReportGenerator(self.db_name, self.report_dir)

        # Init DB
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
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
            # Changes table is also needed for the query to work
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
             # Rankings table needed
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

    def tearDown(self):
        if os.path.exists(self.db_name):
            os.remove(self.db_name)
        # Clean up reports
        if os.path.exists(self.report_dir):
            for f in os.listdir(self.report_dir):
                os.remove(os.path.join(self.report_dir, f))
            os.rmdir(self.report_dir)

    def test_markdown_injection(self):
        # Insert malicious post
        malicious_title = "Safe | Title [Link](javascript:alert(1))"
        malicious_url = "javascript:alert('XSS')"

        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO posts (title, post_url, scraped_at)
                VALUES (?, ?, ?)
            ''', (malicious_title, malicious_url, datetime.now()))
            conn.commit()

        self.generator.generate_daily_report()

        # Check report content
        report_files = os.listdir(self.report_dir)
        self.assertTrue(len(report_files) > 0)

        with open(os.path.join(self.report_dir, report_files[0]), 'r') as f:
            content = f.read()

        # Verify Fix:

        # 1. The title injection should be escaped.
        # [Link] -> \[Link\]
        self.assertIn(r"\[Link\]", content)

        # 2. The URL injection should be neutralized.
        # It should show "(Unsafe Link)" instead of [View](javascript...)
        self.assertIn("(Unsafe Link)", content)
        self.assertNotIn(f"({malicious_url})", content)

if __name__ == '__main__':
    unittest.main()
