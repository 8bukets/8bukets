import csv
import os
import unittest
from scraper import MarkPositionScraperAsync

class TestCSVSecurity(unittest.TestCase):
    def setUp(self):
        self.output_json = "test_links.json"
        self.output_csv = "test_links.csv"
        self.output_txt = "test_links.txt"
        self.scraper = MarkPositionScraperAsync(
            output_json=self.output_json,
            output_csv=self.output_csv,
            output_txt=self.output_txt
        )

    def tearDown(self):
        # Clean up test files
        for f in [self.output_json, self.output_csv, self.output_txt]:
            if os.path.exists(f):
                os.remove(f)

    def test_csv_injection_prevention(self):
        # Malicious inputs
        malicious_posts = [
            {
                'title': '=cmd|/C calc!A0',
                'date': '2023-10-27',
                'author': 'Hacker',
                'categories': ['Security'],
                'external_link': '@SUM(1+1)*cmd|/C calc!A0',
                'domain': 'example.com',
                'post_url': 'http://example.com'
            }
        ]

        # Save data
        self.scraper.save_data(malicious_posts)

        # Read CSV and check for sanitized content
        with open(self.output_csv, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)

            # Check Title (index 0) - Expecting it to be escaped with a single quote
            self.assertEqual(row[0], "'=cmd|/C calc!A0", "Fix verified: Title IS sanitized")

            # Check External Link (index 4) - Expecting it to be escaped with a single quote
            self.assertEqual(row[4], "'@SUM(1+1)*cmd|/C calc!A0", "Fix verified: External Link IS sanitized")

if __name__ == '__main__':
    unittest.main()
