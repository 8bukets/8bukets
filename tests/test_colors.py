import unittest
import sys
import os
from io import StringIO
from utils.colors import Colors

class TestColors(unittest.TestCase):
    def test_colors_tty(self):
        """Test that colors are applied when TTY is detected or FORCE_COLOR is set."""
        # Mock sys.stdout.isatty to return True
        original_isatty = sys.stdout.isatty
        sys.stdout.isatty = lambda: True

        try:
            text = "Hello"
            colored_text = Colors.success(text)
            self.assertIn(Colors.OKGREEN, colored_text)
            self.assertIn(Colors.ENDC, colored_text)
            self.assertIn(text, colored_text)
        finally:
            sys.stdout.isatty = original_isatty

    def test_colors_no_tty(self):
        """Test that colors are NOT applied when no TTY and no FORCE_COLOR."""
        original_isatty = sys.stdout.isatty
        sys.stdout.isatty = lambda: False

        # Ensure FORCE_COLOR is not set
        if 'FORCE_COLOR' in os.environ:
            del os.environ['FORCE_COLOR']

        try:
            text = "Hello"
            colored_text = Colors.success(text)
            self.assertEqual(colored_text, text)
        finally:
            sys.stdout.isatty = original_isatty

    def test_force_color(self):
        """Test that FORCE_COLOR enables colors even without TTY."""
        original_isatty = sys.stdout.isatty
        sys.stdout.isatty = lambda: False

        os.environ['FORCE_COLOR'] = '1'

        try:
            text = "Hello"
            colored_text = Colors.success(text)
            self.assertIn(Colors.OKGREEN, colored_text)
        finally:
            sys.stdout.isatty = original_isatty
            if 'FORCE_COLOR' in os.environ:
                del os.environ['FORCE_COLOR']

if __name__ == '__main__':
    unittest.main()
