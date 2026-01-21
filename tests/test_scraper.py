import unittest
from scraper import MarkPositionScraperAsync

class TestScraper(unittest.TestCase):

    def setUp(self):
        self.scraper = MarkPositionScraperAsync("dummy.json", "dummy.csv", "dummy.txt")

    def test_sanitize_for_csv_safe(self):
        """Test strings that don't need escaping."""
        self.assertEqual(self.scraper.sanitize_for_csv("Normal Title"), "Normal Title")
        self.assertEqual(self.scraper.sanitize_for_csv("12345"), "12345")
        self.assertEqual(self.scraper.sanitize_for_csv(""), "")
        self.assertEqual(self.scraper.sanitize_for_csv(None), "")

    def test_sanitize_for_csv_vulnerable(self):
        """Test strings that trigger CSV injection and need escaping."""
        self.assertEqual(self.scraper.sanitize_for_csv("=1+1"), "'=1+1")
        self.assertEqual(self.scraper.sanitize_for_csv("+1+1"), "'+1+1")
        self.assertEqual(self.scraper.sanitize_for_csv("-1+1"), "'-1+1")
        self.assertEqual(self.scraper.sanitize_for_csv("@cmd"), "'@cmd")

    def test_sanitize_for_csv_mixed(self):
        """Test strings containing triggers but not at start."""
        self.assertEqual(self.scraper.sanitize_for_csv("Title with = sign"), "Title with = sign")

if __name__ == '__main__':
    unittest.main()
