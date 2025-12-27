import unittest
from scraper import MarkPositionScraperAsync

class TestScraperUtils(unittest.TestCase):
    def setUp(self):
        self.scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")

    def test_clean_text(self):
        # Basic space
        self.assertEqual(self.scraper.clean_text("  hello   world  "), "hello world")
        # Tabs and newlines
        self.assertEqual(self.scraper.clean_text("hello\tworld\n"), "hello world")
        # Non-breaking space
        self.assertEqual(self.scraper.clean_text("hello\xa0world"), "hello world")
        # Empty
        self.assertEqual(self.scraper.clean_text(""), "")
        self.assertEqual(self.scraper.clean_text(None), "")
        # All whitespace
        self.assertEqual(self.scraper.clean_text("   \n\t   "), "")
        # Interleaved
        self.assertEqual(self.scraper.clean_text(" a \n b \t c "), "a b c")

if __name__ == '__main__':
    unittest.main()
