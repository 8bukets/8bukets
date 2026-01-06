import unittest
import csv
import os
from scraper import OracleNewsScraper

class TestCSVInjection(unittest.TestCase):
    def setUp(self):
        self.output_csv = "test_injection.csv"
        # Dummy files for other outputs
        self.output_json = "test_dummy.json"
        self.output_txt = "test_dummy.txt"
        self.scraper = OracleNewsScraper(self.output_json, self.output_csv, self.output_txt)

    def tearDown(self):
        if os.path.exists(self.output_csv):
            os.remove(self.output_csv)
        if os.path.exists(self.output_json):
            os.remove(self.output_json)
        if os.path.exists(self.output_txt):
            os.remove(self.output_txt)

    def test_csv_injection(self):
        malicious_title = "=SUM(1+1)"
        posts = [{
            "title": malicious_title,
            "date": "Oct 15, 2025",
            "author": "Hacker",
            "categories": ["News"],
            "external_link": "http://example.com",
            "domain": "example.com",
            "post_url": "http://example.com"
        }]

        self.scraper.save_data(posts)

        with open(self.output_csv, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)
            title = row[0]

        # The test expects the fix to be applied (prefixed with single quote)
        self.assertEqual(title, "'" + malicious_title, "Input should be sanitized with a leading quote")

if __name__ == '__main__':
    unittest.main()
