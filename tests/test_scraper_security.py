import unittest
import os
import csv
import sys

# Add root directory to sys.path to import scraper
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scraper import OracleNewsScraper

class TestCSVInjection(unittest.TestCase):
    def setUp(self):
        self.output_json = 'tests/test_output.json'
        self.output_csv = 'tests/test_output.csv'
        self.output_txt = 'tests/test_output.txt'
        self.scraper = OracleNewsScraper(self.output_json, self.output_csv, self.output_txt)

    def tearDown(self):
        # Cleanup files
        for f in [self.output_json, self.output_csv, self.output_txt]:
            if os.path.exists(f):
                os.remove(f)

    def test_csv_injection_vulnerability(self):
        # Payload starting with '='
        malicious_title = "=1+1"
        posts = [{
            'title': malicious_title,
            'date': 'Oct 15, 2025',
            'author': 'Hacker',
            'categories': ['News'],
            'external_link': 'http://example.com',
            'domain': 'example.com',
            'post_url': 'http://example.com'
        }]

        self.scraper.save_data(posts)

        # Read CSV and verify vulnerability
        with open(self.output_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader)
            row = next(reader)
            # row[0] corresponds to 'Title'
            self.assertEqual(row[0], "'=1+1", "Vulnerability fixed: malicious payload sanitized with leading quote")

if __name__ == '__main__':
    unittest.main()
