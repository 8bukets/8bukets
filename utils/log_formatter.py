import logging
import sys

class ColorFormatter(logging.Formatter):
    """
    Custom formatter to add colors and emojis to log levels.
    """
    grey = "\x1b[38;5;240m"
    cyan = "\x1b[36m"
    green = "\x1b[32m"
    yellow = "\x1b[33m"
    red = "\x1b[31m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    def __init__(self, fmt):
        super().__init__()
        self.fmt = fmt
        self.FORMATS = {
            logging.DEBUG: self.grey + "🐛 " + self.fmt + self.reset,
            logging.INFO: self.green + "ℹ️  " + self.fmt + self.reset,
            logging.WARNING: self.yellow + "⚠️  " + self.fmt + self.reset,
            logging.ERROR: self.red + "❌ " + self.fmt + self.reset,
            logging.CRITICAL: self.bold_red + "🚨 " + self.fmt + self.reset
        }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt='%H:%M:%S')
        return formatter.format(record)

def setup_colored_logging(level=logging.INFO):
    """
    Sets up the root logger with ColorFormatter.
    This replaces basicConfig and ensures all loggers inherit this formatting.
    """
    root_logger = logging.getLogger()
    root_logger.setLevel(level)

    # Remove existing handlers to avoid duplicates
    if root_logger.handlers:
        for handler in root_logger.handlers:
            root_logger.removeHandler(handler)

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(level)

    # Standard format
    fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    ch.setFormatter(ColorFormatter(fmt))

    root_logger.addHandler(ch)
