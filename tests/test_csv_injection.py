import unittest
import csv
import os
import sys

# Add root directory to sys.path to import scraper
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scraper import MarkPositionScraperAsync

class TestCSVInjection(unittest.TestCase):
    def setUp(self):
        self.output_csv = 'test_output.csv'
        self.scraper = MarkPositionScraperAsync(
            output_json='test.json',
            output_csv=self.output_csv,
            output_txt='test.txt'
        )

    def tearDown(self):
        if os.path.exists(self.output_csv):
            os.remove(self.output_csv)
        if os.path.exists('test.json'):
            os.remove('test.json')
        if os.path.exists('test.txt'):
            os.remove('test.txt')

    def test_csv_injection_vulnerability(self):
        # Data with malicious payload
        malicious_data = [
            {
                'title': '=SUM(1+1)',
                'date': '2023-01-01',
                'author': '+MaliciousAuthor',
                'categories': ['@Category'],
                'external_link': '-http://evil.com',
                'domain': 'evil.com',
                'post_url': 'http://example.com/post'
            }
        ]

        # Save data using the scraper
        self.scraper.save_data(malicious_data)

        # Verify the CSV content
        with open(self.output_csv, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader) # Skip header
            row = next(reader)

            # Sanitized expectation
            # These should now be prepended with '
            self.assertEqual(row[0], "'=SUM(1+1)")
            self.assertEqual(row[2], "'+MaliciousAuthor")
            self.assertEqual(row[3], "'@Category")
            self.assertEqual(row[4], "'-http://evil.com")

if __name__ == '__main__':
    unittest.main()
