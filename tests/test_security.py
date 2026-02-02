import unittest
import os
import csv
import sys
from unittest.mock import MagicMock

# Add root directory to path to allow importing scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import MarkPositionScraperAsync

class TestSecurity(unittest.TestCase):
    def setUp(self):
        self.output_csv = 'test_security_output.csv'
        # Dummy files for json/txt as we won't check them
        self.output_json = 'test_security_output.json'
        self.output_txt = 'test_security_output.txt'

        self.scraper = MarkPositionScraperAsync(
            output_json=self.output_json,
            output_csv=self.output_csv,
            output_txt=self.output_txt
        )

    def tearDown(self):
        for f in [self.output_csv, self.output_json, self.output_txt]:
            if os.path.exists(f):
                os.remove(f)

    def test_csv_injection_prevention(self):
        """
        Test that fields starting with =, +, -, @ are sanitized in CSV output.
        """
        malicious_posts = [
            {
                'title': '=cmd|/C calc!A0',
                'date': '+2023-01-01',
                'author': '-Malicious Author',
                'categories': ['@Category'],
                'external_link': 'http://example.com',
                'domain': 'example.com',
                'post_url': 'http://example.com/post'
            }
        ]

        self.scraper.save_data(malicious_posts)

        with open(self.output_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader) # Skip header
            row = next(reader)

            # Check Title
            self.assertTrue(row[0].startswith("'"), f"Title not sanitized: {row[0]}")
            self.assertEqual(row[0], "'=cmd|/C calc!A0")

            # Check Date
            self.assertTrue(row[1].startswith("'"), f"Date not sanitized: {row[1]}")
            self.assertEqual(row[1], "'+2023-01-01")

            # Check Author
            self.assertTrue(row[2].startswith("'"), f"Author not sanitized: {row[2]}")
            self.assertEqual(row[2], "'-Malicious Author")

            # Check Categories (joined by comma, but the start should be sanitized if the first cat is malicious)
            # In my test data, categories is list.
            # The code does: ", ".join(post.get('categories', []))
            # If the first category starts with @, the joined string starts with @.
            self.assertTrue(row[3].startswith("'"), f"Categories not sanitized: {row[3]}")
            self.assertEqual(row[3], "'@Category")

if __name__ == '__main__':
    unittest.main()
