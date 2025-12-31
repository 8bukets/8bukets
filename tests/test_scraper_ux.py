import unittest
import sys
import os
from io import StringIO

# Add parent directory to path to import scraper
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scraper import Colors

class TestColors(unittest.TestCase):
    def test_strip_removes_ansi_codes(self):
        colored_text = f"{Colors.RED}Error{Colors.RESET}"
        self.assertEqual(Colors.strip(colored_text), "Error")

        complex_text = f"{Colors.BOLD}{Colors.BLUE}Title{Colors.RESET}"
        self.assertEqual(Colors.strip(complex_text), "Title")

    def test_constants_exist(self):
        self.assertTrue(hasattr(Colors, 'BLUE'))
        self.assertTrue(hasattr(Colors, 'GREEN'))
        self.assertTrue(hasattr(Colors, 'RED'))
        self.assertTrue(hasattr(Colors, 'BOLD'))
        self.assertTrue(hasattr(Colors, 'RESET'))

if __name__ == '__main__':
    unittest.main()
