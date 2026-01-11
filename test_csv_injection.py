import unittest
import csv
import io
import os
from scraper import MarkPositionScraperAsync

class TestCSVInjection(unittest.TestCase):
    def test_csv_injection_sanitization(self):
        # Data with potential formula injection
        posts = [
            {
                'title': '=1+1',
                'date': '@SUM(1,2)',
                'author': '+Malicious',
                'categories': ['-BadCategory'],
                'external_link': 'http://example.com',
                'domain': 'example.com',
                'post_url': 'http://example.com/post'
            },
             {
                'title': 'Safe Title',
                'date': '2022-01-01',
                'author': 'Safe Author',
                'categories': ['Safe Category'],
                'external_link': 'http://example.com',
                'domain': 'example.com',
                'post_url': 'http://example.com/post'
            }
        ]

        output_csv = 'test_injection.csv'
        scraper = MarkPositionScraperAsync(
            output_json='test.json',
            output_csv=output_csv,
            output_txt='test.txt'
        )

        # Manually invoke save_data which contains the logic
        scraper.save_data(posts)

        # Verify content
        with open(output_csv, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row1 = next(reader)
            row2 = next(reader)

        # Clean up
        if os.path.exists(output_csv):
            os.remove(output_csv)
        if os.path.exists('test.json'):
            os.remove('test.json')
        if os.path.exists('test.txt'):
            os.remove('test.txt')

        # Check for single quotes
        self.assertTrue(row1[0].startswith("'"), f"Title should be sanitized: {row1[0]}")
        self.assertTrue(row1[1].startswith("'"), f"Date should be sanitized: {row1[1]}")
        self.assertTrue(row1[2].startswith("'"), f"Author should be sanitized: {row1[2]}")
        self.assertTrue(row1[3].startswith("'"), f"Category should be sanitized: {row1[3]}")

        # Check safe row
        self.assertFalse(row2[0].startswith("'"), f"Safe Title should NOT be sanitized: {row2[0]}")

if __name__ == '__main__':
    unittest.main()
