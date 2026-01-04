import unittest
from scraper import clean_text, is_url, extract_domain

class TestScraperUtils(unittest.TestCase):

    def test_clean_text(self):
        self.assertEqual(clean_text("  hello   world  "), "hello world")
        self.assertEqual(clean_text("hello\xa0world"), "hello world")
        self.assertEqual(clean_text(None), "")

    def test_is_url(self):
        self.assertTrue(is_url("https://example.com"))
        self.assertTrue(is_url("http://example.com"))
        self.assertFalse(is_url("example.com"))
        self.assertFalse(is_url("Not a URL"))

    def test_extract_domain(self):
        self.assertEqual(extract_domain("https://www.example.com/page"), "example.com")
        self.assertEqual(extract_domain("http://sub.example.com"), "sub.example.com")
        self.assertIsNone(extract_domain(None))
        self.assertIsNone(extract_domain("not a url"))

if __name__ == '__main__':
    unittest.main()
