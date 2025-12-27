
import csv
import os
import unittest
from scraper import MarkPositionScraperAsync

class TestCSVInjection(unittest.TestCase):
    def setUp(self):
        self.output_csv = "test_links.csv"
        self.output_json = "test_links.json"
        self.output_txt = "test_unique_links.txt"
        self.scraper = MarkPositionScraperAsync(
            output_json=self.output_json,
            output_csv=self.output_csv,
            output_txt=self.output_txt,
            max_pages=1,
            concurrency=1
        )

    def tearDown(self):
        for f in [self.output_csv, self.output_json, self.output_txt]:
            if os.path.exists(f):
                os.remove(f)

    def test_csv_injection_prevention(self):
        # Malicious data
        posts = [{
            'title': '=cmd|/c calc!A0',
            'date': '2023-01-01',
            'author': '@SUM(1+1)',
            'categories': ['+News'],
            'external_link': '-http://evil.com',
            'domain': 'evil.com',
            'post_url': 'http://example.com'
        }]

        self.scraper.save_data(posts)

        with open(self.output_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)

            # Expect sanitized output
            self.assertEqual(row[0], "'=cmd|/c calc!A0", "Title should be sanitized")
            self.assertEqual(row[2], "'@SUM(1+1)", "Author should be sanitized")
            self.assertEqual(row[3], "'+News", "Categories should be sanitized")
            self.assertEqual(row[4], "'-http://evil.com", "External Link should be sanitized")

if __name__ == "__main__":
    unittest.main()
