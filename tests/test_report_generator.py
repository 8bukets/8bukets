import unittest
import sqlite3
import os
import shutil
import sys
from datetime import datetime, timedelta

# Add root directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from report_generator import ReportGenerator

class TestReportGenerator(unittest.TestCase):
    def setUp(self):
        self.test_dir = "test_reports"
        self.db_name = "test_wishlist_report.db"
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
        if os.path.exists(self.db_name):
            os.remove(self.db_name)

        # Setup DB
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
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
        self.cursor.execute('''
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
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS rankings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                query TEXT,
                rank INTEGER,
                title TEXT,
                url TEXT,
                checked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()

        self.generator = ReportGenerator(self.db_name, self.test_dir)

    def tearDown(self):
        self.conn.close()
        if os.path.exists(self.db_name):
            os.remove(self.db_name)
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_generate_report_no_data(self):
        self.generator.generate_daily_report()
        files = os.listdir(self.test_dir)
        self.assertEqual(len(files), 1)
        with open(os.path.join(self.test_dir, files[0]), 'r', encoding='utf-8') as f:
            content = f.read()
            self.assertIn("# Daily Scraper Report", content)
            self.assertIn("Total Posts:** 0", content)

            # Check TOC
            self.assertIn("## 📋 Table of Contents", content)
            self.assertIn("[💡 Recommendations](#recommendations)", content)
            self.assertIn("[📈 SEO Trend Analysis](#seo-trend-analysis)", content)
            # Conditional TOC should be missing
            self.assertNotIn("[🧠 Keyword Trends]", content)
            self.assertNotIn("[🆕 Recently Scraped Posts]", content)

            # Check Anchors
            self.assertIn("<a name='recommendations'></a>", content)

            # Default headers
            self.assertIn("## 💡 Recommendations", content)
            self.assertIn("## 📈 SEO Trend Analysis", content)

            # Conditional headers should be missing
            self.assertNotIn("## 🧠 Keyword Trends", content)
            self.assertNotIn("## 🔄 Content Updates", content)
            self.assertNotIn("## 🆕 Recently Scraped Posts", content)

            # Footer
            self.assertIn("Generated with ❤️ by Palette", content)

    def test_generate_report_with_data(self):
        # Insert data
        now = datetime.now()
        self.cursor.execute("INSERT INTO posts (title, post_url, scraped_at) VALUES (?, ?, ?)",
                            ("Test Post", "http://test.com", now))
        self.conn.commit()

        self.generator.generate_daily_report()
        files = os.listdir(self.test_dir)
        self.assertEqual(len(files), 1)
        with open(os.path.join(self.test_dir, files[0]), 'r', encoding='utf-8') as f:
            content = f.read()
            self.assertIn("Total Posts:** 1", content)

            # Check TOC
            self.assertIn("[🆕 Recently Scraped Posts](#recently-scraped-posts)", content)
            self.assertIn("[🧠 Keyword Trends](#keyword-trends)", content)

            # Check Headers & Anchors
            self.assertIn("<a name='recently-scraped-posts'></a>", content)
            self.assertIn("## 🆕 Recently Scraped Posts", content)
            self.assertIn("Test Post", content)

            # Footer
            self.assertIn("Generated with ❤️ by Palette", content)

if __name__ == '__main__':
    unittest.main()
