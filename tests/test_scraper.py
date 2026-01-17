import unittest
from scraper import Colors, MarkPositionScraperAsync
import sys
import io

class TestScraperUX(unittest.TestCase):
    def test_colors_enable(self):
        # Test that Colors.enable doesn't crash
        Colors.enable()
        # We can't easily test isatty here without mocking, but we can check if attributes exist
        self.assertTrue(hasattr(Colors, 'HEADER'))
        self.assertTrue(hasattr(Colors, 'GREEN'))

    def test_print_summary(self):
        scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            scraper.print_summary(100, 50, 1.23)
            output = captured_output.getvalue()
            self.assertIn("Scraper Summary", output)
            self.assertIn("Total Posts:", output)
            self.assertIn("100", output)
            self.assertIn("1.23 seconds", output)
        finally:
            sys.stdout = sys.__stdout__

if __name__ == '__main__':
    unittest.main()
