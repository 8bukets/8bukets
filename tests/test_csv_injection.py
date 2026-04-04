import unittest
import os
import csv
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

    def test_csv_injection(self):
        # Data with malicious payload
        malicious_data = [{
            'title': '=cmd|/c calc!A0',
            'date': '2023-01-01',
            'author': '@attacker',
            'categories': ['+news'],
            'external_link': '-http://evil.com',
            'domain': 'evil.com',
            'post_url': 'http://example.com'
        }]

        with open(self.output_json, 'w', encoding='utf-8') as json_f, \
             open(self.output_csv, 'w', newline='', encoding='utf-8') as csv_f, \
             open(self.output_txt, 'w', encoding='utf-8') as txt_f:

            csv_writer = csv.writer(csv_f)
            self.scraper.save_batch(malicious_data, json_f, csv_writer, txt_f, set(), True)

        # Read the CSV back
        with open(self.output_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            row = next(reader)

            # Check if payloads are sanitized (they SHOULD be now)
            self.assertEqual(row[0], "'=cmd|/c calc!A0")
            self.assertEqual(row[2], "'@attacker")
            # categories are joined by ", "
            self.assertIn("'+news", row[3])
            self.assertEqual(row[4], "'-http://evil.com")

if __name__ == '__main__':
    unittest.main()
