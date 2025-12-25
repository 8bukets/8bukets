import unittest
import sys
from unittest.mock import MagicMock

# Mock dependencies that might be missing
sys.modules['aiohttp'] = MagicMock()
sys.modules['bs4'] = MagicMock()

from scraper import MarkPositionScraperAsync

class TestScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = MarkPositionScraperAsync("links.json", "links.csv", "unique_links.txt")

    def test_clean_text(self):
        self.assertEqual(self.scraper.clean_text("  hello   world  "), "hello world")
        self.assertEqual(self.scraper.clean_text("hello\xa0world"), "hello world")
        self.assertEqual(self.scraper.clean_text(""), "")
        self.assertEqual(self.scraper.clean_text(None), "")
        self.assertEqual(self.scraper.clean_text("\n\t  mixed \n whitespace  "), "mixed whitespace")

if __name__ == '__main__':
    unittest.main()
