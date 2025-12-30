import unittest
import sys
import os
from unittest.mock import patch
from scraper import Colors

class TestColors(unittest.TestCase):
    def test_colors_attributes(self):
        """Test that color constants are defined correctly."""
        self.assertEqual(Colors.HEADER, '\033[95m')
        self.assertEqual(Colors.BLUE, '\033[94m')
        self.assertEqual(Colors.ENDC, '\033[0m')

    def test_style_with_force_color(self):
        """Test styling when FORCE_COLOR is set."""
        with patch.dict(os.environ, {'FORCE_COLOR': '1'}):
            text = "Hello"
            styled = Colors.style(text, Colors.BOLD, Colors.GREEN)
            self.assertEqual(styled, f"{Colors.BOLD}{Colors.GREEN}Hello{Colors.ENDC}")

    def test_style_no_tty_no_force_color(self):
        """Test styling when not a TTY and FORCE_COLOR is not set."""
        # Mock sys.stdout.isatty to return False
        with patch('sys.stdout.isatty', return_value=False):
            # Ensure FORCE_COLOR is not set
            with patch.dict(os.environ, {}, clear=True):
                text = "Hello"
                styled = Colors.style(text, Colors.BOLD)
                # Should return plain text
                self.assertEqual(styled, text)

if __name__ == '__main__':
    unittest.main()
