import unittest
import os
import csv
from scraper import OracleNewsScraper

class TestCSVInjection(unittest.TestCase):
    def setUp(self):
        self.output_json = "test_links.json"
        self.output_csv = "test_links.csv"
        self.output_txt = "test_unique_links.txt"
        self.scraper = OracleNewsScraper(self.output_json, self.output_csv, self.output_txt)

    def tearDown(self):
        if os.path.exists(self.output_json):
            os.remove(self.output_json)
        if os.path.exists(self.output_csv):
            os.remove(self.output_csv)
        if os.path.exists(self.output_txt):
            os.remove(self.output_txt)

    def test_csv_injection_prevention(self):
        # Malicious data
        posts = [
            {
                "title": "=cmd|' /C calc'!A0",
                "date": "Oct 15, 2025",
                "author": "+@bad",
                "categories": ["-News"],
                "external_link": "http://evil.com",
                "domain": "oracle.com",
                "post_url": "http://oracle.com/news"
            }
        ]

        self.scraper.save_data(posts)

        with open(self.output_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)

            # Check Title
            # Expecting the value to be sanitized with a single quote prefix
            self.assertEqual(row[0], "'=cmd|' /C calc'!A0", f"Title not sanitized: {row[0]}")

            # Check Author
            self.assertEqual(row[2], "'+@bad", f"Author not sanitized: {row[2]}")

            # Check Categories
            # "-News" -> "'-News"
            self.assertEqual(row[3], "'-News", f"Categories not sanitized: {row[3]}")
