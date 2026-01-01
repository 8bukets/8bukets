import logging
import copy

class Colors:
    RESET = "\033[0m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BOLD = "\033[1m"

class ColoredFormatter(logging.Formatter):
    LEVEL_COLORS = {
        logging.DEBUG: Colors.BLUE,
        logging.INFO: Colors.GREEN,
        logging.WARNING: Colors.YELLOW,
        logging.ERROR: Colors.RED,
        logging.CRITICAL: Colors.MAGENTA + Colors.BOLD,
    }

    LEVEL_EMOJIS = {
        logging.DEBUG: "🐛",
        logging.INFO: "ℹ️",
        logging.WARNING: "⚠️",
        logging.ERROR: "❌",
        logging.CRITICAL: "🚨",
    }

    def format(self, record):
        # Create a shallow copy to prevent side effects on other handlers
        record = copy.copy(record)

        color = self.LEVEL_COLORS.get(record.levelno, Colors.WHITE)
        emoji = self.LEVEL_EMOJIS.get(record.levelno, "")

        # Colorize levelname
        record.levelname = f"{color}{emoji} {record.levelname:<8}{Colors.RESET}"

        # Colorize message for severe errors
        if record.levelno >= logging.ERROR:
            record.msg = f"{color}{record.msg}{Colors.RESET}"

        return super().format(record)
