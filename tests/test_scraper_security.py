import unittest
import os
import csv
import sys
# Add parent directory to path so we can import scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import MarkPositionScraperAsync

class TestCSVSecurity(unittest.TestCase):
    def setUp(self):
        self.csv_file = 'test_links.csv'
        self.json_file = 'test_links.json'
        self.txt_file = 'test_unique_links.txt'
        self.scraper = MarkPositionScraperAsync(self.json_file, self.csv_file, self.txt_file)

    def tearDown(self):
        if os.path.exists(self.csv_file):
            os.remove(self.csv_file)
        if os.path.exists(self.json_file):
            os.remove(self.json_file)
        if os.path.exists(self.txt_file):
            os.remove(self.txt_file)

    def test_csv_injection_prevention(self):
        """Test that user-controlled fields are sanitized to prevent CSV injection."""
        # Malicious payloads
        payloads = [
            {'title': '=cmd|/C calc!A0', 'date': '2023-01-01', 'author': 'Hacker', 'categories': ['News'], 'external_link': 'http://evil.com', 'domain': 'evil.com', 'post_url': 'http://site.com/post'},
            {'title': '+1+2', 'date': '2023-01-01', 'author': '@MyName', 'categories': ['-Formula'], 'external_link': 'http://evil.com', 'domain': 'evil.com', 'post_url': 'http://site.com/post2'},
        ]

        self.scraper.save_data(payloads)

        with open(self.csv_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row1 = next(reader)
            row2 = next(reader)

            # Check for fix: payloads should be escaped with '
            self.assertEqual(row1[0], "'=cmd|/C calc!A0", "Title starting with = not escaped")
            self.assertEqual(row2[0], "'+1+2", "Title starting with + not escaped")
            self.assertEqual(row2[2], "'@MyName", "Author starting with @ not escaped")
            self.assertEqual(row2[3], "'-Formula", "Category starting with - not escaped")

if __name__ == '__main__':
    unittest.main()
