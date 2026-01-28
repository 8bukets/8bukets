import unittest
import os
import shutil
import sqlite3
from datetime import datetime
from report_generator import ReportGenerator

class TestReportUX(unittest.TestCase):
    def setUp(self):
        self.test_dir = "test_reports"
        self.db_name = "test_wishlist.db"
        if not os.path.exists(self.test_dir):
            os.makedirs(self.test_dir)

        # Setup DB
        self.init_db()
        self.seed_data()

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
        if os.path.exists(self.db_name):
            os.remove(self.db_name)

    def init_db(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY, title TEXT, post_url TEXT, external_link TEXT, scraped_at TIMESTAMP)')
            cursor.execute('CREATE TABLE IF NOT EXISTS changes (id INTEGER PRIMARY KEY, post_id INTEGER, field TEXT, old_value TEXT, new_value TEXT, changed_at TIMESTAMP)')
            cursor.execute('CREATE TABLE IF NOT EXISTS rankings (id INTEGER PRIMARY KEY, query TEXT, rank INTEGER, title TEXT, url TEXT, checked_at TIMESTAMP)')
            conn.commit()

    def seed_data(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            now = datetime.now()

            # New Post
            cursor.execute('INSERT INTO posts (title, post_url, scraped_at) VALUES (?, ?, ?)',
                           ("Test Post", "http://example.com", now))

            # Ranking
            cursor.execute('INSERT INTO rankings (query, rank, title, url, checked_at) VALUES (?, ?, ?, ?, ?)',
                           ("test query", 1, "Test", "http://example.com", now))

            conn.commit()

    def test_report_structure(self):
        generator = ReportGenerator(db_name=self.db_name, report_dir=self.test_dir)
        generator.generate_daily_report()

        report_date = datetime.now().strftime("%Y-%m-%d")
        report_path = os.path.join(self.test_dir, f"report_{report_date}.md")

        self.assertTrue(os.path.exists(report_path), "Report file should exist")

        with open(report_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Check for UX elements
        self.assertIn("<a name='table-of-contents'></a>", content)
        self.assertIn("## 📑 Table of Contents", content)
        self.assertIn("[💡 Recommendations](#recommendations)", content)
        self.assertIn("[Back to Top](#table-of-contents)", content)
        self.assertIn("<a name='recommendations'></a>", content)
        self.assertIn("<a name='recently-scraped-posts'></a>", content)

if __name__ == '__main__':
    unittest.main()
