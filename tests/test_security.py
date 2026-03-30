import unittest
import os
import csv
from scraper import MarkPositionScraperAsync

class TestSecurity(unittest.TestCase):
    def setUp(self):
        self.json_path = "test_security_links.json"
        self.csv_path = "test_security_links.csv"
        self.txt_path = "test_security_unique_links.txt"

        self.scraper = MarkPositionScraperAsync(
            output_json=self.json_path,
            output_csv=self.csv_path,
            output_txt=self.txt_path
        )

    def tearDown(self):
        if os.path.exists(self.json_path): os.remove(self.json_path)
        if os.path.exists(self.csv_path): os.remove(self.csv_path)
        if os.path.exists(self.txt_path): os.remove(self.txt_path)

    def test_csv_injection_prevention(self):
        # Malicious payload
        malicious_posts = [
            {
                'title': '=cmd|\'/C calc\'!A0',
                'date': '+2023-01-01',
                'author': '-AuthorName',
                'categories': ['@Category'],
                'external_link': 'http://example.com',
                'domain': 'example.com',
                'post_url': 'http://post.url'
            }
        ]

        # Save data
        self.scraper.save_data(malicious_posts)

        # Verify CSV content
        with open(self.csv_path, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader)
            row = next(reader)

            # Assert that dangerous characters are escaped with a single quote
            self.assertTrue(row[0].startswith("'="), "Title should be escaped")
            self.assertTrue(row[1].startswith("'+"), "Date should be escaped")
            self.assertTrue(row[2].startswith("'-"), "Author should be escaped")
            self.assertTrue(row[3].startswith("'@"), "Category should be escaped")

if __name__ == '__main__':
    unittest.main()
