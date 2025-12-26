import logging
import sys

class ColorFormatter(logging.Formatter):
    """
    Custom logging formatter to add colors and emojis to log records.
    """

    # ANSI escape codes
    GREY = "\x1b[38;20m"
    GREEN = "\x1b[32;20m"
    YELLOW = "\x1b[33;20m"
    RED = "\x1b[31;20m"
    BOLD_RED = "\x1b[31;1m"
    RESET = "\x1b[0m"

    # Emojis for log levels
    EMOJIS = {
        logging.DEBUG: "🐞",
        logging.INFO: "ℹ️ ",
        logging.WARNING: "⚠️ ",
        logging.ERROR: "❌",
        logging.CRITICAL: "🚨"
    }

    FORMATS = {
        logging.DEBUG: GREY + EMOJIS[logging.DEBUG] + " %(asctime)s - %(name)s - %(levelname)s - %(message)s" + RESET,
        logging.INFO: GREEN + EMOJIS[logging.INFO] + " %(asctime)s - %(name)s - %(levelname)s - %(message)s" + RESET,
        logging.WARNING: YELLOW + EMOJIS[logging.WARNING] + " %(asctime)s - %(name)s - %(levelname)s - %(message)s" + RESET,
        logging.ERROR: RED + EMOJIS[logging.ERROR] + " %(asctime)s - %(name)s - %(levelname)s - %(message)s" + RESET,
        logging.CRITICAL: BOLD_RED + EMOJIS[logging.CRITICAL] + " %(asctime)s - %(name)s - %(levelname)s - %(message)s" + RESET
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt='%H:%M:%S')
        return formatter.format(record)

def setup_colored_logging(level=logging.INFO):
    """
    Sets up the root logger to use ColorFormatter.
    """
    root_logger = logging.getLogger()
    root_logger.setLevel(level)

    # Remove existing handlers to avoid duplication
    if root_logger.hasHandlers():
        root_logger.handlers.clear()

    # Create console handler with custom formatter
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(ColorFormatter())

    root_logger.addHandler(console_handler)
