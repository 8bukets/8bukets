
import csv
import os
import unittest
from scraper import MarkPositionScraperAsync

class TestCSVInjection(unittest.TestCase):
    def setUp(self):
        self.csv_file = 'test_injection.csv'
        self.json_file = 'test_injection.json'
        self.txt_file = 'test_injection.txt'
        self.scraper = MarkPositionScraperAsync(
            output_json=self.json_file,
            output_csv=self.csv_file,
            output_txt=self.txt_file
        )

    def tearDown(self):
        for f in [self.csv_file, self.json_file, self.txt_file]:
            if os.path.exists(f):
                os.remove(f)

    def test_csv_injection(self):
        # Data with potential CSV injection payloads
        malicious_data = [
            {
                'title': '=cmd|/C calc!A0',
                'author': '+SUM(1+1)',
                'categories': ['-1-1'],
                'external_link': '@SUM(1+1)',
                'domain': 'example.com',
                'post_url': 'http://example.com'
            }
        ]

        self.scraper.save_data(malicious_data)

        with open(self.csv_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)

            # Check if fields are sanitized (should start with single quote)
            # Title
            self.assertTrue(row[0].startswith("'"), f"Title not sanitized: {row[0]}")
            self.assertEqual(row[0], "'=cmd|/C calc!A0")

            # Author (index 2 in scraper.save_data: Title, Date, Author...)
            self.assertTrue(row[2].startswith("'"), f"Author not sanitized: {row[2]}")

            # Categories (index 3)
            self.assertTrue(row[3].startswith("'"), f"Categories not sanitized: {row[3]}")

            # External Link (index 4)
            self.assertTrue(row[4].startswith("'"), f"External Link not sanitized: {row[4]}")

    def test_normal_data(self):
        # Normal data should remain unchanged
        normal_data = [
            {
                'title': 'Normal Title',
                'author': 'Normal Author',
                'categories': ['News'],
                'external_link': 'http://google.com',
                'domain': 'google.com',
                'post_url': 'http://example.com/post'
            }
        ]

        self.scraper.save_data(normal_data)

        with open(self.csv_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)

            self.assertEqual(row[0], 'Normal Title')
            self.assertEqual(row[2], 'Normal Author')
            self.assertEqual(row[3], 'News')
            self.assertEqual(row[4], 'http://google.com')

if __name__ == '__main__':
    unittest.main()
