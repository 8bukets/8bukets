import logging
import sys
import os

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

class ColoredFormatter(logging.Formatter):
    COLORS = {
        'DEBUG': Colors.BLUE,
        'INFO': Colors.GREEN,
        'WARNING': Colors.WARNING,
        'ERROR': Colors.FAIL,
        'CRITICAL': Colors.FAIL + Colors.BOLD,
    }

    def format(self, record):
        message = super().format(record)
        # Check if we should colorize
        # Colorize if stdout is a TTY OR if FORCE_COLOR is set
        if not sys.stderr.isatty() and not os.environ.get('FORCE_COLOR'):
             return message

        log_color = self.COLORS.get(record.levelname, Colors.ENDC)
        return f"{log_color}{message}{Colors.ENDC}"
