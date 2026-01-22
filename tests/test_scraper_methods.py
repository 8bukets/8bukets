import unittest
from scraper import MarkPositionScraperAsync

class TestMarkPositionScraperMethods(unittest.TestCase):
    def setUp(self):
        # We don't need real output files for these tests
        self.scraper = MarkPositionScraperAsync("dummy.json", "dummy.csv", "dummy.txt")

    def test_clean_text_basic(self):
        self.assertEqual(self.scraper.clean_text("  hello   world  "), "hello world")
        self.assertEqual(self.scraper.clean_text("hello world"), "hello world")
        self.assertEqual(self.scraper.clean_text(""), "")
        self.assertEqual(self.scraper.clean_text(None), "")

    def test_clean_text_nbsp(self):
        # \xa0 is non-breaking space
        self.assertEqual(self.scraper.clean_text("hello\xa0world"), "hello world")
        self.assertEqual(self.scraper.clean_text("hello \xa0 world"), "hello world")

    def test_clean_text_newlines(self):
        self.assertEqual(self.scraper.clean_text("hello\nworld"), "hello world")
        self.assertEqual(self.scraper.clean_text("hello\n\tworld"), "hello world")

    def test_is_url(self):
        self.assertTrue(self.scraper.is_url("http://example.com"))
        self.assertTrue(self.scraper.is_url("https://example.com"))
        self.assertTrue(self.scraper.is_url("https://sub.domain.com/path?q=1"))
        self.assertTrue(self.scraper.is_url("  https://example.com  ")) # strips whitespace

        self.assertFalse(self.scraper.is_url("example.com"))
        self.assertFalse(self.scraper.is_url("ftp://example.com")) # regex only checks http(s)
        self.assertFalse(self.scraper.is_url("Just text"))
        self.assertFalse(self.scraper.is_url(""))

if __name__ == '__main__':
    unittest.main()
