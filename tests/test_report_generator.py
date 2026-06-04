import unittest
import os
import sqlite3
import datetime
import shutil
from report_generator import ReportGenerator

class TestReportGenerator(unittest.TestCase):
    def setUp(self):
        self.db_name = "test_report_db.db"
        self.report_dir = "test_reports"

        # Ensure clean state
        if os.path.exists(self.db_name):
            os.remove(self.db_name)
        if os.path.exists(self.report_dir):
            shutil.rmtree(self.report_dir)

        self.init_db()
        self.populate_db()

        self.generator = ReportGenerator(db_name=self.db_name, report_dir=self.report_dir)

    def tearDown(self):
        if os.path.exists(self.db_name):
            os.remove(self.db_name)
        if os.path.exists(self.report_dir):
            shutil.rmtree(self.report_dir)

    def init_db(self):
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

    def populate_db(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            recent = datetime.datetime.now()

            # Insert posts
            posts = [
                ("Design Trends", "http://example.com/1", "http://ext.com/1", "2023-10-26", recent.isoformat(), "Author", '["Design"]', recent),
                ("Design Ideas", "http://example.com/2", "http://ext.com/2", "2023-10-26", recent.isoformat(), "Author", '["Ideas"]', recent),
            ]
            for p in posts:
                cursor.execute('''
                    INSERT INTO posts (title, post_url, external_link, date_str, datetime_iso, author, categories, scraped_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', p)
            conn.commit()

    def test_create_ascii_bar(self):
        bar = self.generator.create_ascii_bar(5, 10, width=10)
        self.assertEqual(bar, "█████░░░░░")

        bar = self.generator.create_ascii_bar(10, 10, width=10)
        self.assertEqual(bar, "██████████")

        bar = self.generator.create_ascii_bar(0, 10, width=10)
        self.assertEqual(bar, "░░░░░░░░░░")

    def test_report_generation(self):
        self.generator.generate_daily_report()

        if not os.path.exists(self.report_dir):
             self.fail("Report directory was not created")

        report_files = os.listdir(self.report_dir)
        self.assertTrue(len(report_files) > 0)

        with open(os.path.join(self.report_dir, report_files[0]), 'r') as f:
            content = f.read()

        self.assertIn("## 🧠 Keyword Trends", content)
        self.assertIn("Distribution", content)
        self.assertIn("██", content) # Check for block character

if __name__ == '__main__':
    unittest.main()
