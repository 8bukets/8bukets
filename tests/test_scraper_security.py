import unittest
import csv
import os
import sys
import tempfile
import shutil

# Add parent directory to path to import scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import MarkPositionScraperAsync

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.json_file = os.path.join(self.test_dir, 'test.json')
        self.csv_file = os.path.join(self.test_dir, 'test.csv')
        self.txt_file = os.path.join(self.test_dir, 'test.txt')
        self.scraper = MarkPositionScraperAsync(self.json_file, self.csv_file, self.txt_file)

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_csv_injection_prevention(self):
        """Test that potential formula injection characters are escaped in CSV."""
        malicious_data = [
            {
                'title': '=1+1',
                'date': '+2023-01-01',
                'author': '@attacker',
                'categories': ['-malicious'],
                'external_link': '\tmalicious_tab',
                'domain': '0',  # Test for integer 0 / string "0" not being empty
                'post_url': 'http://example.com/post'
            }
        ]

        self.scraper.save_data(malicious_data)

        with open(self.csv_file, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader)
            row = next(reader)

            # Helper to check if value is sanitized (starts with ')
            def is_sanitized(val):
                return val.startswith("'")

            # Title: =1+1 -> '=1+1
            self.assertTrue(is_sanitized(row[0]), f"Title not sanitized: {row[0]}")
            self.assertEqual(row[0], "'=1+1")

            # Date: +2023-01-01 -> '+2023-01-01
            self.assertTrue(is_sanitized(row[1]), f"Date not sanitized: {row[1]}")
            self.assertEqual(row[1], "'+2023-01-01")

            # Author: @attacker -> '@attacker
            self.assertTrue(is_sanitized(row[2]), f"Author not sanitized: {row[2]}")
            self.assertEqual(row[2], "'@attacker")

            # Categories: -malicious -> '-malicious
            self.assertTrue(is_sanitized(row[3]), f"Categories not sanitized: {row[3]}")
            self.assertEqual(row[3], "'-malicious")

            # External Link: \tmalicious_tab -> '\tmalicious_tab
            self.assertTrue(is_sanitized(row[4]), f"Tab not sanitized: {row[4]}")
            self.assertEqual(row[4], "'\tmalicious_tab")

            # Domain: '0' -> '0' (should not be empty or sanitized with quote unless it starts with dangerous char)
            # '0' does not start with dangerous char, but should prevent "if not value" bug.
            self.assertEqual(row[5], "0", f"Domain '0' was incorrectly handled: {row[5]}")

if __name__ == '__main__':
    unittest.main()
