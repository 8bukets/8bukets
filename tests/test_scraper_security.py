import unittest
import os
import csv
import json
from scraper import MarkPositionScraperAsync

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        self.output_json = "test_security.json"
        self.output_csv = "test_security.csv"
        self.output_txt = "test_security.txt"
        self.scraper = MarkPositionScraperAsync(self.output_json, self.output_csv, self.output_txt)

    def tearDown(self):
        if os.path.exists(self.output_json):
            os.remove(self.output_json)
        if os.path.exists(self.output_csv):
            os.remove(self.output_csv)
        if os.path.exists(self.output_txt):
            os.remove(self.output_txt)

    def test_csv_injection_sanitization(self):
        """Test that CSV injection characters are sanitized."""
        malicious_inputs = [
            "=cmd|' /C calc'!A0",
            "+malicious",
            "-subtraction",
            "@function"
        ]

        for inp in malicious_inputs:
            sanitized = self.scraper.sanitize_for_csv(inp)
            self.assertTrue(sanitized.startswith("'"), f"Input '{inp}' was not sanitized. Got: '{sanitized}'")
            self.assertEqual(sanitized[1:], inp)

    def test_normal_input_not_sanitized(self):
        """Test that normal inputs are not sanitized."""
        normal_inputs = [
            "Normal Title",
            "12345",
            "http://example.com"
        ]
        for inp in normal_inputs:
            sanitized = self.scraper.sanitize_for_csv(inp)
            self.assertEqual(sanitized, inp, f"Normal input '{inp}' was wrongly sanitized.")

    def test_save_data_sanitization(self):
        """Test that save_data actually applies sanitization."""
        malicious_data = [
            {
                "title": "=bad",
                "date": "+2023",
                "author": "@hacker",
                "categories": ["-category"],
                "external_link": "=http://evil.com",
                "domain": "evil.com",
                "post_url": "http://example.com"
            }
        ]

        self.scraper.save_data(malicious_data)

        with open(self.output_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)

            # Row structure: Title, Date, Author, Categories, External Link, Domain, Post URL
            self.assertTrue(row[0].startswith("'=bad"))
            self.assertTrue(row[1].startswith("'+2023"))
            self.assertTrue(row[2].startswith("'@hacker"))
            self.assertTrue(row[3].startswith("'-category"))
            self.assertTrue(row[4].startswith("'=http://evil.com"))

if __name__ == '__main__':
    unittest.main()
