import unittest
import os
import csv
import json
from scraper import MarkPositionScraperAsync

class TestCSVInjection(unittest.TestCase):
    def setUp(self):
        self.output_json = "test_links.json"
        self.output_csv = "test_links.csv"
        self.output_txt = "test_unique_links.txt"
        self.scraper = MarkPositionScraperAsync(
            output_json=self.output_json,
            output_csv=self.output_csv,
            output_txt=self.output_txt
        )

    def tearDown(self):
        if os.path.exists(self.output_json):
            os.remove(self.output_json)
        if os.path.exists(self.output_csv):
            os.remove(self.output_csv)
        if os.path.exists(self.output_txt):
            os.remove(self.output_txt)

    def test_csv_injection_prevention(self):
        # Data with potential CSV injection formulas
        malicious_posts = [
            {
                'title': '=1+1',
                'date': '+2023-01-01',
                'author': '-Admin',
                'categories': ['@Category'],
                'external_link': 'http://example.com',
                'domain': 'example.com',
                'post_url': 'http://example.com/post'
            }
        ]

        # Save data
        self.scraper.save_data(malicious_posts)

        # Read CSV and check if inputs are sanitized (prefixed with ')
        with open(self.output_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader)
            row = next(reader)

            # Check Title: '=1+1' should become ''=1+1'
            self.assertTrue(row[0].startswith("'"), f"Title was not sanitized: {row[0]}")
            self.assertEqual(row[0], "'=1+1")

            # Check Date: '+2023-01-01' should become ''+2023-01-01'
            self.assertTrue(row[1].startswith("'"), f"Date was not sanitized: {row[1]}")
            self.assertEqual(row[1], "'+2023-01-01")

            # Check Author: '-Admin' should become ''-Admin'
            self.assertTrue(row[2].startswith("'"), f"Author was not sanitized: {row[2]}")
            self.assertEqual(row[2], "'-Admin")

            # Check Categories: '@Category' should become ''@Category'
            self.assertTrue(row[3].startswith("'"), f"Categories was not sanitized: {row[3]}")
            self.assertEqual(row[3], "'@Category")

if __name__ == '__main__':
    unittest.main()
