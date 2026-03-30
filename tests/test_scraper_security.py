import unittest
import csv
import io
import sys
import os

# Add root directory to sys.path to allow importing scraper
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scraper import MarkPositionScraperAsync

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        self.scraper = MarkPositionScraperAsync("dummy.json", "dummy.csv", "dummy.txt")

    def test_sanitize_for_csv_injection(self):
        """Test that CSV Formula Injection payloads are sanitized."""
        # Test cases: payload -> expected (sanitized)
        test_cases = [
            ("=HYPERLINK('http://malicious.com')", "'=HYPERLINK('http://malicious.com')"),
            ("+1+2", "'+1+2"),
            ("-1+2", "'-1+2"),
            ("@SUM(1+1)", "'@SUM(1+1)"),
            ("Normal Text", "Normal Text"),
            ("", ""),
            (None, ""),
            ("=Safe?", "'=Safe?"),
        ]

        for payload, expected in test_cases:
            with self.subTest(payload=payload):
                result = self.scraper.sanitize_for_csv(payload)
                self.assertEqual(result, expected)

    def test_save_batch_sanitization(self):
        """Test that save_batch actually uses sanitization."""
        # Mock objects
        class MockWriter:
            def __init__(self):
                self.rows = []
            def writerow(self, row):
                self.rows.append(row)

        mock_writer = MockWriter()

        # Data with potential injection
        posts = [{
            'title': '=CMD|',
            'date': '+2023',
            'author': '@Hacker',
            'categories': ['-Cat1', 'Cat2'],
            'external_link': '=http://evil.com',
            'domain': '+evil.com',
            'post_url': '@http://post.com'
        }]

        # Dummy file handles
        class MockFile:
            def write(self, text): pass

        mock_json = MockFile()
        mock_txt = MockFile()

        self.scraper.save_batch(posts, mock_json, mock_writer, mock_txt, set(), True)

        # Check if fields were sanitized in the CSV writer
        row = mock_writer.rows[0]

        # Order: Title, Date, Author, Categories, External Link, Domain, Post URL
        self.assertEqual(row[0], "'=CMD|")
        self.assertEqual(row[1], "'+2023")
        self.assertEqual(row[2], "'@Hacker")
        # Categories are joined, check logic. Expected: "'-Cat1, Cat2" (because the string starts with -)
        self.assertEqual(row[3], "'-Cat1, Cat2")
        self.assertEqual(row[4], "'=http://evil.com")
        self.assertEqual(row[5], "'+evil.com")
        self.assertEqual(row[6], "'@http://post.com")

if __name__ == '__main__':
    unittest.main()
