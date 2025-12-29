import unittest
import csv
import os
import sys

# Add root directory to path to import scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import MarkPositionScraperAsync

class TestSecurity(unittest.TestCase):
    def test_csv_injection(self):
        # Malicious data
        malicious_posts = [
            {
                'title': '=1+1',  # Formula injection
                'date': '2023-01-01',
                'author': 'Hacker',
                'categories': ['Tech'],
                'external_link': 'http://example.com',
                'domain': 'example.com',
                'post_url': 'http://site.com/post'
            },
            {
                'title': '@SUM(1,1)', # Another injection
                'date': '2023-01-02',
                'author': 'Hacker',
                'categories': ['Tech'],
                'external_link': 'http://example.com',
                'domain': 'example.com',
                'post_url': 'http://site.com/post2'
            }
        ]

        scraper = MarkPositionScraperAsync(
            output_json='dummy.json',
            output_csv='test_output.csv',
            output_txt='dummy.txt'
        )

        try:
            scraper.save_data(malicious_posts)

            with open('test_output.csv', 'r', newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                header = next(reader)
                row1 = next(reader)
                row2 = next(reader)

                # Check row 1 title
                self.assertTrue(row1[0].startswith("'"), f"Title starting with '=' should be escaped. Got: {row1[0]}")
                self.assertEqual(row1[0], "'=1+1")

                # Check row 2 title
                self.assertTrue(row2[0].startswith("'"), f"Title starting with '@' should be escaped. Got: {row2[0]}")
                self.assertEqual(row2[0], "'@SUM(1,1)")

        finally:
            if os.path.exists('test_output.csv'):
                os.remove('test_output.csv')
            if os.path.exists('dummy.json'):
                os.remove('dummy.json')
            if os.path.exists('dummy.txt'):
                os.remove('dummy.txt')

if __name__ == '__main__':
    unittest.main()
