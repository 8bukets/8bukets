import unittest
import os
import sqlite3
from report_generator import ReportGenerator
from datetime import datetime

class TestReportGeneratorSecurity(unittest.TestCase):
    def setUp(self):
        self.test_db = "test_security.db"
        self.report_dir = "test_reports"

        # Setup clean environment
        if os.path.exists(self.test_db):
            os.remove(self.test_db)
        if not os.path.exists(self.report_dir):
            os.makedirs(self.report_dir)

        # Create DB with schema
        with sqlite3.connect(self.test_db) as conn:
            cursor = conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY, title TEXT, post_url TEXT, external_link TEXT, date_str TEXT, datetime_iso TEXT, author TEXT, categories TEXT, scraped_at TIMESTAMP)')
            cursor.execute('CREATE TABLE IF NOT EXISTS changes (id INTEGER PRIMARY KEY, post_id INTEGER, field TEXT, old_value TEXT, new_value TEXT, changed_at TIMESTAMP)')
            cursor.execute('CREATE TABLE IF NOT EXISTS rankings (id INTEGER PRIMARY KEY, query TEXT, rank INTEGER, title TEXT, url TEXT, checked_at TIMESTAMP)')
            conn.commit()

        self.reporter = ReportGenerator(db_name=self.test_db, report_dir=self.report_dir)

    def tearDown(self):
        if os.path.exists(self.test_db):
            os.remove(self.test_db)
        # Clean up reports
        for f in os.listdir(self.report_dir):
            os.remove(os.path.join(self.report_dir, f))
        os.rmdir(self.report_dir)

    def test_sanitize_markdown_cell(self):
        """Test that pipes and newlines are escaped."""
        raw = "Hello | World"
        sanitized = self.reporter.sanitize_markdown_cell(raw)
        self.assertEqual(sanitized, "Hello &#124; World")

        raw_newline = "Line1\nLine2"
        sanitized_newline = self.reporter.sanitize_markdown_cell(raw_newline)
        self.assertEqual(sanitized_newline, "Line1 Line2")

        self.assertEqual(self.reporter.sanitize_markdown_cell(None), "")

    def test_sanitize_url(self):
        """Test that malicious URLs are blocked."""
        safe_url = "https://example.com"
        self.assertEqual(self.reporter.sanitize_url(safe_url), "https://example.com")

        malicious_url = "javascript:alert(1)"
        self.assertEqual(self.reporter.sanitize_url(malicious_url), "#invalid-url-blocked")

        malicious_url_case = "JavaSCRIPT:alert(1)"
        self.assertEqual(self.reporter.sanitize_url(malicious_url_case), "#invalid-url-blocked")

        whitespace_url = "  javascript:alert(1)  "
        self.assertEqual(self.reporter.sanitize_url(whitespace_url), "#invalid-url-blocked")

    def test_report_generation_security(self):
        """Test that the generated report contains sanitized output."""
        with sqlite3.connect(self.test_db) as conn:
            cursor = conn.cursor()
            # Insert malicious post
            cursor.execute('''
                INSERT INTO posts (title, post_url, scraped_at)
                VALUES (?, ?, ?)
            ''', ("Malicious Title | Pipe", "javascript:alert(1)", datetime.now()))

            # Insert malicious change
            cursor.execute('''
                INSERT INTO changes (post_id, field, old_value, new_value, changed_at)
                VALUES (?, ?, ?, ?, ?)
            ''', (1, "title", "Old | Value", "New | Value", datetime.now()))
            conn.commit()

        self.reporter.generate_daily_report()

        report_files = os.listdir(self.report_dir)
        self.assertTrue(len(report_files) > 0)

        with open(os.path.join(self.report_dir, report_files[0]), "r") as f:
            content = f.read()

        # Verify sanitization
        self.assertNotIn("javascript:alert(1)", content)
        self.assertIn("#invalid-url-blocked", content)
        self.assertIn("Malicious Title &#124; Pipe", content)
        self.assertIn("Old &#124; Value", content)
        self.assertIn("New &#124; Value", content)

if __name__ == '__main__':
    unittest.main()
