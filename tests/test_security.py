import unittest
import csv
import os
import json
from scraper import MarkPositionScraperAsync

class TestSecurity(unittest.TestCase):
    def setUp(self):
        self.output_json = 'test_security_links.json'
        self.output_csv = 'test_security_links.csv'
        self.output_txt = 'test_security_links.txt'
        self.scraper = MarkPositionScraperAsync(self.output_json, self.output_csv, self.output_txt)

    def tearDown(self):
        for f in [self.output_json, self.output_csv, self.output_txt]:
            if os.path.exists(f):
                os.remove(f)

    def test_csv_injection_sanitization(self):
        # Create a mock post with malicious payloads
        malicious_posts = [
            {
                'title': '=cmd|/C calc!A0',
                'date': '+2+3',
                'author': '-10+20',
                'categories': ['@SUM(1+1)'],
                'external_link': 'http://example.com',
                'domain': 'example.com',
                'post_url': 'http://example.com/post'
            }
        ]

        # Save data using the scraper
        self.scraper.save_data(malicious_posts)

        # Read the CSV back and check for sanitization
        with open(self.output_csv, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader)
            row = next(reader)

            # Map headers to indices for clarity
            # ['Title', 'Date', 'Author', 'Categories', 'External Link', 'Domain', 'Post URL']

            # Check Title
            self.assertTrue(row[0].startswith("'"), f"Title should be escaped: {row[0]}")
            self.assertEqual(row[0], "'=cmd|/C calc!A0")

            # Check Date
            self.assertTrue(row[1].startswith("'"), f"Date should be escaped: {row[1]}")
            self.assertEqual(row[1], "'+2+3")

            # Check Author
            self.assertTrue(row[2].startswith("'"), f"Author should be escaped: {row[2]}")
            self.assertEqual(row[2], "'-10+20")

            # Check Categories
            # Note: Categories are joined by ", ". The first one starts with @.
            self.assertTrue(row[3].startswith("'"), f"Categories should be escaped: {row[3]}")
            self.assertEqual(row[3], "'@SUM(1+1)")

if __name__ == '__main__':
    unittest.main()
