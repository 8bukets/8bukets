import unittest
import os
import csv
from scraper import MarkPositionScraperAsync

class TestSecurity(unittest.TestCase):
    def setUp(self):
        self.output_json = "test_links.json"
        self.output_csv = "test_links.csv"
        self.output_txt = "test_links.txt"

        # Clean up
        for f in [self.output_json, self.output_csv, self.output_txt]:
            if os.path.exists(f):
                os.remove(f)

    def tearDown(self):
        # Clean up
        for f in [self.output_json, self.output_csv, self.output_txt]:
            if os.path.exists(f):
                os.remove(f)

    def test_csv_injection_prevention(self):
        """Test that malicious inputs are sanitized in CSV output."""
        scraper = MarkPositionScraperAsync(self.output_json, self.output_csv, self.output_txt)

        malicious_data = [
            {
                'title': '=SUM(1+1)',
                'date': '+2023-01-01',
                'author': '-BadActor',
                'categories': ['@Category'],
                'external_link': 'http://example.com',
                'domain': 'example.com',
                'post_url': 'http://wordpress.com/post'
            }
        ]

        scraper.save_data(malicious_data)

        # Check CSV content
        with open(self.output_csv, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)

            self.assertEqual(row[0], "'=SUM(1+1)", "Title should be sanitized")
            self.assertEqual(row[1], "'+2023-01-01", "Date should be sanitized")
            self.assertEqual(row[2], "'-BadActor", "Author should be sanitized")
            # Categories are joined, so the first char of the string matters.
            # " ".join(['@Category']) -> "@Category"
            self.assertEqual(row[3], "'@Category", "Categories should be sanitized")

if __name__ == "__main__":
    unittest.main()
