import unittest
import sys
import os
import csv
import shutil
from unittest.mock import MagicMock

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import MarkPositionScraperAsync

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        self.output_json = "test_output.json"
        self.output_csv = "test_output.csv"
        self.output_txt = "test_output.txt"
        self.scraper = MarkPositionScraperAsync(self.output_json, self.output_csv, self.output_txt)

    def tearDown(self):
        for f in [self.output_json, self.output_csv, self.output_txt]:
            if os.path.exists(f):
                os.remove(f)

    def test_csv_injection_mitigation(self):
        """Test that potential CSV injection payloads are sanitized."""
        malicious_posts = [
            {
                'title': '=1+1',
                'date': '@2023',
                'author': '+Hacker',
                'categories': ['-Category'],
                'external_link': '=cmd|/C calc!A0',
                'domain': 'example.com',
                'post_url': 'http://example.com'
            }
        ]

        self.scraper.save_data(malicious_posts)

        with open(self.output_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader) # Skip header
            row = next(reader)

            # Row structure: ['Title', 'Date', 'Author', 'Categories', 'External Link', 'Domain', 'Post URL']

            # Check Title
            self.assertTrue(row[0].startswith("'"), f"Title not sanitized: {row[0]}")
            self.assertEqual(row[0], "'=1+1")

            # Check Date
            self.assertTrue(row[1].startswith("'"), f"Date not sanitized: {row[1]}")
            self.assertEqual(row[1], "'@2023")

            # Check Author
            self.assertTrue(row[2].startswith("'"), f"Author not sanitized: {row[2]}")
            self.assertEqual(row[2], "'+Hacker")

            # Check Categories (joined by ", ")
            # The sanitizer might be applied to the string as a whole or individual items?
            # The code joins then writes. Ideally we sanitize the result string.
            self.assertTrue(row[3].startswith("'"), f"Categories not sanitized: {row[3]}")
            self.assertEqual(row[3], "'-Category")

            # Check External Link
            self.assertTrue(row[4].startswith("'"), f"External Link not sanitized: {row[4]}")

if __name__ == '__main__':
    unittest.main()
