import unittest
from scraper import MarkPositionScraperAsync
import re

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        self.scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")

    def test_clean_text_basic(self):
        self.assertEqual(self.scraper.clean_text("  Hello   World  "), "Hello World")
        self.assertEqual(self.scraper.clean_text("Hello\xa0World"), "Hello World")
        self.assertEqual(self.scraper.clean_text(None), "")

    def test_is_url_basic(self):
        self.assertTrue(self.scraper.is_url("https://example.com"))
        self.assertTrue(self.scraper.is_url("http://example.com"))
        self.assertFalse(self.scraper.is_url("ftp://example.com"))
        self.assertFalse(self.scraper.is_url("example.com"))
        self.assertFalse(self.scraper.is_url(""))

if __name__ == '__main__':
    unittest.main()
