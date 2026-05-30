import unittest
import os
import csv
import sys

# Add parent directory to path so we can import scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import MarkPositionScraperAsync

class TestCSVInjection(unittest.TestCase):
    def setUp(self):
        self.output_json = "test_output.json"
        self.output_csv = "test_output.csv"
        self.output_txt = "test_output.txt"
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
        # malicious data
        posts = [
            {
                'title': '=cmd|/C calc!A0',
                'date': '2023-01-01',
                'author': '+Malicious',
                'categories': ['@Category'],
                'external_link': '-http://evil.com',
                'domain': 'evil.com',
                'post_url': 'http://example.com'
            }
        ]

        self.scraper.save_data(posts)

        with open(self.output_csv, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)

            # Index 0: Title
            self.assertTrue(row[0].startswith("'"), f"Title not sanitized: {row[0]}")
            # Index 2: Author
            self.assertTrue(row[2].startswith("'"), f"Author not sanitized: {row[2]}")
            # Index 3: Categories
            self.assertTrue(row[3].startswith("'"), f"Categories not sanitized: {row[3]}")
            # Index 4: External Link
            self.assertTrue(row[4].startswith("'"), f"External Link not sanitized: {row[4]}")

if __name__ == '__main__':
    unittest.main()
