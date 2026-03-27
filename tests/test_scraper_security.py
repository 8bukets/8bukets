import unittest
import csv
import io
import json
import sys
import os

# Add project root to sys.path so we can import scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import MarkPositionScraperAsync

class TestScraperSecurity(unittest.TestCase):
    def test_csv_injection_prevention(self):
        scraper = MarkPositionScraperAsync("dummy.json", "dummy.csv", "dummy.txt")

        # Malicious input
        malicious_posts = [
            {
                'title': '=cmd|/C calc!A0',
                'date': '+2023-01-01',
                'author': '@attacker',
                'categories': ['-category'],
                'external_link': 'http://example.com',
                'domain': 'example.com',
                'post_url': 'http://example.com/post'
            }
        ]

        # Mocks
        json_f = io.StringIO()
        csv_f = io.StringIO()
        csv_writer = csv.writer(csv_f)
        txt_f = io.StringIO()
        seen_links = set()

        scraper.save_batch(malicious_posts, json_f, csv_writer, txt_f, seen_links, True)

        # Check CSV output
        csv_output = csv_f.getvalue()
        reader = csv.reader(io.StringIO(csv_output))
        row = next(reader)

        # Expectation: Values starting with =, +, -, @ should be prefixed with '
        self.assertTrue(row[0].startswith("'="), f"Title not sanitized: {row[0]}")
        self.assertTrue(row[1].startswith("'+"), f"Date not sanitized: {row[1]}")
        self.assertTrue(row[2].startswith("'@"), f"Author not sanitized: {row[2]}")
        # Categories are joined by ", ". The first one starts with -.
        self.assertTrue(row[3].startswith("'-"), f"Category not sanitized: {row[3]}")

if __name__ == '__main__':
    unittest.main()
