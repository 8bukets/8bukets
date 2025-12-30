import unittest
import csv
import os
import sys

# Add parent directory to path to allow importing scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import OracleNewsScraper

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        self.output_json = 'test_security_links.json'
        self.output_csv = 'test_security_links.csv'
        self.output_txt = 'test_security_unique_links.txt'
        self.scraper = OracleNewsScraper(
            output_json=self.output_json,
            output_csv=self.output_csv,
            output_txt=self.output_txt
        )

    def tearDown(self):
        for f in [self.output_json, self.output_csv, self.output_txt]:
            if os.path.exists(f):
                os.remove(f)

    def test_sanitize_for_csv(self):
        """Test that dangerous characters are escaped."""
        # Test dangerous prefixes
        self.assertEqual(self.scraper.sanitize_for_csv("=1+1"), "'=1+1")
        self.assertEqual(self.scraper.sanitize_for_csv("+1+1"), "'+1+1")
        self.assertEqual(self.scraper.sanitize_for_csv("-1+1"), "'-1+1")
        self.assertEqual(self.scraper.sanitize_for_csv("@SUM(1,1)"), "'@SUM(1,1)")

        # Test benign strings
        self.assertEqual(self.scraper.sanitize_for_csv("Normal text"), "Normal text")
        self.assertEqual(self.scraper.sanitize_for_csv("Title = Something"), "Title = Something")

        # Test non-string inputs
        self.assertEqual(self.scraper.sanitize_for_csv(None), None)
        self.assertEqual(self.scraper.sanitize_for_csv(123), 123)

    def test_save_data_sanitization(self):
        """Test that data written to CSV is actually sanitized."""
        posts = [{
            'title': '=cmd|/C calc',
            'date': 'Oct 15',
            'author': '+Hacker',
            'categories': ['@News'],
            'external_link': '-http://evil.com',
            'domain': 'evil.com',
            'post_url': 'http://evil.com'
        }]

        self.scraper.save_data(posts)

        with open(self.output_csv, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader)
            row = next(reader)

            # Check Title
            self.assertEqual(row[0], "'=cmd|/C calc")
            # Check Author
            self.assertEqual(row[2], "'+Hacker")
            # Check Categories
            self.assertEqual(row[3], "'@News")
            # Check External Link
            self.assertEqual(row[4], "'-http://evil.com")

if __name__ == '__main__':
    unittest.main()
