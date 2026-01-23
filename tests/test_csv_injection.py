import sys
import os
import csv
import unittest

# Ensure we can import from the root directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scraper import MarkPositionScraperAsync

class TestCSVInjection(unittest.TestCase):
    def setUp(self):
        self.output_json = "test_output.json"
        self.output_csv = "test_output.csv"
        self.output_txt = "test_output.txt"
        self.scraper = MarkPositionScraperAsync(self.output_json, self.output_csv, self.output_txt)

    def tearDown(self):
        for f in [self.output_json, self.output_csv, self.output_txt]:
            if os.path.exists(f):
                os.remove(f)

    def test_csv_injection_sanitization(self):
        """
        Test that malicious payloads are sanitized when written to CSV.
        """
        malicious_posts = [
            {
                'title': '=1+1',
                'date': '+2023-01-01',
                'author': '-Author',
                'categories': ['@Category'],
                'external_link': 'http://example.com',
                'domain': 'example.com',
                'post_url': 'http://example.com/post'
            }
        ]

        self.scraper.save_data(malicious_posts)

        with open(self.output_csv, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader)
            row = next(reader)

            # AFTER fix: these should start with a single quote
            self.assertTrue(row[0].startswith("'="), f"Title not sanitized: {row[0]}")
            self.assertTrue(row[1].startswith("'+"), f"Date not sanitized: {row[1]}")
            self.assertTrue(row[2].startswith("'-"), f"Author not sanitized: {row[2]}")
            self.assertTrue(row[3].startswith("'@"), f"Categories not sanitized: {row[3]}")

if __name__ == '__main__':
    unittest.main()
