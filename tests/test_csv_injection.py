import unittest
import csv
import os
import json
import asyncio
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

    def test_csv_injection_prevention(self):
        # Data with potential CSV injection payloads
        malicious_posts = [
            {
                'title': '=1+1',  # Formula injection
                'date': '2023-01-01',
                'author': '@SUM(1,1)', # Formula injection
                'categories': ['-10'], # Formula injection
                'external_link': '+1', # Formula injection
                'domain': 'example.com',
                'post_url': 'http://example.com'
            }
        ]

        # Save data
        self.scraper.save_data(malicious_posts)

        # Read back and verify sanitization
        with open(self.output_csv, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader)
            row = next(reader)

            # Map headers to indices
            header_map = {h: i for i, h in enumerate(headers)}

            title = row[header_map['Title']]
            author = row[header_map['Author']]
            categories = row[header_map['Categories']]
            link = row[header_map['External Link']]

            # Check that dangerous characters are escaped with a single quote
            self.assertTrue(title.startswith("'"), f"Title '{title}' should be sanitized")
            self.assertTrue(author.startswith("'"), f"Author '{author}' should be sanitized")
            self.assertTrue(categories.startswith("'"), f"Categories '{categories}' should be sanitized")
            self.assertTrue(link.startswith("'"), f"Link '{link}' should be sanitized")

if __name__ == '__main__':
    unittest.main()
