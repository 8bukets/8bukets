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
        # Malicious data
        malicious_posts = [
            {
                'title': '=1+1',
                'date': '2023-10-27',
                'author': '@attacker',
                'categories': ['+category'],
                'external_link': '-http://evil.com',
                'domain': 'evil.com',
                'post_url': 'http://example.com/post'
            }
        ]

        # Save data
        self.scraper.save_data(malicious_posts)

        # Read CSV and check for injection
        with open(self.output_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader) # Skip header
            row = next(reader)

            title = row[0]
            author = row[2]
            categories = row[3]
            external_link = row[4]

            print(f"Title: {title}")
            print(f"Author: {author}")
            print(f"Categories: {categories}")
            print(f"External Link: {external_link}")

            self.assertTrue(title.startswith("'="), "Title should be sanitized")
            self.assertTrue(author.startswith("'@"), "Author should be sanitized")
            self.assertTrue(categories.startswith("'+"), "Categories should be sanitized")
            self.assertTrue(external_link.startswith("'-"), "External Link should be sanitized")

if __name__ == '__main__':
    unittest.main()
