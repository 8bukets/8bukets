import unittest
import sys
import os
import re

# Add root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import OracleNewsScraper

class TestOracleNewsScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = OracleNewsScraper("dummy.json", "dummy.csv", "dummy.txt")

    def test_clean_text(self):
        # Test 1: Basic whitespace
        self.assertEqual(self.scraper.clean_text("  hello   world  "), "hello world")

        # Test 2: Non-breaking space
        self.assertEqual(self.scraper.clean_text("hello\xa0world"), "hello world")

        # Test 3: Newlines and tabs
        self.assertEqual(self.scraper.clean_text("hello\n\tworld"), "hello world")

        # Test 4: Empty string
        self.assertEqual(self.scraper.clean_text(""), "")

        # Test 5: None
        self.assertEqual(self.scraper.clean_text(None), "")

    def test_date_regex_pattern(self):
        # Verify the regex pattern works as expected
        pattern = self.scraper.DATE_PATTERN

        # Match
        match = pattern.search("some-url-2025-12-11/")
        self.assertIsNotNone(match)
        self.assertEqual(match.group(1), "2025-12-11")

        # No match
        match = pattern.search("some-url-no-date/")
        self.assertIsNone(match)

        # Match middle
        match = pattern.search("prefix-2024-01-01-suffix")
        self.assertIsNotNone(match)
        self.assertEqual(match.group(1), "2024-01-01")

if __name__ == '__main__':
    unittest.main()
