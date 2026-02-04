import unittest
import logging
import sys
import os

# Add parent directory to path so we can import scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import UXFormatter

class TestUXFormatter(unittest.TestCase):
    def test_info_formatting(self):
        formatter = UXFormatter()
        record = logging.LogRecord(
            name="test", level=logging.INFO, pathname=__file__, lineno=10,
            msg="Fetching data", args=(), exc_info=None
        )
        output = formatter.format(record)
        # Check for Blue color code and info emoji
        self.assertIn("\033[94m", output)
        self.assertIn("ℹ️", output)
        self.assertIn("Fetching data", output)

    def test_success_formatting(self):
        formatter = UXFormatter()
        record = logging.LogRecord(
            name="test", level=logging.INFO, pathname=__file__, lineno=10,
            msg="Saved 10 posts", args=(), exc_info=None
        )
        output = formatter.format(record)
        # Check for Green color code and checkmark emoji
        self.assertIn("\033[92m", output)
        self.assertIn("✅", output)
        self.assertIn("Saved 10 posts", output)

    def test_warning_formatting(self):
        formatter = UXFormatter()
        record = logging.LogRecord(
            name="test", level=logging.WARNING, pathname=__file__, lineno=10,
            msg="Something suspicious", args=(), exc_info=None
        )
        output = formatter.format(record)
        # Check for Yellow color code and warning emoji
        self.assertIn("\033[93m", output)
        self.assertIn("⚠️", output)

    def test_error_formatting(self):
        formatter = UXFormatter()
        record = logging.LogRecord(
            name="test", level=logging.ERROR, pathname=__file__, lineno=10,
            msg="Fatal error", args=(), exc_info=None
        )
        output = formatter.format(record)
        # Check for Red color code and error emoji
        self.assertIn("\033[91m", output)
        self.assertIn("❌", output)

if __name__ == '__main__':
    unittest.main()
