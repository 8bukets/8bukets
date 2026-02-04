import unittest
import os
import csv
from scraper import OracleNewsScraper

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        self.output_json = "test_sec_links.json"
        self.output_csv = "test_sec_links.csv"
        self.output_txt = "test_sec_unique_links.txt"
        self.scraper = OracleNewsScraper(self.output_json, self.output_csv, self.output_txt)

    def tearDown(self):
        for f in [self.output_json, self.output_csv, self.output_txt]:
            if os.path.exists(f):
                os.remove(f)

    def test_csv_injection_prevention(self):
        """Test that potential CSV injection payloads are sanitized."""
        malicious_posts = [
            {
                'title': '=cmd|/C calc!A0',
                'date': '+2025-01-01',
                'author': '-Author',
                'categories': ['@Category'],
                'external_link': 'http://example.com',
                'domain': 'example.com',
                'post_url': 'http://example.com/post'
            }
        ]

        self.scraper.save_data(malicious_posts)

        with open(self.output_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)

            # Row structure: ['Title', 'Date', 'Author', 'Categories', 'External Link', 'Domain', 'Post URL']

            # Check Title (=)
            self.assertEqual(row[0], "'=cmd|/C calc!A0", "Title starting with '=' should be escaped")
            # Check Date (+)
            self.assertEqual(row[1], "'+2025-01-01", "Date starting with '+' should be escaped")
            # Check Author (-)
            self.assertEqual(row[2], "'-Author", "Author starting with '-' should be escaped")
            # Check Categories (@)
            self.assertEqual(row[3], "'@Category", "Categories starting with '@' should be escaped")

    def test_safe_data_not_escaped(self):
        """Test that safe data is not modified."""
        safe_posts = [
            {
                'title': 'Safe Title',
                'date': '2025-01-01',
                'author': 'Safe Author',
                'categories': ['News'],
                'external_link': 'http://example.com',
                'domain': 'example.com',
                'post_url': 'http://example.com/post'
            }
        ]

        self.scraper.save_data(safe_posts)

        with open(self.output_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)

            self.assertEqual(row[0], "Safe Title")
            self.assertEqual(row[1], "2025-01-01")

if __name__ == '__main__':
    unittest.main()
