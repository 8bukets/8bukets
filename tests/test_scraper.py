import unittest
from scraper import OracleNewsScraper

class TestOracleNewsScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = OracleNewsScraper("test.json", "test.csv", "test.txt")

    def test_clean_text_normal(self):
        self.assertEqual(self.scraper.clean_text("Hello World"), "Hello World")

    def test_clean_text_multiple_spaces(self):
        self.assertEqual(self.scraper.clean_text("Hello   World"), "Hello World")

    def test_clean_text_non_breaking_space(self):
        self.assertEqual(self.scraper.clean_text("Hello\xa0World"), "Hello World")

    def test_clean_text_mixed_whitespace(self):
        self.assertEqual(self.scraper.clean_text("Hello \xa0  World"), "Hello World")

    def test_clean_text_newlines_tabs(self):
        self.assertEqual(self.scraper.clean_text("Hello\nWorld\t!"), "Hello World !")

    def test_clean_text_leading_trailing(self):
        self.assertEqual(self.scraper.clean_text("  Hello World  "), "Hello World")

    def test_clean_text_none(self):
        self.assertEqual(self.scraper.clean_text(None), "")

    def test_clean_text_empty(self):
        self.assertEqual(self.scraper.clean_text(""), "")

if __name__ == '__main__':
    unittest.main()
