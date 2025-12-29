import unittest
import logging
import sys
import re
from utils.colors import ColoredFormatter, Colors

class TestColoredFormatter(unittest.TestCase):
    def setUp(self):
        self.formatter = ColoredFormatter()

    def test_format_basic(self):
        record = logging.LogRecord(
            name="TestAgent",
            level=logging.INFO,
            pathname=__file__,
            lineno=10,
            msg="Test message",
            args=(),
            exc_info=None
        )
        output = self.formatter.format(record)

        # Check for presence of ANSI codes
        self.assertIn(Colors.GREEN, output)
        self.assertIn(Colors.RESET, output)

        # Check for message
        self.assertIn("Test message", output)

        # Check for default emoji
        self.assertIn("🤖", output)

    def test_format_known_agent(self):
        record = logging.LogRecord(
            name="Researcher",
            level=logging.INFO,
            pathname=__file__,
            lineno=10,
            msg="Scraping",
            args=(),
            exc_info=None
        )
        output = self.formatter.format(record)

        # Check for Researcher emoji
        self.assertIn("🔍", output)

    def test_format_exception(self):
        try:
            1 / 0
        except ZeroDivisionError:
            exc_info = sys.exc_info()

        record = logging.LogRecord(
            name="TestAgent",
            level=logging.ERROR,
            pathname=__file__,
            lineno=10,
            msg="Error occurred",
            args=(),
            exc_info=exc_info
        )
        output = self.formatter.format(record)

        self.assertIn("Error occurred", output)
        self.assertIn("ZeroDivisionError", output)
        self.assertIn("division by zero", output)

if __name__ == "__main__":
    import sys
    unittest.main()
