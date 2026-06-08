import unittest
import os
import csv
import json
from scraper import MarkPositionScraperAsync

class TestSecurity(unittest.TestCase):
    def setUp(self):
        self.output_json = "sec_test.json"
        self.output_csv = "sec_test.csv"
        self.output_txt = "sec_test.txt"
        self.scraper = MarkPositionScraperAsync(self.output_json, self.output_csv, self.output_txt)

    def tearDown(self):
        for f in [self.output_json, self.output_csv, self.output_txt]:
            if os.path.exists(f):
                os.remove(f)

    def test_csv_injection(self):
        # Data with malicious prefixes
        malicious_posts = [
            {
                'title': '=cmd|/C calc!A0',
                'date': '+2023-01-01',
                'author': '@SUM(1+1)',
                'categories': ['-News'], # Even list items joined could be risky if the first one starts with -
                'external_link': 'http://example.com',
                'domain': 'example.com',
                'post_url': 'http://wordpress.com/post/1'
            }
        ]

        self.scraper.save_data(malicious_posts)

        with open(self.output_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)

            # Check Title (index 0)
            self.assertTrue(row[0].startswith("'"), f"Title not sanitized: {row[0]}")
            self.assertEqual(row[0], "'=cmd|/C calc!A0")

            # Check Date (index 1)
            self.assertTrue(row[1].startswith("'"), f"Date not sanitized: {row[1]}")

            # Check Author (index 2)
            self.assertTrue(row[2].startswith("'"), f"Author not sanitized: {row[2]}")

            # Check Categories (index 3)
            # If categories are joined ", ", and the first one starts with -, the whole cell starts with -
            self.assertTrue(row[3].startswith("'"), f"Categories not sanitized: {row[3]}")

if __name__ == '__main__':
    unittest.main()
