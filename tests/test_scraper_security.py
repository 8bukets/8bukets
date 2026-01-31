import unittest
import os
import csv
from scraper import OracleNewsScraper

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        self.output_json = "test_links.json"
        self.output_csv = "test_links.csv"
        self.output_txt = "test_unique_links.txt"
        self.scraper = OracleNewsScraper(
            output_json=self.output_json,
            output_csv=self.output_csv,
            output_txt=self.output_txt
        )

    def tearDown(self):
        for f in [self.output_json, self.output_csv, self.output_txt]:
            if os.path.exists(f):
                os.remove(f)

    def test_csv_injection(self):
        """
        Test that fields starting with =, +, -, @ are sanitized to prevent CSV injection.
        """
        posts = [{
            'title': '=1+1',
            'date': 'Oct 15, 2025',
            'author': 'Hacker',
            'categories': ['News'],
            'external_link': 'http://example.com',
            'domain': 'example.com',
            'post_url': 'http://example.com/post'
        }]

        self.scraper.save_data(posts)

        with open(self.output_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)
            # The title is the first column
            title = row[0]

            # Verify that the field is sanitized by prepending a single quote
            self.assertEqual(title, "'=1+1", "CSV Injection vulnerability should be prevented by sanitization")

if __name__ == '__main__':
    unittest.main()
