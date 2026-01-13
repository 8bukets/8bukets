import unittest
from scraper import MarkPositionScraperAsync

class TestScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = MarkPositionScraperAsync("dummy.json", "dummy.csv", "dummy.txt")

    def test_clean_text(self):
        # Test None
        self.assertEqual(self.scraper.clean_text(None), "")
        # Test empty string
        self.assertEqual(self.scraper.clean_text(""), "")
        # Test normal string
        self.assertEqual(self.scraper.clean_text("Hello World"), "Hello World")
        # Test multiple spaces
        self.assertEqual(self.scraper.clean_text("Hello   World"), "Hello World")
        # Test tabs and newlines
        self.assertEqual(self.scraper.clean_text("Hello\tWorld\n"), "Hello World")
        # Test non-breaking space
        self.assertEqual(self.scraper.clean_text("Hello\xa0World"), "Hello World")
        # Test leading/trailing whitespace
        self.assertEqual(self.scraper.clean_text("  Hello World  "), "Hello World")
        # Test combination
        self.assertEqual(self.scraper.clean_text(" \t Hello \xa0  World \n "), "Hello World")

if __name__ == '__main__':
    unittest.main()
