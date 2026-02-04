import unittest
import os
import sys
import csv
import json

# Add parent directory to path to import scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import MarkPositionScraperAsync

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        self.output_json = "test_links.json"
        self.output_csv = "test_links.csv"
        self.output_txt = "test_unique_links.txt"
        self.scraper = MarkPositionScraperAsync(
            output_json=self.output_json,
            output_csv=self.output_csv,
            output_txt=self.output_txt
        )

    def tearDown(self):
        # Cleanup created files
        for f in [self.output_json, self.output_csv, self.output_txt]:
            if os.path.exists(f):
                os.remove(f)

    def test_csv_injection_vulnerability(self):
        # Malicious data
        malicious_posts = [
            {
                'title': '=cmd|/C calc!A0',
                'date': '+2023-01-01',
                'author': '-Author',
                'categories': ['@Category'],
                'external_link': 'http://example.com',
                'domain': 'example.com',
                'post_url': 'http://post.com'
            }
        ]

        # Save data
        self.scraper.save_data(malicious_posts)

        # Read CSV and check for raw malicious characters at start
        with open(self.output_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)

            # Check Title
            print(f"Title: {row[0]}")
            # Should be sanitized with single quote
            self.assertEqual(row[0], "'=cmd|/C calc!A0")

            # Check Date
            print(f"Date: {row[1]}")
            self.assertEqual(row[1], "'+2023-01-01")

            # Check Author
            print(f"Author: {row[2]}")
            self.assertEqual(row[2], "'-Author")

            # Check Categories
            print(f"Categories: {row[3]}")
            self.assertEqual(row[3], "'@Category")

if __name__ == '__main__':
    unittest.main()
