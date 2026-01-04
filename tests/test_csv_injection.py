import unittest
import csv
import os
import json
from scraper import MarkPositionScraperAsync

class TestCSVInjection(unittest.TestCase):
    def setUp(self):
        self.output_json = "test_links.json"
        self.output_csv = "test_links.csv"
        self.output_txt = "test_unique_links.txt"
        self.scraper = MarkPositionScraperAsync(self.output_json, self.output_csv, self.output_txt)

    def tearDown(self):
        if os.path.exists(self.output_json):
            os.remove(self.output_json)
        if os.path.exists(self.output_csv):
            os.remove(self.output_csv)
        if os.path.exists(self.output_txt):
            os.remove(self.output_txt)

    def test_csv_injection(self):
        # Create data with potential CSV injection payloads
        malicious_data = [
            {
                'title': '=1+1', # Excel formula
                'date': '2023-10-27',
                'author': '@attacker', # Could trigger something
                'categories': ['+category'],
                'external_link': '-http://evil.com',
                'domain': 'evil.com',
                'post_url': 'http://example.com/post'
            }
        ]

        # Save data
        self.scraper.save_data(malicious_data)

        # Read CSV and verify if injection characters are preserved or sanitized
        with open(self.output_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader) # Skip header
            row = next(reader)

            # Currently (before fix), these should start with the malicious chars
            # After fix, they should be prefixed with '

            print(f"Row data: {row}")

            # Check Title
            # If sanitized, it should start with "'" or similar escaping mechanism.
            # If not sanitized, it starts with "="
            if row[0].startswith("="):
                print("VULNERABILITY CONFIRMED: Title starts with =")
            else:
                print(f"Title sanitized? {row[0]}")

            # Ideally we want this test to FAIL if it is NOT sanitized (or we use it to confirm the bug first)
            # But let's write assertions for the DESIRED state (secure)

            self.assertFalse(row[0].startswith("="), "Title should be sanitized")
            self.assertTrue(row[0].startswith("'="), "Title should have leading quote")

            self.assertFalse(row[2].startswith("@"), "Author should be sanitized")
            self.assertTrue(row[2].startswith("'@"), "Author should have leading quote")

if __name__ == '__main__':
    unittest.main()
