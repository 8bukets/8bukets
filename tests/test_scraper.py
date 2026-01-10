import unittest
from scraper import MarkPositionScraperAsync

class TestScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = MarkPositionScraperAsync("dummy.json", "dummy.csv", "dummy.txt")

    def test_clean_text_normal(self):
        text = "Hello World"
        self.assertEqual(self.scraper.clean_text(text), "Hello World")

    def test_clean_text_whitespace(self):
        text = "  Hello   World  "
        self.assertEqual(self.scraper.clean_text(text), "Hello World")

    def test_clean_text_newlines_tabs(self):
        text = "Hello\nWorld\tTest"
        self.assertEqual(self.scraper.clean_text(text), "Hello World Test")

    def test_clean_text_nbsp(self):
        text = "Hello\xa0World"
        self.assertEqual(self.scraper.clean_text(text), "Hello World")

    def test_clean_text_empty(self):
        self.assertEqual(self.scraper.clean_text(""), "")
        self.assertEqual(self.scraper.clean_text(None), "")

    def test_clean_text_complex(self):
        text = "  Multi\nLine\t\xa0String  "
        self.assertEqual(self.scraper.clean_text(text), "Multi Line String")

if __name__ == '__main__':
    unittest.main()
