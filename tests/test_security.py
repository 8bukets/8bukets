import unittest
import csv
import os
from scraper import OracleNewsScraper

class TestCSVInjection(unittest.TestCase):
    def setUp(self):
        self.output_json = "test_output.json"
        self.output_csv = "test_output.csv"
        self.output_txt = "test_output.txt"
        self.scraper = OracleNewsScraper(self.output_json, self.output_csv, self.output_txt)

    def tearDown(self):
        if os.path.exists(self.output_json):
            os.remove(self.output_json)
        if os.path.exists(self.output_csv):
            os.remove(self.output_csv)
        if os.path.exists(self.output_txt):
            os.remove(self.output_txt)

    def test_sanitize_for_csv(self):
        # Test cases for injection characters
        self.assertEqual(self.scraper.sanitize_for_csv("=1+1"), "'=1+1")
        self.assertEqual(self.scraper.sanitize_for_csv("+1+1"), "'+1+1")
        self.assertEqual(self.scraper.sanitize_for_csv("-1+1"), "'-1+1")
        self.assertEqual(self.scraper.sanitize_for_csv("@SUM(1,1)"), "'@SUM(1,1)")

        # Test safe strings
        self.assertEqual(self.scraper.sanitize_for_csv("Safe Text"), "Safe Text")
        self.assertEqual(self.scraper.sanitize_for_csv("123"), "123")
        self.assertEqual(self.scraper.sanitize_for_csv(""), "")

    def test_save_data_sanitization(self):
        malicious_posts = [
            {
                'title': '=cmd|/c calc',
                'date': '@SUM(1,1)',
                'author': 'Normal Author',
                'categories': ['News'],
                'external_link': 'http://example.com',
                'domain': 'example.com',
                'post_url': 'http://example.com'
            }
        ]

        self.scraper.save_data(malicious_posts)

        with open(self.output_csv, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader) # Skip header
            row = next(reader)

            # Check title
            self.assertEqual(row[0], "'=cmd|/c calc")
            # Check date
            self.assertEqual(row[1], "'@SUM(1,1)")
            # Check normal field
            self.assertEqual(row[2], "Normal Author")

if __name__ == '__main__':
    unittest.main()
