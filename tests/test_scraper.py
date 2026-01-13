import unittest
from scraper import MarkPositionScraperAsync
from bs4 import BeautifulSoup

class TestScraperHelpers(unittest.TestCase):
    def setUp(self):
        self.scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")

    def test_clean_text(self):
        self.assertEqual(self.scraper.clean_text("  hello   world  "), "hello world")
        self.assertEqual(self.scraper.clean_text("hello\xa0world"), "hello world")
        self.assertEqual(self.scraper.clean_text(None), "")

    def test_is_url(self):
        self.assertTrue(self.scraper.is_url("https://example.com"))
        self.assertTrue(self.scraper.is_url("http://example.com"))
        self.assertFalse(self.scraper.is_url("example.com"))
        self.assertFalse(self.scraper.is_url("ftp://example.com"))

    def test_extract_domain(self):
        self.assertEqual(self.scraper.extract_domain("https://www.example.com/page"), "example.com")
        self.assertEqual(self.scraper.extract_domain("http://sub.example.com"), "sub.example.com")
        self.assertIsNone(self.scraper.extract_domain(None))
        # urlparse("not a url").netloc is empty string
        self.assertEqual(self.scraper.extract_domain("not a url"), "")

if __name__ == '__main__':
    unittest.main()
