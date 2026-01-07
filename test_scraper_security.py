import unittest
import csv
import os
import shutil
from scraper import OracleNewsScraper

class TestCSVInjectionFix(unittest.TestCase):
    def setUp(self):
        self.output_json = 'test_links_fix.json'
        self.output_csv = 'test_links_fix.csv'
        self.output_txt = 'test_unique_links_fix.txt'
        self.scraper = OracleNewsScraper(self.output_json, self.output_csv, self.output_txt)

    def tearDown(self):
        if os.path.exists(self.output_json):
            os.remove(self.output_json)
        if os.path.exists(self.output_csv):
            os.remove(self.output_csv)
        if os.path.exists(self.output_txt):
            os.remove(self.output_txt)

    def test_csv_sanitization(self):
        # Data with potential CSV injection payloads
        malicious_data = [{
            'title': '=cmd|/c calc!A0',
            'date': '@SUM(1+1)*cmd|\' /C calc\'!A0',
            'author': '+1-2',
            'categories': ['-1+1'],
            'external_link': '=HYPERLINK("http://malicious.com")',
            'domain': '@malicious.com',
            'post_url': '+http://example.com'
        }]

        # Save data
        self.scraper.save_data(malicious_data)

        # Read the CSV and check for sanitization (prefixing with ')
        with open(self.output_csv, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader)
            row = next(reader)

            # The vulnerability is fixed if these start with '
            self.assertTrue(row[0].startswith("'="), f"Title should be sanitized. Got: {row[0]}")
            self.assertTrue(row[1].startswith("'@"), f"Date should be sanitized. Got: {row[1]}")
            self.assertTrue(row[2].startswith("'+"), f"Author should be sanitized. Got: {row[2]}")
            self.assertTrue(row[3].startswith("'-"), f"Categories should be sanitized. Got: {row[3]}")
            self.assertTrue(row[4].startswith("'="), f"External Link should be sanitized. Got: {row[4]}")
            self.assertTrue(row[5].startswith("'@"), f"Domain should be sanitized. Got: {row[5]}")
            self.assertTrue(row[6].startswith("'+"), f"Post URL should be sanitized. Got: {row[6]}")

if __name__ == '__main__':
    unittest.main()
