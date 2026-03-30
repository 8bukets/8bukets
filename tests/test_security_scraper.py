import sys
import os
import csv
import unittest

# Add parent directory to path to import scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import MarkPositionScraperAsync

class TestCsvSecurity(unittest.TestCase):
    def setUp(self):
        self.csv_file = "tests/temp_security_test.csv"
        # Dummy files for json/txt
        self.json_file = "tests/temp.json"
        self.txt_file = "tests/temp.txt"

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

    def test_csv_injection_sanitization(self):
        # Data with potential CSV injection payloads
        malicious_posts = [
            {
                'title': '=1+1',
                'date': '@2023',
                'author': '+BadActor',
                'categories': ['-Category'],
                'external_link': 'http://example.com',
                'domain': 'example.com',
                'post_url': 'http://post.url'
            }
        ]

        self.scraper.save_data(malicious_posts)

        if not os.path.exists(self.csv_file):
            self.fail("CSV file was not created")

        with open(self.csv_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)

            # Check Title (=1+1) -> Should be sanitized to '=1+1
            self.assertTrue(row[0].startswith("'"), f"Title not sanitized: {row[0]}")
            self.assertEqual(row[0], "'=1+1")

            # Check Date (@2023) -> Should be sanitized to '@2023
            self.assertTrue(row[1].startswith("'"), f"Date not sanitized: {row[1]}")

            # Check Author (+BadActor) -> Should be sanitized to '+BadActor
            self.assertTrue(row[2].startswith("'"), f"Author not sanitized: {row[2]}")

            # Check Categories (-Category) -> Should be sanitized to '-Category
            self.assertTrue(row[3].startswith("'"), f"Categories not sanitized: {row[3]}")

if __name__ == '__main__':
    unittest.main()
