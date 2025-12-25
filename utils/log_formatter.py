import logging
import sys

# ANSI Colors
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
GREY = "\033[90m"

# Emojis for levels
LEVEL_EMOJIS = {
    logging.DEBUG: "🐛",
    logging.INFO: "ℹ️ ",
    logging.WARNING: "⚠️ ",
    logging.ERROR: "❌",
    logging.CRITICAL: "🚨"
}

# Colors for levels
LEVEL_COLORS = {
    logging.DEBUG: GREY,
    logging.INFO: BLUE,
    logging.WARNING: YELLOW,
    logging.ERROR: RED,
    logging.CRITICAL: RED + BOLD
}

class ColorFormatter(logging.Formatter):
    def format(self, record):
        color = LEVEL_COLORS.get(record.levelno, WHITE)
        emoji = LEVEL_EMOJIS.get(record.levelno, "")

        # Format Timestamp
        asctime = self.formatTime(record, self.datefmt)

        # Format Name
        name = record.name
        if "Agent" in name:
            name_color = MAGENTA
        elif "Orchestrator" in name:
            name_color = CYAN
        elif "scraper" in name or "main" in name:
            name_color = GREEN
        else:
            name_color = WHITE

        name_fmt = f"{name_color}{name}{RESET}"

        # Format Level
        # We pad the levelname to align, but we need to strip colors for length calc if we care about strict alignment.
        # For simplicity, we just dump it.
        levelname = f"{color}{emoji} {record.levelname}{RESET}"

        # Format Message
        message = record.getMessage()

        # Structure: TIME | NAME | LEVEL | MESSAGE
        return f"{GREY}{asctime}{RESET} | {name_fmt} | {levelname} | {message}"

def setup_logging(level=logging.INFO):
    """
    Sets up the logging configuration with ColorFormatter.
    """
    formatter = ColorFormatter(datefmt='%H:%M:%S')

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    # Get the root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(level)

    # Remove existing handlers to avoid duplicates
    if root_logger.hasHandlers():
        root_logger.handlers.clear()

    root_logger.addHandler(handler)
