import unittest
import os
import csv
from scraper import MarkPositionScraperAsync

class TestSecurity(unittest.TestCase):
    def setUp(self):
        self.output_json = 'test_sec_links.json'
        self.output_csv = 'test_sec_links.csv'
        self.output_txt = 'test_sec_unique_links.txt'
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

    def test_sanitize_for_csv(self):
        # Test basic cases
        self.assertEqual(self.scraper.sanitize_for_csv("=cmd"), "'=cmd")
        self.assertEqual(self.scraper.sanitize_for_csv("+cmd"), "'+cmd")
        self.assertEqual(self.scraper.sanitize_for_csv("-cmd"), "'-cmd")
        self.assertEqual(self.scraper.sanitize_for_csv("@cmd"), "'@cmd")

        # Test safe cases
        self.assertEqual(self.scraper.sanitize_for_csv("safe"), "safe")
        self.assertEqual(self.scraper.sanitize_for_csv("123"), "123")
        self.assertEqual(self.scraper.sanitize_for_csv(""), "")
        self.assertEqual(self.scraper.sanitize_for_csv(None), "")

        # Test whitespace handling (should still sanitize if stripped version starts with dangerous char)
        self.assertEqual(self.scraper.sanitize_for_csv("  =cmd"), "'  =cmd")

    def test_save_data_sanitization(self):
        malicious_post = {
            'title': '=cmd',
            'date': '+date',
            'author': '-author',
            'categories': ['@cat'],
            'external_link': '=http://evil.com',
            'domain': '+evil.com',
            'post_url': '-http://wordpress.com'
        }

        self.scraper.save_data([malicious_post])

        with open(self.output_csv, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            row = next(reader)

            self.assertEqual(row['Title'], "'=cmd")
            self.assertEqual(row['Date'], "'+date")
            self.assertEqual(row['Author'], "'-author")
            self.assertEqual(row['Categories'], "'@cat")
            self.assertEqual(row['External Link'], "'=http://evil.com")
            self.assertEqual(row['Domain'], "'+evil.com")
            self.assertEqual(row['Post URL'], "'-http://wordpress.com")

if __name__ == '__main__':
    unittest.main()
