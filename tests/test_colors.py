import unittest
import logging
from colors import ColoredFormatter, Colors

class TestColors(unittest.TestCase):
    def test_colors_exist(self):
        self.assertTrue(hasattr(Colors, 'RED'))
        self.assertTrue(hasattr(Colors, 'GREEN'))
        self.assertTrue(hasattr(Colors, 'RESET'))

    def test_formatter_formats(self):
        formatter = ColoredFormatter('%(levelname)s - %(message)s')
        record = logging.LogRecord('name', logging.INFO, 'pathname', 1, 'msg', (), None)
        formatted = formatter.format(record)

        # Check if emoji is present
        self.assertIn("ℹ️", formatted)
        # Check if color code is present (INFO is GREEN)
        self.assertIn(Colors.GREEN, formatted)
        # Check if reset code is present
        self.assertIn(Colors.RESET, formatted)

    def test_formatter_error(self):
        formatter = ColoredFormatter('%(levelname)s - %(message)s')
        record = logging.LogRecord('name', logging.ERROR, 'pathname', 1, 'error msg', (), None)
        formatted = formatter.format(record)

        # Check if emoji is present
        self.assertIn("❌", formatted)
        # Check if color code is present (ERROR is RED)
        self.assertIn(Colors.RED, formatted)
        # Check if message is colored for ERROR
        self.assertIn(Colors.RED + 'error msg', formatted)

if __name__ == '__main__':
    unittest.main()
