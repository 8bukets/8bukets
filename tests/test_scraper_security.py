import unittest
import csv
import os
import sys

# Add parent directory to path to import scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import MarkPositionScraperAsync

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        self.output_csv = "test_security_output.csv"
        self.scraper = MarkPositionScraperAsync(
            output_json="dummy.json",
            output_csv=self.output_csv,
            output_txt="dummy.txt"
        )

    def tearDown(self):
        if os.path.exists(self.output_csv):
            os.remove(self.output_csv)
        if os.path.exists("dummy.json"):
            os.remove("dummy.json")
        if os.path.exists("dummy.txt"):
            os.remove("dummy.txt")

    def test_sanitize_for_csv(self):
        """Test the sanitize_for_csv method directly."""
        self.assertEqual(self.scraper.sanitize_for_csv("=1+1"), "'=1+1")
        self.assertEqual(self.scraper.sanitize_for_csv("+cmd"), "'+cmd")
        self.assertEqual(self.scraper.sanitize_for_csv("-minus"), "'-minus")
        self.assertEqual(self.scraper.sanitize_for_csv("@sum"), "'@sum")
        self.assertEqual(self.scraper.sanitize_for_csv("Normal text"), "Normal text")
        self.assertEqual(self.scraper.sanitize_for_csv(None), "")
        self.assertEqual(self.scraper.sanitize_for_csv(""), "")

    def test_csv_injection_in_file(self):
        """Test that malicious data is sanitized when writing to CSV."""
        malicious_data = [{
            'title': '=cmd|/C calc',
            'date': '2023-01-01',
            'author': 'User',
            'categories': ['News'],
            'external_link': 'http://example.com',
            'domain': 'example.com',
            'post_url': 'http://example.com/post'
        }]

        self.scraper.save_data(malicious_data)

        with open(self.output_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader) # Header
            row = next(reader)

            # Title is first column
            self.assertEqual(row[0], "'=cmd|/C calc")

if __name__ == '__main__':
    unittest.main()
