import unittest
import csv
import os
import sys
import json

# Add parent directory to path to import scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import MarkPositionScraperAsync

class TestCSVInjection(unittest.TestCase):
    def setUp(self):
        self.output_json = "test_links.json"
        self.output_csv = "test_links.csv"
        self.output_txt = "test_links.txt"
        self.scraper = MarkPositionScraperAsync(self.output_json, self.output_csv, self.output_txt)

    def tearDown(self):
        if os.path.exists(self.output_json):
            os.remove(self.output_json)
        if os.path.exists(self.output_csv):
            os.remove(self.output_csv)
        if os.path.exists(self.output_txt):
            os.remove(self.output_txt)

    def test_csv_injection(self):
        # Malicious data simulating formula injection
        malicious_posts = [
            {
                'title': '=cmd|/C calc!A0',
                'date': '2023-10-27',
                'author': '@attacker',
                'categories': ['+hacking'],
                'external_link': '-http://evil.com',
                'domain': 'evil.com',
                'post_url': 'http://example.com'
            }
        ]

        self.scraper.save_data(malicious_posts)

        with open(self.output_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)

            # Check if fields ARE sanitized (fix confirmation)
            # They should start with '
            self.assertTrue(row[0].startswith("'="), f"Title should be sanitized, got: {row[0]}")
            self.assertTrue(row[2].startswith("'@"), f"Author should be sanitized, got: {row[2]}")
            self.assertTrue(row[3].startswith("'+"), f"Categories should be sanitized, got: {row[3]}")
            self.assertTrue(row[4].startswith("'-"), f"External Link should be sanitized, got: {row[4]}")

if __name__ == '__main__':
    unittest.main()
