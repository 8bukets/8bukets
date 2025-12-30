import unittest
import csv
import os
from scraper import MarkPositionScraperAsync

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        self.output_csv = "test_security.csv"
        self.scraper = MarkPositionScraperAsync(
            output_json="test.json",
            output_csv=self.output_csv,
            output_txt="test.txt"
        )

    def tearDown(self):
        if os.path.exists(self.output_csv):
            os.remove(self.output_csv)
        if os.path.exists("test.json"):
            os.remove("test.json")
        if os.path.exists("test.txt"):
            os.remove("test.txt")

    def test_csv_injection_prevention(self):
        # Data with potential CSV injection payloads
        posts = [
            {
                'title': '=cmd|/C calc.exe!A0',
                'date': '2023-01-01',
                'author': '+Hacker',
                'categories': ['-BadCategory'],
                'external_link': '@http://evil.com',
                'domain': 'evil.com',
                'post_url': 'http://example.com'
            }
        ]

        # Save data using the scraper
        self.scraper.save_data(posts)

        # Read back and verify sanitization
        with open(self.output_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader)
            row = next(reader)

            # Check Title
            self.assertTrue(row[0].startswith("'="), f"Title not sanitized: {row[0]}")
            # Check Author
            self.assertTrue(row[2].startswith("'+"), f"Author not sanitized: {row[2]}")
            # Check Categories (joined string)
            self.assertTrue(row[3].startswith("'-"), f"Categories not sanitized: {row[3]}")
            # Check External Link
            self.assertTrue(row[4].startswith("'@"), f"External Link not sanitized: {row[4]}")

if __name__ == '__main__':
    unittest.main()
