import unittest
from scraper import OracleNewsScraper

class TestScraperFunc(unittest.TestCase):
    def setUp(self):
        self.scraper = OracleNewsScraper("dummy.json", "dummy.csv", "dummy.txt")

    def test_clean_text_basic(self):
        self.assertEqual(self.scraper.clean_text("  hello   world  "), "hello world")

    def test_clean_text_tabs_newlines(self):
        self.assertEqual(self.scraper.clean_text("hello\tworld\n\nagain"), "hello world again")

    def test_clean_text_non_breaking_space(self):
        self.assertEqual(self.scraper.clean_text("hello\xa0world"), "hello world")

    def test_clean_text_none(self):
        self.assertEqual(self.scraper.clean_text(None), "")

    def test_clean_text_empty(self):
        self.assertEqual(self.scraper.clean_text(""), "")

if __name__ == '__main__':
    unittest.main()
