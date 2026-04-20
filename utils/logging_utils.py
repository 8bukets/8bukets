import logging
import sys
import copy

class Colors:
    """ANSI color codes"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def disable():
        Colors.HEADER = ''
        Colors.BLUE = ''
        Colors.CYAN = ''
        Colors.GREEN = ''
        Colors.YELLOW = ''
        Colors.RED = ''
        Colors.RESET = ''
        Colors.BOLD = ''
        Colors.UNDERLINE = ''

# Disable colors if not running in a TTY (e.g. piped to file)
if not sys.stdout.isatty():
    Colors.disable()

class ColorFormatter(logging.Formatter):
    """Custom formatter to add colors to log levels"""

    FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

    LEVEL_COLORS = {
        logging.DEBUG: Colors.BLUE,
        logging.INFO: Colors.GREEN,
        logging.WARNING: Colors.YELLOW,
        logging.ERROR: Colors.RED,
        logging.CRITICAL: Colors.RED + Colors.BOLD
    }

    def format(self, record):
        # Create a copy to avoid mutating the original record
        record_copy = copy.copy(record)

        color = self.LEVEL_COLORS.get(record_copy.levelno, Colors.RESET)

        # Apply color only to the parts we want
        record_copy.levelname = f"{color}{record_copy.levelname}{Colors.RESET}"
        record_copy.msg = f"{color}{record_copy.msg}{Colors.RESET}"

        return super().format(record_copy)
