import unittest
from unittest.mock import MagicMock, patch
import os
import shutil
from report_generator import ReportGenerator

class TestReportGenerator(unittest.TestCase):
    def setUp(self):
        self.report_dir = "test_reports"
        self.db_name = "test_wishlist.db"
        if not os.path.exists(self.report_dir):
            os.makedirs(self.report_dir)
        self.generator = ReportGenerator(self.db_name, self.report_dir)

    def tearDown(self):
        if os.path.exists(self.report_dir):
            shutil.rmtree(self.report_dir)

    @patch('sqlite3.connect')
    def test_generate_daily_report_vulnerability(self, mock_connect):
        # Mock database connection and cursor
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Mock data
        # 1. Total posts
        total_posts = 10

        # 2. New posts (title with script tag)
        new_posts = [
            ("Malicious <script>alert('xss')</script>", "http://example.com/bad", "2023-01-01 12:00:00")
        ]

        # 3. Updated posts (values with pipes)
        updated_posts = [
            ("Safe Title", "http://example.com/safe", "status", "old | val", "new | val", "2023-01-01 12:00:00")
        ]

        # 4. Rankings
        rankings = [
             ("query | injection", 1, "Title", "http://url", "2023-01-01")
        ]

        # 5. Past rankings
        past_rankings = []

        # Configure cursor side effects for sequential calls
        # Sequence of execute calls in generate_daily_report:
        # 1. COUNT(*)
        # 2. New posts
        # 3. Updated posts
        # 4. Latest SEO rankings
        # 5. Previous SEO rankings

        mock_cursor.fetchone.side_effect = [
            (total_posts,), # Total posts
        ]

        mock_cursor.fetchall.side_effect = [
            new_posts,      # New posts
            updated_posts,  # Updated posts
            rankings,       # Latest SEO rankings
            past_rankings,  # Previous SEO rankings
        ]

        # Run generator
        self.generator.generate_daily_report()

        # Check the generated file
        files = os.listdir(self.report_dir)
        self.assertTrue(len(files) > 0)
        report_path = os.path.join(self.report_dir, files[0])

        with open(report_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Assertions for FIX (what we expect AFTER the fix)

        # 1. Check for escaped script tag in New Posts section
        # The code SHOULD sanitize HTML, so we expect escaped characters.
        self.assertNotIn("<script>alert('xss')</script>", content)
        # html.escape escapes single quotes to &#x27; by default
        self.assertIn("&lt;script&gt;alert(&#x27;xss&#x27;)&lt;/script&gt;", content)

        # 2. Check for escaped pipes in Updated Posts section
        # The code SHOULD replace pipes with &#124; to preserve table structure.
        self.assertNotIn("| old | val | new | val |", content)
        self.assertIn("old &#124; val", content)
        self.assertIn("new &#124; val", content)

        # 3. Check for escaped pipes in Rankings section
        self.assertNotIn("| query | injection |", content)
        self.assertIn("query &#124; injection", content)

if __name__ == '__main__':
    unittest.main()
