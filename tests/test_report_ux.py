import sqlite3
import os
import unittest
import shutil
from datetime import datetime, timedelta
from report_generator import ReportGenerator

class TestReportUX(unittest.TestCase):
    def setUp(self):
        self.db_name = "test_ux_data.db"
        self.report_dir = "test_reports"
        if not os.path.exists(self.report_dir):
            os.makedirs(self.report_dir)

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

        # Insert dummy data
        today = datetime.now()
        yesterday = today - timedelta(days=0.5) # within 24h

        self.cursor.execute('''
            INSERT INTO posts (title, post_url, scraped_at)
            VALUES ('UX Improvement Guide', 'http://example.com/ux-guide', ?)
        ''', (today,))

        self.cursor.execute('''
            INSERT INTO posts (title, post_url, scraped_at)
            VALUES ('Accessibility 101', 'http://example.com/a11y', ?)
        ''', (today,))

        self.conn.commit()

    def tearDown(self):
        self.conn.close()
        # Clean up files
        if os.path.exists(self.db_name):
            os.remove(self.db_name)
        if os.path.exists(self.report_dir):
             shutil.rmtree(self.report_dir)

    def test_report_generation_ux(self):
        generator = ReportGenerator(db_name=self.db_name, report_dir=self.report_dir)
        generator.generate_daily_report()

        report_date = datetime.now().strftime("%Y-%m-%d")
        report_path = os.path.join(self.report_dir, f"report_{report_date}.md")

        self.assertTrue(os.path.exists(report_path))

        with open(report_path, 'r', encoding='utf-8') as f:
            content = f.read()

        print("\n--- Generated Report Content Start ---")
        print(content)
        print("--- Generated Report Content End ---\n")

        # Check for UX improvements

        # 1. Check for Table of Contents with new anchors
        has_toc = "## 📑 Table of Contents" in content
        self.assertTrue(has_toc, "Table of Contents missing")
        self.assertIn("- [💡 Recommendations](#recommendations)", content)
        self.assertIn("- [🆕 Recently Scraped Posts](#recently-scraped-posts)", content)

        # Check for anchors in headers
        self.assertIn('## <a name="recommendations"></a>💡 Recommendations', content)
        self.assertIn('## <a name="recently-scraped-posts"></a>🆕 Recently Scraped Posts', content)

        # 2. Check for Linked Title
        has_linked_title = "[UX Improvement Guide](http://example.com/ux-guide)" in content
        self.assertTrue(has_linked_title, "Titles should be linked directly")

        # 3. Check for Summary Table
        has_summary_table = "## 📊 Summary" in content and "| Metric | Count |" in content
        self.assertTrue(has_summary_table, "Summary table missing")

if __name__ == "__main__":
    unittest.main()
