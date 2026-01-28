import unittest
import re
from scraper import MarkPositionScraperAsync

class TestMarkPositionScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")

    def test_clean_text(self):
        self.assertEqual(self.scraper.clean_text("  Hello   World  "), "Hello World")
        self.assertEqual(self.scraper.clean_text("NoChange"), "NoChange")
        self.assertEqual(self.scraper.clean_text(None), "")
        self.assertEqual(self.scraper.clean_text("Line\nBreak"), "Line Break")
        self.assertEqual(self.scraper.clean_text("Non\xa0Breaking"), "Non Breaking")

    def test_is_url(self):
        self.assertTrue(self.scraper.is_url("https://example.com"))
        self.assertTrue(self.scraper.is_url("http://example.com"))
        self.assertFalse(self.scraper.is_url("example.com"))
        self.assertFalse(self.scraper.is_url("Not a URL"))
        self.assertFalse(self.scraper.is_url(""))

if __name__ == '__main__':
    unittest.main()
