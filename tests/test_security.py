import unittest
import os
import csv
import sys
import shutil

# Add parent directory to path to import scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import MarkPositionScraperAsync

class TestCSVSecurity(unittest.TestCase):
    def setUp(self):
        self.test_dir = 'test_output'
        if not os.path.exists(self.test_dir):
            os.makedirs(self.test_dir)
        self.json_file = os.path.join(self.test_dir, 'test.json')
        self.csv_file = os.path.join(self.test_dir, 'test.csv')
        self.txt_file = os.path.join(self.test_dir, 'test.txt')

        self.scraper = MarkPositionScraperAsync(
            output_json=self.json_file,
            output_csv=self.csv_file,
            output_txt=self.txt_file
        )

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_csv_injection_prevention(self):
        # Malicious data samples
        malicious_posts = [
            {
                'title': '=SUM(1+1)',
                'date': '@SUM(1+1)',
                'author': '+SUM(1+1)',
                'categories': ['-SUM(1+1)', 'Normal'],
                'external_link': 'http://example.com',
                'domain': 'example.com',
                'post_url': 'http://example.com/post'
            },
            {
                'title': 'Normal Title',
                'date': '2023-01-01',
                'author': 'Normal Author',
                'categories': ['News'],
                'external_link': 'http://example.com',
                'domain': 'example.com',
                'post_url': 'http://example.com/post'
            }
        ]

        # Save data
        self.scraper.save_data(malicious_posts)

        # Read CSV and verify sanitization
        with open(self.csv_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row1 = next(reader) # Malicious row
            row2 = next(reader) # Normal row

        # Check malicious fields
        # Title starts with =
        self.assertFalse(row1[0].startswith('='), "Title starting with '=' should be sanitized")
        self.assertTrue(row1[0].startswith("'="), f"Title should be escaped with single quote, got: {row1[0]}")

        # Date starts with @
        self.assertFalse(row1[1].startswith('@'), "Date starting with '@' should be sanitized")
        self.assertTrue(row1[1].startswith("'@"), f"Date should be escaped with single quote, got: {row1[1]}")

        # Author starts with +
        self.assertFalse(row1[2].startswith('+'), "Author starting with '+' should be sanitized")
        self.assertTrue(row1[2].startswith("'+"), f"Author should be escaped with single quote, got: {row1[2]}")

        # Categories - joined by comma, first one starts with -
        # The first char of the string will be -
        self.assertFalse(row1[3].startswith('-'), "Categories string starting with '-' should be sanitized")
        self.assertTrue(row1[3].startswith("'-"), f"Categories should be escaped with single quote, got: {row1[3]}")

        # Check normal fields remain normal
        self.assertEqual(row2[0], 'Normal Title')

if __name__ == '__main__':
    unittest.main()
