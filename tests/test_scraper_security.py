import unittest
import csv
import io
import sys
import os

# Add parent directory to path so we can import scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import MarkPositionScraperAsync

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        self.scraper = MarkPositionScraperAsync("dummy.json", "dummy.csv", "dummy.txt")

    def test_sanitize_for_csv(self):
        """Test that the sanitize_for_csv method correctly sanitizes inputs."""
        # Test cases that should be sanitized
        self.assertEqual(self.scraper.sanitize_for_csv("=cmd|' /C calc'!A0"), "'=cmd|' /C calc'!A0")
        self.assertEqual(self.scraper.sanitize_for_csv("+cmd|' /C calc'!A0"), "'+cmd|' /C calc'!A0")
        self.assertEqual(self.scraper.sanitize_for_csv("-cmd|' /C calc'!A0"), "'-cmd|' /C calc'!A0")
        self.assertEqual(self.scraper.sanitize_for_csv("@cmd|' /C calc'!A0"), "'@cmd|' /C calc'!A0")

        # Test cases that should NOT be sanitized
        self.assertEqual(self.scraper.sanitize_for_csv("Safe Title"), "Safe Title")
        self.assertEqual(self.scraper.sanitize_for_csv("123"), "123")
        self.assertEqual(self.scraper.sanitize_for_csv(""), "")
        self.assertEqual(self.scraper.sanitize_for_csv(None), "")

    def test_save_batch_security(self):
        """Test that save_batch applies sanitization."""
        post = {
            'title': '=Malicious Title',
            'date': '+2023-01-01',
            'author': '-Hacker',
            'categories': ['@Category'],
            'external_link': 'http://example.com',
            'domain': 'example.com',
            'post_url': 'http://example.com/post'
        }

        output = io.StringIO()
        writer = csv.writer(output)
        json_f = io.StringIO()
        txt_f = io.StringIO()
        seen_links = set()

        self.scraper.save_batch([post], json_f, writer, txt_f, seen_links, True)

        output.seek(0)
        reader = csv.reader(output)
        row = next(reader)

        # Verify all fields are sanitized if needed
        self.assertEqual(row[0], "'=Malicious Title")
        self.assertEqual(row[1], "'+2023-01-01")
        self.assertEqual(row[2], "'-Hacker")

        # Categories are joined, so the resulting string starts with @
        self.assertEqual(row[3], "'@Category")

if __name__ == '__main__':
    unittest.main()
