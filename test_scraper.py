
import unittest
from scraper import MarkPositionScraperAsync

class TestScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")

    def test_clean_text(self):
        text = "  Hello   World \xa0 "
        expected = "Hello World"
        self.assertEqual(self.scraper.clean_text(text), expected)
        self.assertEqual(self.scraper.clean_text(None), "")

    def test_is_url(self):
        self.assertTrue(self.scraper.is_url("http://example.com"))
        self.assertTrue(self.scraper.is_url("https://example.com"))
        self.assertFalse(self.scraper.is_url("example.com"))
        self.assertFalse(self.scraper.is_url("not a url"))

if __name__ == "__main__":
    unittest.main()
