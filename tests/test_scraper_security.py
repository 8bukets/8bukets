import unittest
import csv
import os
import sys
import json
from scraper import MarkPositionScraperAsync

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        self.output_json = "test_security.json"
        self.output_csv = "test_security.csv"
        self.output_txt = "test_security.txt"
        self.scraper = MarkPositionScraperAsync(self.output_json, self.output_csv, self.output_txt)

    def tearDown(self):
        if os.path.exists(self.output_json): os.remove(self.output_json)
        if os.path.exists(self.output_csv): os.remove(self.output_csv)
        if os.path.exists(self.output_txt): os.remove(self.output_txt)

    def test_csv_injection_sanitization(self):
        """Test that CSV output is sanitized against formula injection."""
        malicious_posts = [
            {
                'title': '=cmd|\' /C calc\'!A0',
                'date': '2023-01-01',
                'author': '+MaliciousAuthor',
                'categories': ['-BadCategory'],
                'external_link': '@http://evil.com',
                'domain': 'evil.com',
                'post_url': 'http://example.com'
            }
        ]

        self.scraper.save_data(malicious_posts)

        with open(self.output_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)

            # Title
            self.assertTrue(row[0].startswith("'="), f"Title not sanitized: {row[0]}")
            # Author
            self.assertTrue(row[2].startswith("'+"), f"Author not sanitized: {row[2]}")
            # Categories (joined string)
            self.assertTrue(row[3].startswith("'-"), f"Categories not sanitized: {row[3]}")
            # External Link
            self.assertTrue(row[4].startswith("'@"), f"External Link not sanitized: {row[4]}")

if __name__ == '__main__':
    unittest.main()
