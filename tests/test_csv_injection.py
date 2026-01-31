import unittest
import os
import csv
import logging
from scraper import MarkPositionScraperAsync

# Disable logging for tests
logging.disable(logging.CRITICAL)

class TestCsvInjection(unittest.TestCase):
    def test_csv_injection(self):
        output_json = "test_output.json"
        output_csv = "test_output.csv"
        output_txt = "test_output.txt"

        scraper = MarkPositionScraperAsync(output_json, output_csv, output_txt)
        malicious_data = [{
            'title': '=cmd|/c calc!A0',
            'date': '2023-01-01',
            'author': '@attacker',
            'categories': ['+News', 'Normal'],
            'external_link': '-http://evil.com',
            'domain': 'evil.com',
            'post_url': 'http://example.com'
        }]

        scraper.save_data(malicious_data)

        with open(output_csv, "r", newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader)
            row = next(reader)

            # Check Title
            self.assertTrue(row[0].startswith("'="), f"Title not sanitized: {row[0]}")
            # Check Author
            self.assertTrue(row[2].startswith("'@"), f"Author not sanitized: {row[2]}")
            # Check Categories (joined string should start with '+')
            # The categories are joined by ", ". If the first one starts with +, the whole string starts with +
            self.assertTrue(row[3].startswith("'+"), f"Categories not sanitized: {row[3]}")
            # Check External Link
            self.assertTrue(row[4].startswith("'-"), f"External Link not sanitized: {row[4]}")

    def tearDown(self):
        for f in ["test_output.json", "test_output.csv", "test_output.txt"]:
            if os.path.exists(f):
                os.remove(f)

if __name__ == '__main__':
    unittest.main()
