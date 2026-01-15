
import unittest
import sys
import os

# Add parent directory to path to import scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import MarkPositionScraperAsync

class TestScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = MarkPositionScraperAsync("links.json", "links.csv", "unique_links.txt")

    def test_clean_text_normal(self):
        text = "  Hello   World  "
        self.assertEqual(self.scraper.clean_text(text), "Hello World")

    def test_clean_text_newlines(self):
        text = "Hello\nWorld"
        self.assertEqual(self.scraper.clean_text(text), "Hello World")

    def test_clean_text_tabs(self):
        text = "Hello\tWorld"
        self.assertEqual(self.scraper.clean_text(text), "Hello World")

    def test_clean_text_nbsps(self):
        text = "Hello\xa0World"
        self.assertEqual(self.scraper.clean_text(text), "Hello World")

    def test_clean_text_mixed(self):
        text = "  Hello \n \t \xa0 World  "
        self.assertEqual(self.scraper.clean_text(text), "Hello World")

    def test_clean_text_empty(self):
        self.assertEqual(self.scraper.clean_text(""), "")
        self.assertEqual(self.scraper.clean_text(None), "")

    def test_is_url_http(self):
        self.assertTrue(self.scraper.is_url("http://example.com"))

    def test_is_url_https(self):
        self.assertTrue(self.scraper.is_url("https://example.com"))

    def test_is_url_invalid(self):
        self.assertFalse(self.scraper.is_url("example.com"))
        self.assertFalse(self.scraper.is_url("ftp://example.com"))
        self.assertFalse(self.scraper.is_url("Not a URL"))

if __name__ == '__main__':
    unittest.main()
