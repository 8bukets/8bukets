import unittest
import os
import csv
import sys
# Add parent directory to path to import scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scraper import MarkPositionScraperAsync

class TestCSVInjection(unittest.TestCase):
    def setUp(self):
        self.output_json = 'test_links.json'
        self.output_csv = 'test_links.csv'
        self.output_txt = 'test_unique_links.txt'
        self.scraper = MarkPositionScraperAsync(
            self.output_json, self.output_csv, self.output_txt
        )

    def tearDown(self):
        for f in [self.output_json, self.output_csv, self.output_txt]:
            if os.path.exists(f):
                os.remove(f)

    def test_csv_injection_prevention(self):
        # Malicious payloads
        malicious_posts = [
            {
                'title': '=cmd|/C calc!A0',
                'date': '+2021-01-01',
                'author': '-Author',
                'categories': ['@Category'],
                'external_link': 'http://example.com',
                'domain': 'example.com',
                'post_url': 'http://post.url'
            }
        ]

        self.scraper.save_data(malicious_posts)

        with open(self.output_csv, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader) # Skip header
            row = next(reader)

            # Helper to check if sanitized
            def is_sanitized(val):
                # Should start with ' if original started with =, +, -, @
                return val.startswith("'")

            # Check fields
            # ['Title', 'Date', 'Author', 'Categories', 'External Link', 'Domain', 'Post URL']
            self.assertTrue(is_sanitized(row[0]), f"Title not sanitized: {row[0]}")
            self.assertTrue(is_sanitized(row[1]), f"Date not sanitized: {row[1]}")
            self.assertTrue(is_sanitized(row[2]), f"Author not sanitized: {row[2]}")
            self.assertTrue(is_sanitized(row[3]), f"Categories not sanitized: {row[3]}")

if __name__ == '__main__':
    unittest.main()
