import unittest
from scraper import MarkPositionScraperAsync

class TestScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")

    def test_clean_text(self):
        inputs = [
            ("  hello   world  ", "hello world"),
            ("foo\nbar", "foo bar"),
            ("test\xa0string", "test string"),
            ("", ""),
            (None, ""),
            ("   ", "")
        ]

        for text, expected in inputs:
            with self.subTest(text=text):
                self.assertEqual(self.scraper.clean_text(text), expected)

if __name__ == '__main__':
    unittest.main()
