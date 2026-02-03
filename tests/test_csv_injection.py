import unittest
import os
import csv
import tempfile
import shutil
import sys

# Add parent directory to path to import scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import MarkPositionScraperAsync

class TestCSVInjection(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.json_path = os.path.join(self.test_dir, 'test.json')
        self.csv_path = os.path.join(self.test_dir, 'test.csv')
        self.txt_path = os.path.join(self.test_dir, 'test.txt')
        self.scraper = MarkPositionScraperAsync(
            output_json=self.json_path,
            output_csv=self.csv_path,
            output_txt=self.txt_path
        )

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_csv_injection(self):
        malicious_posts = [
            {
                'title': '=1+1',
                'date': '+2023-01-01',
                'author': '-Author',
                'categories': ['@Category'],
                'external_link': '=http://evil.com',
                'domain': '+evil.com',
                'post_url': '-http://example.com/post'
            }
        ]

        self.scraper.save_data(malicious_posts)

        with open(self.csv_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)

        # Expected behavior: All dangerous fields should be prefixed with '
        self.assertTrue(row[0].startswith("'"), f"Title not sanitized: {row[0]}")
        self.assertTrue(row[1].startswith("'"), f"Date not sanitized: {row[1]}")
        self.assertTrue(row[2].startswith("'"), f"Author not sanitized: {row[2]}")
        self.assertTrue(row[3].startswith("'"), f"Categories not sanitized: {row[3]}")
        self.assertTrue(row[4].startswith("'"), f"External Link not sanitized: {row[4]}")
        self.assertTrue(row[5].startswith("'"), f"Domain not sanitized: {row[5]}")
        self.assertTrue(row[6].startswith("'"), f"Post URL not sanitized: {row[6]}")

if __name__ == '__main__':
    unittest.main()
