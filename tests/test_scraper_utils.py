import unittest
from scraper import MarkPositionScraperAsync

class TestScraperUtils(unittest.TestCase):
    def setUp(self):
        # Initialize with dummy paths
        self.scraper = MarkPositionScraperAsync("dummy.json", "dummy.csv", "dummy.txt")

    def test_clean_text(self):
        # Basic whitespace
        self.assertEqual(self.scraper.clean_text("  hello   world  "), "hello world")
        # Non-breaking space
        self.assertEqual(self.scraper.clean_text("hello\xa0world"), "hello world")
        # Newlines and tabs
        self.assertEqual(self.scraper.clean_text("hello\n\tworld"), "hello world")
        # Empty and None
        self.assertEqual(self.scraper.clean_text(""), "")
        self.assertEqual(self.scraper.clean_text(None), "")
        # Already clean
        self.assertEqual(self.scraper.clean_text("hello world"), "hello world")

    def test_is_url(self):
        # Valid URLs
        self.assertTrue(self.scraper.is_url("https://example.com"))
        self.assertTrue(self.scraper.is_url("http://example.com"))
        self.assertTrue(self.scraper.is_url("  https://example.com  "))

        # Invalid URLs
        self.assertFalse(self.scraper.is_url("ftp://example.com"))
        self.assertFalse(self.scraper.is_url("example.com"))
        self.assertFalse(self.scraper.is_url(""))
        self.assertFalse(self.scraper.is_url("   "))
        self.assertFalse(self.scraper.is_url("not a url"))

if __name__ == '__main__':
    unittest.main()
