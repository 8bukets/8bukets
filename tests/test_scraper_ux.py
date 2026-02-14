import unittest
from io import StringIO
import sys
from unittest.mock import patch
from scrape_informatic import Colors, print_summary

class TestUX(unittest.TestCase):
    def test_colors_style(self):
        """Verify Colors.style wraps text correctly."""
        text = "Hello"
        colored = Colors.style(text, Colors.GREEN)
        self.assertEqual(colored, f"{Colors.GREEN}Hello{Colors.RESET}")

    def test_print_summary(self):
        """Verify print_summary generates expected output."""
        captured_output = StringIO()
        sys.stdout = captured_output
        print_summary(100, "test.json", 1.234)
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        self.assertIn("Scrape Complete", output)
        self.assertIn("100", output)
        self.assertIn("test.json", output)
        self.assertIn("1.23s", output)

if __name__ == '__main__':
    unittest.main()
