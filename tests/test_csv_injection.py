import unittest
import os
import csv
import sys

# Add parent directory to path so we can import scraper
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scraper import MarkPositionScraperAsync

class TestCSVInjection(unittest.TestCase):
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
        for f in [self.output_json, self.output_csv, self.output_txt]:
            if os.path.exists(f):
                os.remove(f)

    def test_csv_injection_mitigation(self):
        # Data with CSV injection payload
        malicious_data = [{
            'title': '=cmd|/C calc!A0',
            'date': '2023-10-27',
            'author': '@attacker',
            'categories': ['Security'],
            'external_link': 'http://example.com',
            'domain': 'example.com',
            'post_url': 'http://example.com/post'
        }]

        # Save data
        self.scraper.save_data(malicious_data)

        # Read CSV and check if payload is sanitized
        with open(self.output_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader)
            row = next(reader)

            title = row[0]
            author = row[2]

            # Assertions
            self.assertTrue(title.startswith("'"), f"Title should be sanitized (quoted), got: {title}")
            self.assertTrue(author.startswith("'"), f"Author should be sanitized (quoted), got: {author}")
            self.assertEqual(title, "'=cmd|/C calc!A0")
            self.assertEqual(author, "'@attacker")

if __name__ == '__main__':
    unittest.main()
