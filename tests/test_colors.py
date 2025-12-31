import unittest
import os
import sys
from utils.colors import Colors
from unittest.mock import patch

class TestColors(unittest.TestCase):
    def test_style_enabled_by_tty(self):
        """Test that style adds codes when isatty is True and FORCE_COLOR is unset."""
        with patch('sys.stdout.isatty', return_value=True):
            with patch.dict(os.environ, {}, clear=True):
                result = Colors.style("test", Colors.BLUE)
                self.assertEqual(result, f"{Colors.BLUE}test{Colors.ENDC}")

    def test_style_disabled_by_no_tty(self):
        """Test that style returns raw text when isatty is False."""
        with patch('sys.stdout.isatty', return_value=False):
            with patch.dict(os.environ, {}, clear=True):
                result = Colors.style("test", Colors.BLUE)
                self.assertEqual(result, "test")

    def test_style_enabled_by_force_color(self):
        """Test that FORCE_COLOR overrides isatty=False."""
        with patch('sys.stdout.isatty', return_value=False):
            with patch.dict(os.environ, {'FORCE_COLOR': '1'}):
                result = Colors.style("test", Colors.BLUE)
                self.assertEqual(result, f"{Colors.BLUE}test{Colors.ENDC}")

    def test_convenience_methods(self):
        """Test convenience methods like .green(), .fail()."""
        # Ensure enabled
        with patch('sys.stdout.isatty', return_value=True):
            with patch.dict(os.environ, {}, clear=True):
                self.assertEqual(Colors.green("ok"), f"{Colors.GREEN}ok{Colors.ENDC}")
                self.assertEqual(Colors.fail("err"), f"{Colors.FAIL}err{Colors.ENDC}")

if __name__ == '__main__':
    unittest.main()
