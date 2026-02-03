import unittest
import os
import csv
from scraper import MarkPositionScraperAsync

class TestCSVInjection(unittest.TestCase):
    def setUp(self):
        self.output_json = 'test_links.json'
        self.output_csv = 'test_links.csv'
        self.output_txt = 'test_links.txt'
        self.scraper = MarkPositionScraperAsync(
            output_json=self.output_json,
            output_csv=self.output_csv,
            output_txt=self.output_txt
        )

    def tearDown(self):
        for f in [self.output_json, self.output_csv, self.output_txt]:
            if os.path.exists(f):
                os.remove(f)

    def test_csv_content(self):
        # Malicious data
        malicious_data = [{
            'title': '=1+1',
            'date': '@SUM(1,1)',
            'author': '-1',
            'categories': ['+1'],
            'external_link': '=cmd|/C calc!A0',
            'domain': 'example.com',
            'post_url': 'http://example.com'
        }]

        self.scraper.save_data(malicious_data)

        # Read CSV
        with open(self.output_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)

        # CHECK SECURE BEHAVIOR (Post-fix)
        # We expect the values to be escaped with a single quote
        self.assertEqual(row[0], "'=1+1") # Title
        self.assertEqual(row[1], "'@SUM(1,1)") # Date
        self.assertEqual(row[2], "'-1") # Author
        self.assertEqual(row[3], "'+1") # Categories
        self.assertEqual(row[4], "'=cmd|/C calc!A0") # External Link

if __name__ == '__main__':
    unittest.main()
