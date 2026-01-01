import unittest
import csv
import os
import json
from scraper import MarkPositionScraperAsync

class TestSecurity(unittest.TestCase):
    def setUp(self):
        self.output_json = "test_links.json"
        self.output_csv = "test_links.csv"
        self.output_txt = "test_unique_links.txt"
        self.scraper = MarkPositionScraperAsync(self.output_json, self.output_csv, self.output_txt)

    def tearDown(self):
        for f in [self.output_json, self.output_csv, self.output_txt]:
            if os.path.exists(f):
                os.remove(f)

    def test_csv_injection_sanitization(self):
        """Test that CSV injection payloads are sanitized."""
        malicious_data = [
            {
                'title': '=SUM(1+1)',
                'date': '2023-01-01',
                'author': '@attacker',
                'categories': ['+bad_category'],
                'external_link': '-http://evil.com',
                'domain': 'evil.com',
                'post_url': 'http://example.com'
            }
        ]

        self.scraper.save_data(malicious_data)

        with open(self.output_csv, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)

            # Verify sanitization
            self.assertTrue(row[0].startswith("'="), "Title not sanitized")
            self.assertTrue(row[2].startswith("'@"), "Author not sanitized")
            self.assertTrue(row[3].startswith("'+"), "Categories not sanitized")
            self.assertTrue(row[4].startswith("'-"), "External Link not sanitized")

            # Verify non-malicious fields are untouched
            self.assertEqual(row[1], '2023-01-01', "Date modified unnecessarily")
            self.assertEqual(row[5], 'evil.com', "Domain modified unnecessarily")

    def test_sanitize_for_csv_method(self):
        """Unit test for sanitize_for_csv method."""
        self.assertEqual(self.scraper.sanitize_for_csv("=cmd|' /C calc'!A0"), "'=cmd|' /C calc'!A0")
        self.assertEqual(self.scraper.sanitize_for_csv("+123"), "'+123")
        self.assertEqual(self.scraper.sanitize_for_csv("-123"), "'-123")
        self.assertEqual(self.scraper.sanitize_for_csv("@echo"), "'@echo")
        self.assertEqual(self.scraper.sanitize_for_csv("Normal Text"), "Normal Text")
        self.assertEqual(self.scraper.sanitize_for_csv(""), "")
        self.assertEqual(self.scraper.sanitize_for_csv(None), None)

if __name__ == '__main__':
    unittest.main()
