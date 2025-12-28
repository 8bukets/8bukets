import unittest
import csv
import os
from scraper import MarkPositionScraperAsync

class TestCSVInjection(unittest.TestCase):
    def test_csv_injection_prevention(self):
        # Create a mock scraper instance
        scraper = MarkPositionScraperAsync("test_links.json", "test_links.csv", "test_unique_links.txt")

        # Malicious data
        malicious_posts = [
            {
                'title': '=1+1',
                'date': '2023-01-01',
                'author': '@attacker',
                'categories': ['+category'],
                'external_link': '-http://example.com',
                'domain': 'example.com',
                'post_url': 'http://example.com/post'
            }
        ]

        # Save data
        scraper.save_data(malicious_posts)

        # Read the CSV and check for sanitization (expecting single quote prefix)
        with open("test_links.csv", 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader)
            row = next(reader)

            # Helper to check if value is sanitized
            def is_sanitized(val):
                return val.startswith("'")

            # Check fields that started with dangerous characters
            # Title: =1+1
            self.assertTrue(is_sanitized(row[0]), f"Title not sanitized: {row[0]}")
            # Author: @attacker
            self.assertTrue(is_sanitized(row[2]), f"Author not sanitized: {row[2]}")
            # Categories: +category
            self.assertTrue(is_sanitized(row[3]), f"Categories not sanitized: {row[3]}")
            # External Link: -http://example.com
            self.assertTrue(is_sanitized(row[4]), f"External Link not sanitized: {row[4]}")

        # Cleanup
        if os.path.exists("test_links.json"):
            os.remove("test_links.json")
        if os.path.exists("test_links.csv"):
            os.remove("test_links.csv")
        if os.path.exists("test_unique_links.txt"):
            os.remove("test_unique_links.txt")

if __name__ == '__main__':
    unittest.main()
