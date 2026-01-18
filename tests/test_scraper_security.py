import unittest
import csv
import os
import sys

# Add parent directory to path so we can import scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import MarkPositionScraperAsync

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        self.json_file = "test_sec_links.json"
        self.csv_file = "test_sec_links.csv"
        self.txt_file = "test_sec_unique.txt"
        self.scraper = MarkPositionScraperAsync(self.json_file, self.csv_file, self.txt_file)

    def tearDown(self):
        for f in [self.json_file, self.csv_file, self.txt_file]:
            if os.path.exists(f):
                os.remove(f)

    def test_csv_injection_prevention(self):
        malicious_data = [
            {
                "title": "=cmd|' /C calc'!A0",
                "date": "2023-01-01",
                "author": "+@malicious",
                "categories": ["-Normal", "@Bad"],
                "external_link": "http://example.com",
                "domain": "example.com",
                "post_url": "http://example.com/post"
            }
        ]

        self.scraper.save_data(malicious_data)

        with open(self.csv_file, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader) # skip header
            row = next(reader)

            # Verify fields are escaped
            self.assertTrue(row[0].startswith("'="), "Title not escaped")
            self.assertTrue(row[2].startswith("'+"), "Author not escaped")
            # Categories are joined by ", ", so it starts with -Normal...
            self.assertTrue(row[3].startswith("'-"), "Categories not escaped")

if __name__ == '__main__':
    unittest.main()
