import unittest
from scraper import MarkPositionScraperAsync

class TestMarkPositionScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")

    def test_clean_text(self):
        # Basic whitespace cleaning
        self.assertEqual(self.scraper.clean_text("  hello   world  "), "hello world")
        # Non-breaking space
        self.assertEqual(self.scraper.clean_text("hello\xa0world"), "hello world")
        # Empty string
        self.assertEqual(self.scraper.clean_text(""), "")
        # None input
        self.assertEqual(self.scraper.clean_text(None), "")
        # Tabs and newlines
        self.assertEqual(self.scraper.clean_text("hello\t\nworld"), "hello world")

    def test_is_url(self):
        # Valid URLs
        self.assertTrue(self.scraper.is_url("https://example.com"))
        self.assertTrue(self.scraper.is_url("http://example.com"))
        self.assertTrue(self.scraper.is_url("https://sub.example.com/path"))

        # Invalid URLs
        self.assertFalse(self.scraper.is_url("ftp://example.com"))
        self.assertFalse(self.scraper.is_url("example.com"))
        self.assertFalse(self.scraper.is_url("Just some text"))
        self.assertFalse(self.scraper.is_url(""))

if __name__ == '__main__':
    unittest.main()
