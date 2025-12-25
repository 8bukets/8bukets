import unittest
import csv
import os
import json
from scraper import OracleNewsScraper

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        self.output_json = 'test_output.json'
        self.output_csv = 'test_output.csv'
        self.output_txt = 'test_output.txt'
        self.scraper = OracleNewsScraper(self.output_json, self.output_csv, self.output_txt)

    def tearDown(self):
        for f in [self.output_json, self.output_csv, self.output_txt]:
            if os.path.exists(f):
                os.remove(f)

    def test_csv_injection_prevention(self):
        # Malicious data
        malicious_posts = [
            {
                'title': '=cmd|/C calc!A0',
                'date': 'Oct 15, 2025',
                'author': 'Hacker',
                'categories': ['Hack'],
                'external_link': 'http://evil.com',
                'domain': 'evil.com',
                'post_url': 'http://evil.com'
            },
            {
                'title': '+SUM(1+1)',
                'date': 'Oct 15, 2025',
                'author': 'Hacker',
                'categories': ['Hack'],
                'external_link': 'http://evil.com',
                'domain': 'evil.com',
                'post_url': 'http://evil.com'
            },
             {
                'title': '@SUM(1+1)',
                'date': 'Oct 15, 2025',
                'author': 'Hacker',
                'categories': ['Hack'],
                'external_link': 'http://evil.com',
                'domain': 'evil.com',
                'post_url': 'http://evil.com'
            },
             {
                'title': '-SUM(1+1)',
                'date': 'Oct 15, 2025',
                'author': 'Hacker',
                'categories': ['Hack'],
                'external_link': 'http://evil.com',
                'domain': 'evil.com',
                'post_url': 'http://evil.com'
            }
        ]

        # Save data
        self.scraper.save_data(malicious_posts)

        # Verify CSV content
        with open(self.output_csv, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader) # Skip header
            rows = list(reader)

        # Check if the leading characters are sanitized (e.g., prefixed with ')
        for row in rows:
            title = row[0]
            # If the original title started with =, +, -, @, it should now be sanitized
            # A common sanitation is prepending a single quote
            self.assertTrue(title.startswith("'") or title.startswith("\t"),
                            f"CSV Injection vulnerability found! Title '{title}' was not sanitized.")

if __name__ == '__main__':
    unittest.main()
