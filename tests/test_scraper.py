import unittest
import sys
import os

# Add root directory to path so we can import scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import MarkPositionScraperAsync

class TestScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = MarkPositionScraperAsync("dummy.json", "dummy.csv", "dummy.txt")

    def test_clean_text(self):
        self.assertEqual(self.scraper.clean_text("  hello   world  "), "hello world")
        self.assertEqual(self.scraper.clean_text("hello\xa0world"), "hello world")
        self.assertEqual(self.scraper.clean_text("  hello \xa0  world  \n"), "hello world")
        self.assertEqual(self.scraper.clean_text(None), "")
        self.assertEqual(self.scraper.clean_text(""), "")

    def test_is_url(self):
        self.assertTrue(self.scraper.is_url("http://example.com"))
        self.assertTrue(self.scraper.is_url("https://example.com"))
        self.assertFalse(self.scraper.is_url("example.com"))
        self.assertFalse(self.scraper.is_url("Not a url"))
        self.assertFalse(self.scraper.is_url("   "))

if __name__ == '__main__':
    unittest.main()
