import unittest
import os
import csv
from scraper import OracleNewsScraper

class TestCSVSecurity(unittest.TestCase):
    def setUp(self):
        self.output_json = "test_output.json"
        self.output_csv = "test_output.csv"
        self.output_txt = "test_output.txt"
        self.scraper = OracleNewsScraper(self.output_json, self.output_csv, self.output_txt)

    def tearDown(self):
        for f in [self.output_json, self.output_csv, self.output_txt]:
            if os.path.exists(f):
                os.remove(f)

    def test_csv_injection_prevention(self):
        # Malicious data
        posts = [
            {
                'title': '=cmd|/c calc!A0',
                'date': 'Oct 15, 2025',
                'author': '+Author',
                'categories': ['@Category'],
                'external_link': '-http://evil.com',
                'domain': 'oracle.com',
                'post_url': 'http://oracle.com/post'
            }
        ]

        # Save data
        self.scraper.save_data(posts)

        # Verify CSV content
        with open(self.output_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)

            # Check if dangerous fields are escaped
            # Expecting single quote prepended
            self.assertTrue(row[0].startswith("'="), f"Title not escaped: {row[0]}")
            self.assertTrue(row[2].startswith("'+"), f"Author not escaped: {row[2]}")
            self.assertTrue(row[3].startswith("'@"), f"Categories not escaped: {row[3]}")
            self.assertTrue(row[4].startswith("'-"), f"External Link not escaped: {row[4]}")

if __name__ == '__main__':
    unittest.main()
