import unittest
import os
import csv
import sys

# Add parent directory to path to import scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import MarkPositionScraperAsync

class TestCSVInjection(unittest.TestCase):
    def setUp(self):
        self.output_json = "test_links.json"
        self.output_csv = "test_links.csv"
        self.output_txt = "test_unique_links.txt"
        self.scraper = MarkPositionScraperAsync(
            output_json=self.output_json,
            output_csv=self.output_csv,
            output_txt=self.output_txt
        )

    def tearDown(self):
        if os.path.exists(self.output_json):
            os.remove(self.output_json)
        if os.path.exists(self.output_csv):
            os.remove(self.output_csv)
        if os.path.exists(self.output_txt):
            os.remove(self.output_txt)

    def test_csv_injection_prevention(self):
        # Malicious data
        malicious_posts = [
            {
                'title': '=cmd|/C calc!A0',
                'date': '+2023-01-01',
                'author': '-Author',
                'categories': ['@Category'],
                'external_link': '=http://evil.com',
                'domain': '+evil.com',
                'post_url': '-http://wordpress.com/post'
            }
        ]

        self.scraper.save_data(malicious_posts)

        with open(self.output_csv, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader) # Skip header
            row = next(reader)

            # Check Title
            self.assertTrue(row[0].startswith("'"), f"Title not sanitized: {row[0]}")
            self.assertEqual(row[0], "'=cmd|/C calc!A0")

            # Check Date
            self.assertTrue(row[1].startswith("'"), f"Date not sanitized: {row[1]}")

            # Check Author
            self.assertTrue(row[2].startswith("'"), f"Author not sanitized: {row[2]}")

            # Check Categories
            # Categories are joined by ", ". If the first one starts with dangerous char...
            self.assertTrue(row[3].startswith("'"), f"Categories not sanitized: {row[3]}")

if __name__ == '__main__':
    unittest.main()
