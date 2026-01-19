import sys
import os
import csv
import unittest

# Add parent directory to path to import scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import MarkPositionScraperAsync

class TestCSVSecurity(unittest.TestCase):
    def setUp(self):
        self.output_json = "test_security_output.json"
        self.output_csv = "test_security_output.csv"
        self.output_txt = "test_security_output.txt"
        self.scraper = MarkPositionScraperAsync(self.output_json, self.output_csv, self.output_txt)

    def tearDown(self):
        # Cleanup
        if os.path.exists(self.output_json): os.remove(self.output_json)
        if os.path.exists(self.output_csv): os.remove(self.output_csv)
        if os.path.exists(self.output_txt): os.remove(self.output_txt)

    def test_csv_injection_prevention(self):
        """Verify that CSV Formula Injection payloads are sanitized."""

        # Payloads starting with different dangerous characters
        posts = [{
            'title': "=cmd|'/C calc'!A0",
            'date': '+2023-10-27',
            'author': "-malicious",
            'categories': ['@Security'],
            'external_link': 'http://example.com',
            'domain': 'example.com',
            'post_url': 'http://example.com/post'
        }]

        # Save data
        self.scraper.save_data(posts)

        # Read CSV and check for sanitization
        with open(self.output_csv, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)

            # Row structure: Title, Date, Author, Categories, ...
            saved_title = row[0]
            saved_date = row[1]
            saved_author = row[2]
            saved_categories = row[3]

            # Assertions: All must be escaped with a single quote
            self.assertEqual(saved_title, "'=cmd|'/C calc'!A0")
            self.assertEqual(saved_date, "'+2023-10-27")
            self.assertEqual(saved_author, "'-malicious")
            self.assertEqual(saved_categories, "'@Security")

    def test_normal_data_untouched(self):
        """Verify that normal data is NOT modified."""

        posts = [{
            'title': "Normal Title",
            'date': "2023-10-27",
            'author': "Alice",
            'categories': ["Tech"],
            'external_link': 'http://example.com',
            'domain': 'example.com',
            'post_url': 'http://example.com/post'
        }]

        self.scraper.save_data(posts)

        with open(self.output_csv, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            row = next(reader)

            self.assertEqual(row[0], "Normal Title")
            self.assertEqual(row[1], "2023-10-27")

if __name__ == "__main__":
    unittest.main()
