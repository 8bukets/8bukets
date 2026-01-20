
import unittest
import csv
import os
import shutil
import tempfile
from scraper import MarkPositionScraperAsync

class TestSecurity(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.output_json = os.path.join(self.test_dir, 'test.json')
        self.output_csv = os.path.join(self.test_dir, 'test.csv')
        self.output_txt = os.path.join(self.test_dir, 'test.txt')
        self.scraper = MarkPositionScraperAsync(self.output_json, self.output_csv, self.output_txt)

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_csv_injection_prevention(self):
        """Test that CSV injection payloads are sanitized."""
        malicious_posts = [
            {
                'title': '=cmd| /C calc',
                'date': '2023-01-01',
                'author': '+Malicious',
                'categories': ['@Category'],
                'external_link': '-http://evil.com',
                'domain': 'evil.com',
                'post_url': 'http://example.com'
            }
        ]

        self.scraper.save_data(malicious_posts)

        with open(self.output_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)

            # Check Title
            self.assertTrue(row[0].startswith("'="), f"Title not sanitized: {row[0]}")
            # Check Author
            self.assertTrue(row[2].startswith("'+"), f"Author not sanitized: {row[2]}")
            # Check Categories
            self.assertTrue(row[3].startswith("'@"), f"Categories not sanitized: {row[3]}")
            # Check External Link
            self.assertTrue(row[4].startswith("'-"), f"External Link not sanitized: {row[4]}")

    def test_normal_data_integrity(self):
        """Test that normal data is not altered."""
        normal_posts = [
            {
                'title': 'Normal Title',
                'date': '2023-01-01',
                'author': 'John Doe',
                'categories': ['Tech'],
                'external_link': 'http://google.com',
                'domain': 'google.com',
                'post_url': 'http://example.com/post'
            }
        ]

        self.scraper.save_data(normal_posts)

        with open(self.output_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)

            self.assertEqual(row[0], 'Normal Title')
            self.assertEqual(row[2], 'John Doe')
            self.assertEqual(row[3], 'Tech')
            self.assertEqual(row[4], 'http://google.com')

if __name__ == '__main__':
    unittest.main()
