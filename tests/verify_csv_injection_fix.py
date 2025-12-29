import unittest
import csv
import os
import sys

# Add root to path to import scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scraper import MarkPositionScraperAsync

class TestCSVInjectionFix(unittest.TestCase):
    def test_sanitize_csv_field(self):
        scraper = MarkPositionScraperAsync("dummy.json", "dummy.csv", "dummy.txt")

        # Test cases requiring sanitization
        self.assertEqual(scraper.sanitize_csv_field("=SUM(1+1)"), "'=SUM(1+1)")
        self.assertEqual(scraper.sanitize_csv_field("+12345"), "'+12345")
        self.assertEqual(scraper.sanitize_csv_field("-12345"), "'-12345")
        self.assertEqual(scraper.sanitize_csv_field("@example"), "'@example")

        # Test cases NOT requiring sanitization
        self.assertEqual(scraper.sanitize_csv_field("Normal Text"), "Normal Text")
        self.assertEqual(scraper.sanitize_csv_field("12345"), "12345")
        self.assertEqual(scraper.sanitize_csv_field(""), "")
        self.assertEqual(scraper.sanitize_csv_field(None), "")

if __name__ == '__main__':
    unittest.main()
