import unittest
import os
import sys
import csv

# Add parent directory to path to import scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import MarkPositionScraperAsync

class TestCSVSecurity(unittest.TestCase):
    def setUp(self):
        self.output_json = "test_security.json"
        self.output_csv = "test_security.csv"
        self.output_txt = "test_security.txt"
        self.scraper = MarkPositionScraperAsync(
            output_json=self.output_json,
            output_csv=self.output_csv,
            output_txt=self.output_txt
        )

    def tearDown(self):
        for f in [self.output_json, self.output_csv, self.output_txt]:
            if os.path.exists(f):
                os.remove(f)

    def test_csv_injection_prevention(self):
        malicious_posts = [
            {
                'title': '=cmd|/C calc!A0',
                'date': '+2023-01-01',
                'author': '@attacker',
                'categories': ['-badcategory'],
                'external_link': 'http://evil.com',
                'domain': 'evil.com',
                'post_url': 'http://example.com'
            }
        ]

        self.scraper.save_data(malicious_posts)

        with open(self.output_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)

            # Check Title
            self.assertTrue(row[0].startswith("'="), f"Title not sanitized: {row[0]}")
            # Check Date
            self.assertTrue(row[1].startswith("'+"), f"Date not sanitized: {row[1]}")
            # Check Author
            self.assertTrue(row[2].startswith("'@"), f"Author not sanitized: {row[2]}")
            # Check Categories (first one)
            self.assertTrue(row[3].startswith("'-"), f"Categories not sanitized: {row[3]}")

if __name__ == '__main__':
    unittest.main()
