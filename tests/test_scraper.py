import unittest
from unittest.mock import patch
import io
import os
from scraper import Colors, print_summary


class TestUX(unittest.TestCase):
    def test_colors_style_tty(self):
        """Test that colors are applied when stdout is a TTY."""
        with patch('sys.stdout.isatty', return_value=True):
            result = Colors.style("test", Colors.GREEN)
            self.assertEqual(result, f"{Colors.GREEN}test{Colors.ENDC}")

    def test_colors_style_no_tty(self):
        """Test that colors are NOT applied when stdout is NOT a TTY."""
        with patch('sys.stdout.isatty', return_value=False):
            # Also ensure FORCE_COLOR is not set
            with patch.dict(os.environ, {}, clear=True):
                result = Colors.style("test", Colors.GREEN)
                self.assertEqual(result, "test")

    def test_colors_style_force_color(self):
        """Test that colors ARE applied when FORCE_COLOR is set."""
        with patch('sys.stdout.isatty', return_value=False):
            with patch.dict(os.environ, {'FORCE_COLOR': '1'}):
                result = Colors.style("test", Colors.GREEN)
                self.assertEqual(result, f"{Colors.GREEN}test{Colors.ENDC}")

    def test_print_summary(self):
        """Test that summary prints correctly."""
        captured_output = io.StringIO()
        with patch('sys.stdout', new=captured_output):
            # Force no color for simpler string comparison
            with patch('sys.stdout.isatty', return_value=False):
                with patch.dict(os.environ, {}, clear=True):
                    print_summary(100, 50, 1.234)

        output = captured_output.getvalue()
        self.assertIn("SCRAPE COMPLETED SUCCESSFULLY", output)
        self.assertIn("Posts Scraped:    100", output)
        self.assertIn("Unique Links:     50", output)
        self.assertIn("Time Taken:       1.23s", output)


if __name__ == '__main__':
    unittest.main()
