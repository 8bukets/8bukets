import unittest
from unittest.mock import patch, MagicMock
from scraper import OracleNewsScraper, Colors, print_summary
import os
import sys

class TestScraperColors(unittest.TestCase):
    def test_colors_stripped(self):
        text = "\033[32mHello\033[0m"
        self.assertEqual(Colors.strip(text), "Hello")

    @patch('sys.stdout.isatty', return_value=True)
    def test_style_tty(self, mock_isatty):
        text = "Hello"
        styled = Colors.style(text, Colors.GREEN)
        self.assertIn(Colors.GREEN, styled)
        self.assertIn(Colors.RESET, styled)

    @patch('sys.stdout.isatty', return_value=False)
    @patch.dict(os.environ, {'FORCE_COLOR': '1'})
    def test_style_force_color(self, mock_isatty):
        text = "Hello"
        styled = Colors.style(text, Colors.GREEN)
        self.assertIn(Colors.GREEN, styled)

    @patch('sys.stdout.isatty', return_value=False)
    @patch.dict(os.environ, {}, clear=True)
    def test_style_no_color(self, mock_isatty):
        text = "Hello"
        styled = Colors.style(text, Colors.GREEN)
        self.assertEqual(styled, "Hello")

if __name__ == '__main__':
    unittest.main()
