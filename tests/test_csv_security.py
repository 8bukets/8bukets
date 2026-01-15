import unittest
import csv
import os
import shutil
from scraper import MarkPositionScraperAsync

class TestCSVSecurity(unittest.TestCase):
    def setUp(self):
        self.output_json = "test_sec_output.json"
        self.output_csv = "test_sec_output.csv"
        self.output_txt = "test_sec_output.txt"
        self.scraper = MarkPositionScraperAsync(self.output_json, self.output_csv, self.output_txt)

    def tearDown(self):
        for f in [self.output_json, self.output_csv, self.output_txt]:
            if os.path.exists(f):
                os.remove(f)

    def test_csv_injection_sanitization(self):
        malicious_posts = [
            {
                'title': '=cmd|/C calc!A0',
                'date': '+2023-01-01',
                'author': '@attacker',
                'categories': ['-category'],
                'external_link': 'http://normal.com',
                'domain': 'normal.com',
                'post_url': 'http://example.com'
            }
        ]

        self.scraper.save_data(malicious_posts)

        with open(self.output_csv, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)

            # Check that dangerous fields are escaped with '
            self.assertTrue(row[0].startswith("'="), f"Title not sanitized: {row[0]}")
            self.assertTrue(row[1].startswith("'+"), f"Date not sanitized: {row[1]}")
            self.assertTrue(row[2].startswith("'@"), f"Author not sanitized: {row[2]}")
            # Categories are joined
            self.assertTrue(row[3].startswith("'-"), f"Categories not sanitized: {row[3]}")

            # Normal fields should not be escaped
            self.assertEqual(row[4], 'http://normal.com')

if __name__ == '__main__':
    unittest.main()
