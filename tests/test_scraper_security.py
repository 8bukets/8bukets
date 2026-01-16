import unittest
import csv
import os
import json
from scraper import MarkPositionScraperAsync

class TestScraperSecurity(unittest.TestCase):
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
        for f in [self.output_json, self.output_csv, self.output_txt]:
            if os.path.exists(f):
                os.remove(f)

    def test_csv_injection_prevention(self):
        malicious_data = [
            {
                "title": "=cmd|' /C calc'!A0",
                "date": "+2023-01-01",
                "author": "@attacker",
                "categories": ["-malicious"],
                "external_link": "http://normal.com",
                "domain": "normal.com",
                "post_url": "http://example.com/post"
            }
        ]

        self.scraper.save_data(malicious_data)

        with open(self.output_csv, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)

            # Check title (starts with =)
            self.assertTrue(row[0].startswith("'="), f"Title not sanitized: {row[0]}")

            # Check date (starts with +)
            self.assertTrue(row[1].startswith("'+"), f"Date not sanitized: {row[1]}")

            # Check author (starts with @)
            self.assertTrue(row[2].startswith("'@"), f"Author not sanitized: {row[2]}")

            # Check categories (starts with -)
            self.assertTrue(row[3].startswith("'-"), f"Categories not sanitized: {row[3]}")

if __name__ == '__main__':
    unittest.main()
