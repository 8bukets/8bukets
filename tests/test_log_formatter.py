import unittest
import logging
from io import StringIO
from utils.log_formatter import ColorFormatter, Colors

class TestColorFormatter(unittest.TestCase):
    def test_formatter_adds_colors(self):
        formatter = ColorFormatter()
        record = logging.LogRecord('name', logging.INFO, 'pathname', 1, 'Test message', None, None)
        formatted_msg = formatter.format(record)

        # Check for color codes
        self.assertIn(Colors.GREEN, formatted_msg)
        self.assertIn(Colors.ENDC, formatted_msg)
        # Check for emoji
        self.assertIn("ℹ️", formatted_msg)
        # Check for message
        self.assertIn("Test message", formatted_msg)

    def test_formatter_adds_warning_emoji(self):
        formatter = ColorFormatter()
        record = logging.LogRecord('name', logging.WARNING, 'pathname', 1, 'Warning message', None, None)
        formatted_msg = formatter.format(record)

        # Check for warning emoji
        self.assertIn("⚠️", formatted_msg)
        # Check for message
        self.assertIn("Warning message", formatted_msg)

if __name__ == '__main__':
    unittest.main()
