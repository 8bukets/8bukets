import unittest
import os
import csv
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scraper import MarkPositionScraperAsync

class TestCSVInjection(unittest.TestCase):
    def setUp(self):
        self.output_json = "test_links.json"
        self.output_csv = "test_links.csv"
        self.output_txt = "test_unique_links.txt"
        self.scraper = MarkPositionScraperAsync(self.output_json, self.output_csv, self.output_txt)

    def tearDown(self):
        if os.path.exists(self.output_json):
            os.remove(self.output_json)
        if os.path.exists(self.output_csv):
            os.remove(self.output_csv)
        if os.path.exists(self.output_txt):
            os.remove(self.output_txt)

    def test_csv_injection(self):
        # Malicious data
        malicious_posts = [{
            'title': '=1+1',
            'date': '@SUM(1,1)',
            'author': '-1',
            'categories': ['+1'],
            'external_link': 'http://example.com',
            'domain': 'example.com',
            'post_url': 'http://example.com/post'
        }]

        self.scraper.save_data(malicious_posts)

        # Read the CSV and check for injection
        with open(self.output_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)

            # If the value starts with =, @, +, or -, it's potentially dangerous
            # The fix should prepend a single quote

            # Check Title (was =1+1)
            self.assertTrue(row[0].startswith("'"), "Title SHOULD be sanitized (start with ')")
            self.assertEqual(row[0], "'=1+1")

            # Check Date (was @SUM(1,1))
            self.assertTrue(row[1].startswith("'"), "Date SHOULD be sanitized")
            self.assertEqual(row[1], "'@SUM(1,1)")

            # Check Author (was -1)
            self.assertTrue(row[2].startswith("'"), "Author SHOULD be sanitized")
            self.assertEqual(row[2], "'-1")

            # Check Categories (was +1)
            self.assertTrue(row[3].startswith("'"), "Categories SHOULD be sanitized")
            self.assertEqual(row[3], "'+1")

if __name__ == '__main__':
    unittest.main()
