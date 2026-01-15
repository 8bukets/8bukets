import unittest
import csv
import os
import sys

# Add parent directory to path so we can import scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import OracleNewsScraper

class TestCSVInjection(unittest.TestCase):
    def setUp(self):
        self.output_json = "test_output.json"
        self.output_csv = "test_output.csv"
        self.output_txt = "test_output.txt"
        self.scraper = OracleNewsScraper(self.output_json, self.output_csv, self.output_txt)

    def tearDown(self):
        for f in [self.output_json, self.output_csv, self.output_txt]:
            if os.path.exists(f):
                os.remove(f)

    def test_csv_injection_sanitization(self):
        """
        Verify that CSV injection characters are sanitized.
        """
        malicious_post = {
            'title': '=1+1',  # Malicious
            'date': 'Oct 15, 2025',
            'author': '@attacker', # Malicious
            'categories': ['News', '+BadCategory'], # Malicious
            'external_link': 'http://example.com',
            'domain': 'example.com',
            'post_url': 'http://example.com/post'
        }

        posts = [malicious_post]
        self.scraper.save_data(posts)

        # Verify the file was written and read it back
        with open(self.output_csv, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)

            # Row structure: Title, Date, Author, Categories, External Link, Domain, Post URL
            # Expected sanitized output
            self.assertEqual(row[0], "'=1+1")
            self.assertEqual(row[2], "'@attacker")

            # Categories are joined: "News, +BadCategory"
            # It does not start with malicious char, so it is NOT sanitized by startswith check.
            # This is expected behavior for the current implementation which only checks the start of the cell.
            self.assertEqual(row[3], "News, +BadCategory")

    def test_csv_injection_categories_start(self):
        """
        Verify sanitization when the first category is malicious.
        """
        malicious_post = {
            'title': 'Safe Title',
            'date': 'Oct 15, 2025',
            'author': 'Safe Author',
            'categories': ['+BadCategory', 'News'],
            'external_link': 'http://example.com',
            'domain': 'example.com',
            'post_url': 'http://example.com/post'
        }

        posts = [malicious_post]
        self.scraper.save_data(posts)

        with open(self.output_csv, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)

            # Categories: "+BadCategory, News" -> should be sanitized
            self.assertEqual(row[3], "'+BadCategory, News")

if __name__ == '__main__':
    unittest.main()
