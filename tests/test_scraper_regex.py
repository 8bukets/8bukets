
import unittest
from scraper import MarkPositionScraperAsync

class TestScraperRegex(unittest.TestCase):
    def setUp(self):
        self.scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")

    def test_clean_text(self):
        self.assertEqual(self.scraper.clean_text("  hello   world  "), "hello world")
        self.assertEqual(self.scraper.clean_text("hello\xa0world"), "hello world")
        self.assertEqual(self.scraper.clean_text(None), "")
        self.assertEqual(self.scraper.clean_text(""), "")

    def test_is_url(self):
        self.assertTrue(self.scraper.is_url("https://example.com"))
        self.assertTrue(self.scraper.is_url("  https://example.com  "))
        self.assertTrue(self.scraper.is_url("http://example.com"))
        self.assertFalse(self.scraper.is_url("example.com"))
        self.assertFalse(self.scraper.is_url("ftp://example.com"))

if __name__ == '__main__':
    unittest.main()
