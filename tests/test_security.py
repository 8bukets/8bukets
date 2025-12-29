
import unittest
import csv
import os
import json
from scraper import MarkPositionScraperAsync

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        self.output_json = "test_sec_links.json"
        self.output_csv = "test_sec_links.csv"
        self.output_txt = "test_sec_unique_links.txt"
        self.scraper = MarkPositionScraperAsync(self.output_json, self.output_csv, self.output_txt)

    def tearDown(self):
        for f in [self.output_json, self.output_csv, self.output_txt]:
            if os.path.exists(f):
                os.remove(f)

    def test_csv_injection_prevention(self):
        """Test that CSV injection payloads are sanitized."""
        # Create dummy data with malicious payloads
        malicious_posts = [
            {
                'title': '=cmd|/C calc!A0',
                'author': 'Normal Author',
                'date': '2023-01-01',
                'categories': ['Tech'],
                'external_link': 'http://example.com',
                'domain': 'example.com',
                'post_url': 'http://wp.com/post1'
            },
            {
                'title': 'Safe Title',
                'author': '+1-1', # Malicious author
                'date': '2023-01-02',
                'categories': ['News'],
                'external_link': 'http://example.org',
                'domain': 'example.org',
                'post_url': 'http://wp.com/post2'
            },
            {
                'title': '@SUM(1+1)',
                'author': '-100',
                'date': '2023-01-03',
                'categories': ['Finance'],
                'external_link': 'http://example.net',
                'domain': 'example.net',
                'post_url': 'http://wp.com/post3'
            }
        ]

        # Save data using the scraper's method
        self.scraper.save_data(malicious_posts)

        # Read back the CSV and check for sanitization
        with open(self.output_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader) # Skip header
            rows = list(reader)

        # Row 0: Title starts with =
        self.assertEqual(rows[0][0], "'=cmd|/C calc!A0", "Title starting with = should be quoted")

        # Row 1: Author starts with +
        self.assertEqual(rows[1][2], "'+1-1", "Author starting with + should be quoted")

        # Row 2: Title starts with @, Author starts with -
        self.assertEqual(rows[2][0], "'@SUM(1+1)", "Title starting with @ should be quoted")
        self.assertEqual(rows[2][2], "'-100", "Author starting with - should be quoted")

if __name__ == '__main__':
    unittest.main()
