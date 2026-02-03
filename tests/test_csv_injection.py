import unittest
import os
import sys
import csv
import logging

# Add parent directory to path to import scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import MarkPositionScraperAsync

# Disable logging for tests
logging.disable(logging.CRITICAL)

class TestCSVInjection(unittest.TestCase):
    def setUp(self):
        self.json_file = "test_links.json"
        self.csv_file = "test_links.csv"
        self.txt_file = "test_links.txt"
        self.scraper = MarkPositionScraperAsync(
            output_json=self.json_file,
            output_csv=self.csv_file,
            output_txt=self.txt_file
        )

    def tearDown(self):
        for f in [self.json_file, self.csv_file, self.txt_file]:
            if os.path.exists(f):
                os.remove(f)

    def test_csv_sanitization(self):
        """Test that fields starting with special characters are sanitized in CSV."""
        malicious_data = [
            {
                'title': '=cmd|/C calc',
                'date': '+2023-01-01',
                'author': '@hacker',
                'categories': ['-bad_category'],
                'external_link': '=http://evil.com',
                'domain': '+evil.com',
                'post_url': '@http://wordpress.com'
            }
        ]

        self.scraper.save_data(malicious_data)

        self.assertTrue(os.path.exists(self.csv_file), "CSV file was not created")

        with open(self.csv_file, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader) # Skip headers
            row = next(reader)

            # Helper to check sanitization
            def check_sanitization(field_value, field_name):
                self.assertTrue(
                    field_value.startswith("'"),
                    f"{field_name} was not sanitized. Value: {field_value}"
                )
                self.assertFalse(
                    field_value.startswith("''"),
                    f"{field_name} was double sanitized. Value: {field_value}"
                )

            # Check all fields
            # Row structure: Title, Date, Author, Categories, External Link, Domain, Post URL
            check_sanitization(row[0], "Title")
            check_sanitization(row[1], "Date")
            check_sanitization(row[2], "Author")
            check_sanitization(row[3], "Categories")
            check_sanitization(row[4], "External Link")
            check_sanitization(row[5], "Domain")
            check_sanitization(row[6], "Post URL")

if __name__ == '__main__':
    unittest.main()
