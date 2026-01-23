import os
import csv
import sys
import unittest
from scraper import OracleNewsScraper

class TestCSVInjection(unittest.TestCase):
    def setUp(self):
        self.json_file = "test_links.json"
        self.csv_file = "test_links.csv"
        self.txt_file = "test_unique_links.txt"
        self.scraper = OracleNewsScraper(self.json_file, self.csv_file, self.txt_file)

    def tearDown(self):
        if os.path.exists(self.json_file): os.remove(self.json_file)
        if os.path.exists(self.csv_file): os.remove(self.csv_file)
        if os.path.exists(self.txt_file): os.remove(self.txt_file)

    def test_csv_sanitization(self):
        # Malicious payload
        malicious_posts = [{
            'title': '=cmd|\' /C calc\'!A0',
            'date': 'Oct 15, 2025',
            'author': '@attacker',
            'categories': ['+News'],
            'external_link': '-http://example.com',
            'domain': 'example.com',
            'post_url': 'http://example.com'
        }]

        # Execution
        self.scraper.save_data(malicious_posts)

        # Verification
        with open(self.csv_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)

            # Check Title
            self.assertTrue(row[0].startswith("'="), f"Title not sanitized: {row[0]}")
            # Check Author
            self.assertTrue(row[2].startswith("'@"), f"Author not sanitized: {row[2]}")
            # Check Categories
            self.assertTrue(row[3].startswith("'+"), f"Categories not sanitized: {row[3]}")
            # Check External Link
            self.assertTrue(row[4].startswith("'-"), f"External Link not sanitized: {row[4]}")

if __name__ == "__main__":
    unittest.main()
