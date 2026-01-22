import unittest
from scraper import MarkPositionScraperAsync

class TestMarkPositionScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = MarkPositionScraperAsync("dummy.json", "dummy.csv", "dummy.txt")

    def test_clean_text(self):
        self.assertEqual(self.scraper.clean_text("  Simple text  "), "Simple text")
        self.assertEqual(self.scraper.clean_text("Text\xa0with\xa0nbsp"), "Text with nbsp")
        self.assertEqual(self.scraper.clean_text("  Multiple   spaces  "), "Multiple spaces")
        self.assertEqual(self.scraper.clean_text(""), "")
        self.assertEqual(self.scraper.clean_text(None), "")
        self.assertEqual(self.scraper.clean_text("\n\tNewlines and tabs\t\n"), "Newlines and tabs")

    def test_is_url(self):
        self.assertTrue(self.scraper.is_url("http://example.com"))
        self.assertTrue(self.scraper.is_url("https://example.com"))
        self.assertTrue(self.scraper.is_url("  https://example.com  "))
        self.assertFalse(self.scraper.is_url("example.com"))
        self.assertFalse(self.scraper.is_url("ftp://example.com"))
        self.assertFalse(self.scraper.is_url("Just text"))
        self.assertFalse(self.scraper.is_url(""))

    def test_extract_domain(self):
        self.assertEqual(self.scraper.extract_domain("https://www.example.com/path"), "example.com")
        self.assertEqual(self.scraper.extract_domain("http://sub.example.com"), "sub.example.com")
        self.assertIsNone(self.scraper.extract_domain(None))
        self.assertIsNone(self.scraper.extract_domain(""))

if __name__ == '__main__':
    unittest.main()
