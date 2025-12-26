import logging
import copy

class ColorFormatter(logging.Formatter):
    """
    Custom formatter that adds colors and emojis to log levels.
    """

    # ANSI escape codes
    GREY = "\x1b[90m"        # Bright Black (Grey)
    BLUE = "\x1b[34m"        # Blue
    YELLOW = "\x1b[33m"      # Yellow
    RED = "\x1b[31m"         # Red
    BOLD_RED = "\x1b[31;1m"  # Bold Red
    RESET = "\x1b[0m"

    # Emojis for each level
    EMOJIS = {
        logging.DEBUG: "🐛",
        logging.INFO: "ℹ️ ",
        logging.WARNING: "⚠️ ",
        logging.ERROR: "❌",
        logging.CRITICAL: "🚨"
    }

    FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

    FORMATS = {
        logging.DEBUG: GREY + FORMAT + RESET,
        logging.INFO: BLUE + FORMAT + RESET,
        logging.WARNING: YELLOW + FORMAT + RESET,
        logging.ERROR: RED + FORMAT + RESET,
        logging.CRITICAL: BOLD_RED + FORMAT + RESET
    }

    def __init__(self):
        super().__init__()
        self.formatters = {
            level: logging.Formatter(fmt, datefmt='%H:%M:%S')
            for level, fmt in self.FORMATS.items()
        }

    def format(self, record):
        # Create a copy of the record to avoid side effects
        record_copy = copy.copy(record)

        # Add emoji to the message if not already present
        emoji = self.EMOJIS.get(record.levelno, "")
        record_copy.msg = f"{emoji} {record_copy.msg}"

        formatter = self.formatters.get(record.levelno)
        return formatter.format(record_copy)
