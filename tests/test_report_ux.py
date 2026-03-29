import unittest
import os
import sqlite3
from datetime import datetime, timedelta
from report_generator import ReportGenerator

class TestReportUX(unittest.TestCase):
    def setUp(self):
        self.db_name = "test_ux.db"
        self.report_dir = "test_reports_ux"

        # Cleanup
        if os.path.exists(self.db_name):
            os.remove(self.db_name)
        if not os.path.exists(self.report_dir):
            os.makedirs(self.report_dir)

        # Setup DB
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE posts (id INTEGER PRIMARY KEY, title TEXT, post_url TEXT, scraped_at TIMESTAMP)")
        self.cursor.execute("CREATE TABLE changes (id INTEGER PRIMARY KEY, post_id INTEGER, field TEXT, old_value TEXT, new_value TEXT, changed_at TIMESTAMP)")
        self.cursor.execute("CREATE TABLE rankings (id INTEGER PRIMARY KEY, query TEXT, rank INTEGER, title TEXT, url TEXT, checked_at TIMESTAMP)")
        self.conn.commit()

    def tearDown(self):
        self.conn.close()
        if os.path.exists(self.db_name):
            os.remove(self.db_name)
        # Clean reports
        if os.path.exists(self.report_dir):
            for f in os.listdir(self.report_dir):
                os.remove(os.path.join(self.report_dir, f))
            os.rmdir(self.report_dir)

    def test_report_structure_full(self):
        # Insert data to trigger all sections
        now = datetime.now()
        yesterday = now - timedelta(days=1)
        two_days_ago = now - timedelta(days=2)

        # New Post (recent scraped_at)
        self.cursor.execute("INSERT INTO posts (title, post_url, scraped_at) VALUES (?, ?, ?)", ("New Post", "http://example.com/new", now))

        # Updated Post (recent changed_at)
        # Note: Scraped at 2 days ago so it's not "new", but has a change "now"
        self.cursor.execute("INSERT INTO posts (title, post_url, scraped_at) VALUES (?, ?, ?)", ("Updated Post", "http://example.com/updated", two_days_ago))
        post_id = self.cursor.lastrowid
        self.cursor.execute("INSERT INTO changes (post_id, field, old_value, new_value, changed_at) VALUES (?, ?, ?, ?, ?)", (post_id, "title", "Old Title", "Updated Post", now))

        # SEO Ranking (recent checked_at)
        self.cursor.execute("INSERT INTO rankings (query, rank, title, url, checked_at) VALUES (?, ?, ?, ?, ?)", ("query", 1, "Updated Post", "http://example.com/updated", now))
        self.conn.commit()

        # Generate
        generator = ReportGenerator(db_name=self.db_name, report_dir=self.report_dir)
        generator.generate_daily_report()

        # Find report
        report_files = os.listdir(self.report_dir)
        self.assertTrue(len(report_files) > 0)
        report_path = os.path.join(self.report_dir, report_files[0])

        with open(report_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for UX Enhancements

        # 1. Top Anchor
        self.assertIn("<a name='top'></a>", content, "Missing Top anchor")

        # 2. Table of Contents
        self.assertIn("## 📋 Table of Contents", content, "Missing ToC header")
        self.assertIn("[💡 Recommendations](#recommendations)", content)
        self.assertIn("[🧠 Keyword Trends](#keywords)", content)
        self.assertIn("[📈 SEO Trend Analysis](#seo)", content)
        self.assertIn("[🔄 Content Updates](#updates)", content)
        self.assertIn("[🆕 Recently Scraped Posts](#new-posts)", content)

        # 3. Section Anchors
        self.assertIn("<a name='recommendations'></a>", content)
        self.assertIn("<a name='keywords'></a>", content)
        self.assertIn("<a name='seo'></a>", content)
        self.assertIn("<a name='updates'></a>", content)
        self.assertIn("<a name='new-posts'></a>", content)

        # 4. Back to Top
        self.assertIn("[⬆️ Back to Top](#top)", content)

if __name__ == '__main__':
    unittest.main()
