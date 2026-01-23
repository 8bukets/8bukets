import unittest
import csv
import io
import sys
import os

# Ensure we can import from parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scraper import MarkPositionScraperAsync

class TestCSVInjection(unittest.TestCase):
    def test_csv_injection(self):
        # Initialize scraper with dummy paths
        scraper = MarkPositionScraperAsync("dummy.json", "dummy.csv", "dummy.txt")

        # Create a list of posts with malicious payloads
        posts = [
            {
                'title': '=cmd|/C calc!A0',
                'date': '+2023-01-01',
                'author': '@attacker',
                'categories': ['-badcat'], # Will be joined to "-badcat"
                'external_link': 'http://example.com',
                'domain': 'example.com',
                'post_url': 'http://example.com/post'
            }
        ]

        # Mocks
        json_f = io.StringIO()
        csv_output = io.StringIO()
        csv_writer = csv.writer(csv_output)
        txt_f = io.StringIO()
        seen_links = set()

        # Call save_batch
        scraper.save_batch(posts, json_f, csv_writer, txt_f, seen_links, True)

        # Get CSV content
        content = csv_output.getvalue()

        # We expect sanitization (prepending ')
        # Since the code is not fixed yet, these assertions should FAIL if I wrote them to expect the fix.
        # But I want to confirm the vulnerability exists first.
        # Actually, standard TDD says write a failing test.
        # So I expect the OUTPUT to be sanitized.

        self.assertIn("'=cmd|/C calc!A0", content, "Title should be sanitized")
        self.assertIn("'+2023-01-01", content, "Date should be sanitized")
        self.assertIn("'@attacker", content, "Author should be sanitized")
        self.assertIn("'-badcat", content, "Categories should be sanitized")

if __name__ == '__main__':
    unittest.main()
