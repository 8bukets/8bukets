import unittest
import os
import csv
from scraper import MarkPositionScraperAsync

class TestSecurity(unittest.TestCase):
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
        malicious_posts = [
            {
                'title': '=cmd|/C calc!A0',
                'date': '+2023-01-01',
                'author': '@attacker',
                'categories': ['-category'],
                'external_link': 'http://example.com',
                'domain': 'example.com',
                'post_url': 'http://wordpress.com/post'
            }
        ]

        self.scraper.save_data(malicious_posts)

        with open(self.output_csv, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader) # Skip header
            try:
                row = next(reader)
            except StopIteration:
                self.fail("CSV file is empty")

            # Check Title
            self.assertTrue(row[0].startswith("'="), f"Title not sanitized: {row[0]}")
            # Check Date
            self.assertTrue(row[1].startswith("'+"), f"Date not sanitized: {row[1]}")
            # Check Author
            self.assertTrue(row[2].startswith("'@"), f"Author not sanitized: {row[2]}")
            # Check Categories (it joins them, so likely starts with the first one)
            self.assertTrue(row[3].startswith("'-"), f"Categories not sanitized: {row[3]}")

if __name__ == '__main__':
    unittest.main()
