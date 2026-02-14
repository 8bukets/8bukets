import unittest
import os
import csv
import json
from scraper import MarkPositionScraperAsync

class TestSecurity(unittest.TestCase):
    def setUp(self):
        self.csv_file = 'test_security_links.csv'
        self.json_file = 'test_security_links.json'
        self.txt_file = 'test_security_links.txt'
        self.scraper = MarkPositionScraperAsync(
            output_json=self.json_file,
            output_csv=self.csv_file,
            output_txt=self.txt_file
        )

    def tearDown(self):
        if os.path.exists(self.csv_file):
            os.remove(self.csv_file)
        if os.path.exists(self.json_file):
            os.remove(self.json_file)
        if os.path.exists(self.txt_file):
            os.remove(self.txt_file)

    def test_csv_injection_mitigation(self):
        """
        Test that fields starting with =, +, -, @ are escaped in CSV output.
        """
        malicious_posts = [
            {
                'title': '=1+1',
                'date': '2023-01-01',
                'author': '@hacker',
                'categories': ['+admin'],
                'external_link': '-dangerous',
                'domain': 'example.com',
                'post_url': 'http://example.com'
            }
        ]

        # Save data using the scraper
        self.scraper.save_data(malicious_posts)

        # Read the CSV back
        with open(self.csv_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader) # Skip header
            row = next(reader)

            # Check Title (was =1+1)
            # Vulnerable behavior: returns '=1+1'
            # Secure behavior: returns "'=1+1"

            # We assert that the fix is NOT yet applied (confirming vulnerability)
            # OR we can just write the test expecting the FIX, and see it fail.
            # I will write the test expecting the FIX.

            self.assertTrue(row[0].startswith("'"), f"Title not escaped: {row[0]}")
            self.assertEqual(row[0], "'=1+1")

            self.assertTrue(row[2].startswith("'"), f"Author not escaped: {row[2]}")
            self.assertEqual(row[2], "'@hacker")

            # Categories are joined by string, check the first one
            self.assertTrue(row[3].startswith("'"), f"Categories not escaped: {row[3]}")
            self.assertEqual(row[3], "'+admin")

            self.assertTrue(row[4].startswith("'"), f"External Link not escaped: {row[4]}")
            self.assertEqual(row[4], "'-dangerous")

if __name__ == '__main__':
    unittest.main()
