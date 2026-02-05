import unittest
import csv
import os
import sys

# Add parent directory to path to import scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import MarkPositionScraperAsync

class TestCSVInjection(unittest.TestCase):
    def setUp(self):
        self.scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")
        self.malicious_data = [
            {
                'title': '=cmd|/C calc!A0',
                'date': '2023-01-01',
                'author': '@SUM(1+1)',
                'categories': ['+Normal'],
                'external_link': '-MaliciousLink',
                'domain': 'example.com',
                'post_url': 'http://example.com'
            }
        ]

    def test_csv_injection_vulnerability(self):
        # This test verifies that the code sanitizes malicious strings.

        self.scraper.save_data(self.malicious_data)

        with open("test.csv", "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            headers = next(reader)
            row = next(reader)

            # Check Title (Should be sanitized with ')
            self.assertEqual(row[0], "'=cmd|/C calc!A0")
            # Check Author (Should be sanitized with ')
            self.assertEqual(row[2], "'@SUM(1+1)")
            # Check Categories (Should be sanitized with ')
            self.assertEqual(row[3], "'+Normal")
            # Check External Link (Should be sanitized with ')
            self.assertEqual(row[4], "'-MaliciousLink")

    def tearDown(self):
        for f in ["test.json", "test.csv", "test.txt"]:
            if os.path.exists(f):
                os.remove(f)

if __name__ == '__main__':
    unittest.main()
