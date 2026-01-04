import unittest
from unittest.mock import MagicMock, mock_open, patch
import sys
import os
import csv
import io

# Add repo root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scraper import MarkPositionScraperAsync

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        self.scraper = MarkPositionScraperAsync("json", "csv", "txt")

    def test_save_batch_csv_injection(self):
        # Mock the file objects
        mock_json_f = MagicMock()
        mock_txt_f = MagicMock()

        # We need to capture what is written to the CSV
        csv_output = io.StringIO()
        csv_writer = csv.writer(csv_output)

        seen_links = set()

        # Create a post with a malicious title
        malicious_post = {
            'title': '=cmd|/C calc!A0',
            'date': '2023-01-01',
            'author': 'Hacker',
            'categories': ['News'],
            'external_link': 'http://evil.com',
            'domain': 'evil.com',
            'post_url': 'http://wordpress.com/post'
        }

        posts = [malicious_post]

        # Call the method
        self.scraper.save_batch(posts, mock_json_f, csv_writer, mock_txt_f, seen_links, True)

        # Check the output
        output_content = csv_output.getvalue()

        # Currently, we expect the vulnerability to be present (no single quote prepended)
        # So this test failing means the vulnerability exists (or rather, the test asserting "safe" behavior will fail)

        # Let's write the assertion for the SAFE behavior we want.
        # We expect the title to be rewritten to "'=cmd|/C calc!A0"

        expected_title_part = "'=cmd|/C calc!A0"

        # If this assertion fails, it confirms the vulnerability (or lack of fix).
        self.assertIn(expected_title_part, output_content)

if __name__ == '__main__':
    unittest.main()
