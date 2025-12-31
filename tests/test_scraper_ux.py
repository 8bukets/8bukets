import unittest
from io import StringIO
import sys
from unittest.mock import patch, MagicMock
from scraper import Colors, MarkPositionScraperAsync

class TestColors(unittest.TestCase):
    def test_colors_stripped_if_not_tty(self):
        # Force not tty
        with patch('sys.stdout.isatty', return_value=False), \
             patch('os.environ.get', return_value=None):
            self.assertEqual(Colors.style("text", Colors.FAIL), "text")

    def test_colors_applied_if_force_color(self):
        # Force color env var
        with patch('sys.stdout.isatty', return_value=False), \
             patch('os.environ.get', return_value='1'):
            self.assertNotEqual(Colors.style("text", Colors.FAIL), "text")
            self.assertIn(Colors.FAIL, Colors.style("text", Colors.FAIL))

class TestScraperUX(unittest.TestCase):
    def test_summary_output(self):
        scraper = MarkPositionScraperAsync("json", "csv", "txt")
        stats = {
            "posts": 100,
            "unique_links": 50,
            "json": "test.json",
            "csv": "test.csv"
        }

        captured_output = StringIO()
        sys.stdout = captured_output
        try:
            scraper.print_summary(stats, 1.23)
        finally:
            sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        self.assertIn("Scrape Complete!", output)
        self.assertIn("100", output)
        self.assertIn("50", output)
        self.assertIn("1.23s", output)

if __name__ == '__main__':
    unittest.main()
