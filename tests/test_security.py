import unittest
import os
import csv
from scraper import OracleNewsScraper

class TestSecurity(unittest.TestCase):
    def setUp(self):
        self.json_file = "test_links.json"
        self.csv_file = "test_links.csv"
        self.txt_file = "test_links.txt"
        self.scraper = OracleNewsScraper(self.json_file, self.csv_file, self.txt_file)

    def tearDown(self):
        for f in [self.json_file, self.csv_file, self.txt_file]:
            if os.path.exists(f):
                os.remove(f)

    def test_csv_injection_prevention(self):
        """Test that CSV injection payloads are escaped."""
        # Payload starting with '='
        malicious_title = "=cmd|'/C calc'!A0"
        # Payload starting with '+'
        plus_payload = "+sum(1+1)*cmd"

        mock_posts = [
            {
                'title': malicious_title,
                'date': 'Oct 15, 2025',
                'author': 'Hacker',
                'categories': ['News'],
                'external_link': 'http://evil.com',
                'domain': 'evil.com',
                'post_url': 'http://evil.com'
            },
            {
                'title': "Safe Title",
                'date': plus_payload, # Injection in date field
                'author': 'Oracle',
                'categories': ['News'],
                'external_link': 'http://oracle.com',
                'domain': 'oracle.com',
                'post_url': 'http://oracle.com'
            }
        ]

        self.scraper.save_data(mock_posts)

        with open(self.csv_file, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)

            # Check first row (Title injection)
            row1 = next(reader)
            self.assertTrue(row1[0].startswith("'="), f"Title starting with '=' should be escaped. Got: {row1[0]}")

            # Check second row (Date injection)
            row2 = next(reader)
            self.assertTrue(row2[1].startswith("'+"), f"Date starting with '+' should be escaped. Got: {row2[1]}")

if __name__ == '__main__':
    unittest.main()
