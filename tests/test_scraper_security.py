import unittest
import csv
import os
import sys
import tempfile
import shutil

# Add root directory to python path to import scraper
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scraper import MarkPositionScraperAsync

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()
        self.json_path = os.path.join(self.test_dir, "test.json")
        self.csv_path = os.path.join(self.test_dir, "test.csv")
        self.txt_path = os.path.join(self.test_dir, "test.txt")

        self.scraper = MarkPositionScraperAsync(self.json_path, self.csv_path, self.txt_path)

    def tearDown(self):
        # Remove the directory after the test
        shutil.rmtree(self.test_dir)

    def test_sanitize_for_csv(self):
        """Test the sanitize_for_csv method directly."""
        # Test dangerous characters
        self.assertEqual(self.scraper.sanitize_for_csv("=1+1"), "'=1+1")
        self.assertEqual(self.scraper.sanitize_for_csv("+1+1"), "'+1+1")
        self.assertEqual(self.scraper.sanitize_for_csv("-1+1"), "'-1+1")
        self.assertEqual(self.scraper.sanitize_for_csv("@SUM(1,1)"), "'@SUM(1,1)")

        # Test safe characters
        self.assertEqual(self.scraper.sanitize_for_csv("Safe Title"), "Safe Title")
        self.assertEqual(self.scraper.sanitize_for_csv("123"), "123")
        self.assertEqual(self.scraper.sanitize_for_csv(""), "")
        self.assertEqual(self.scraper.sanitize_for_csv(None), "")

    def test_save_data_csv_injection(self):
        """Test that save_data correctly sanitizes CSV output."""
        malicious_post = {
            'title': '=cmd|/C calc!A0',
            'date': '2023-01-01',
            'author': '+Hacker',
            'categories': ['@Test'],
            'external_link': '-http://evil.com',
            'domain': 'evil.com',
            'post_url': 'http://example.com/post'
        }

        self.scraper.save_data([malicious_post])

        with open(self.csv_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader) # Skip header
            row = next(reader)

            # Check Title
            self.assertTrue(row[0].startswith("'="), f"Title not sanitized: {row[0]}")
            # Check Author
            self.assertTrue(row[2].startswith("'+"), f"Author not sanitized: {row[2]}")
            # Check Categories
            self.assertTrue(row[3].startswith("'@"), f"Categories not sanitized: {row[3]}")
            # Check External Link
            self.assertTrue(row[4].startswith("'-"), f"Link not sanitized: {row[4]}")

if __name__ == '__main__':
    unittest.main()
