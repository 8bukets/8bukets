
import unittest
import os
import csv
from scraper import MarkPositionScraperAsync

class TestCSVInjection(unittest.TestCase):
    def setUp(self):
        self.csv_file = 'test_injection.csv'
        self.json_file = 'test_injection.json'
        self.txt_file = 'test_injection.txt'
        self.scraper = MarkPositionScraperAsync(self.json_file, self.csv_file, self.txt_file)

    def tearDown(self):
        if os.path.exists(self.csv_file):
            os.remove(self.csv_file)
        if os.path.exists(self.json_file):
            os.remove(self.json_file)
        if os.path.exists(self.txt_file):
            os.remove(self.txt_file)

    def test_csv_injection(self):
        # Malicious payloads
        malicious_posts = [
            {
                'title': '=1+1',
                'author': '@SUM(1+1)',
                'date': '-1+1',
                'categories': ['+1+1'],
                'external_link': 'http://example.com',
                'domain': 'example.com',
                'post_url': 'http://example.com/post'
            }
        ]

        self.scraper.save_data(malicious_posts)

        with open(self.csv_file, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)

            # Check if any field starts with the dangerous characters
            # In a secure implementation, these should be escaped (e.g. prefixed with ')

            # Title: =1+1 should become '=1+1
            self.assertTrue(row[0].startswith("'="), f"Title NOT sanitized: {row[0]}")

            # Date: -1+1 should become '-1+1
            self.assertTrue(row[1].startswith("'-"), f"Date NOT sanitized: {row[1]}")

            # Author: @SUM(1+1) should become '@SUM(1+1)
            self.assertTrue(row[2].startswith("'@"), f"Author NOT sanitized: {row[2]}")

            # Categories: +1+1 should become '+1+1
            self.assertTrue(row[3].startswith("'+"), f"Categories NOT sanitized: {row[3]}")

            print(f"Row content: {row}")

if __name__ == '__main__':
    unittest.main()
