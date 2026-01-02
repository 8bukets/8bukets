import logging

class Colors:
    """ANSI color codes for CLI output."""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class ColoredFormatter(logging.Formatter):
    """Custom logging formatter to add colors based on log level."""

    FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    FORMATS = {
        logging.DEBUG: Colors.BLUE + FORMAT + Colors.RESET,
        logging.INFO: Colors.GREEN + "ℹ️  " + FORMAT + Colors.RESET,
        logging.WARNING: Colors.YELLOW + "⚠️  " + FORMAT + Colors.RESET,
        logging.ERROR: Colors.RED + "❌ " + FORMAT + Colors.RESET,
        logging.CRITICAL: Colors.RED + Colors.BOLD + "🚨 " + FORMAT + Colors.RESET
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt='%H:%M:%S')
        return formatter.format(record)
