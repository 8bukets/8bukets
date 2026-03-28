import os
import csv
import sys
import unittest

# Add parent directory to path to allow importing scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import MarkPositionScraperAsync

class TestCSVInjection(unittest.TestCase):
    def setUp(self):
        self.output_json = "test_output.json"
        self.output_csv = "test_output.csv"
        self.output_txt = "test_output.txt"
        self.clean_up()

    def tearDown(self):
        self.clean_up()

    def clean_up(self):
        for f in [self.output_json, self.output_csv, self.output_txt]:
            if os.path.exists(f):
                os.remove(f)

    def test_csv_injection_sanitization(self):
        scraper = MarkPositionScraperAsync(self.output_json, self.output_csv, self.output_txt)

        malicious_data = [
            {
                'title': '=cmd|/C calc!A0',
                'date': '+2023-01-01',
                'author': '@SUM(1+1)',
                'categories': ['-Malicious'],
                'external_link': 'Safe Link',
                'domain': 'example.com',
                'post_url': 'http://example.com'
            }
        ]

        scraper.save_data(malicious_data)

        self.assertTrue(os.path.exists(self.output_csv), "CSV file should be created")

        with open(self.output_csv, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)

            # Row structure: Title, Date, Author, Categories, External Link, Domain, Post URL

            # Check Title (=)
            self.assertFalse(row[0].startswith('='), f"Title vulnerability found: {row[0]}")
            self.assertTrue(row[0].startswith("'="), f"Title NOT escaped: {row[0]}")

            # Check Date (+)
            self.assertFalse(row[1].startswith('+'), f"Date vulnerability found: {row[1]}")
            self.assertTrue(row[1].startswith("'+"), f"Date NOT escaped: {row[1]}")

            # Check Author (@)
            self.assertFalse(row[2].startswith('@'), f"Author vulnerability found: {row[2]}")
            self.assertTrue(row[2].startswith("'@"), f"Author NOT escaped: {row[2]}")

            # Check Categories (-)
            self.assertFalse(row[3].startswith('-'), f"Categories vulnerability found: {row[3]}")
            self.assertTrue(row[3].startswith("'-"), f"Categories NOT escaped: {row[3]}")

if __name__ == "__main__":
    unittest.main()
