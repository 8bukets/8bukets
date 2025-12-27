import logging
import sys

# ANSI escape codes for colors
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class ColorFormatter(logging.Formatter):
    """
    A custom logging formatter that adds colors and emojis to log messages based on severity.
    """

    FORMAT = "%(asctime)s %(message)s"

    LEVEL_STYLES = {
        logging.DEBUG: (Colors.BLUE, "🐛"),
        logging.INFO: (Colors.GREEN, "ℹ️ "),
        logging.WARNING: (Colors.WARNING, "⚠️ "),
        logging.ERROR: (Colors.FAIL, "❌"),
        logging.CRITICAL: (Colors.FAIL + Colors.BOLD, "🚨")
    }

    def format(self, record):
        # Determine style
        style, emoji = self.LEVEL_STYLES.get(record.levelno, (Colors.ENDC, ""))

        # Format the timestamp
        record.asctime = self.formatTime(record, self.datefmt)

        # Format the message (handling arguments)
        message = record.getMessage()

        # Construct the colored message
        # Format: [TIME] [EMOJI] Message
        formatted_msg = f"{Colors.CYAN}{record.asctime}{Colors.ENDC} {emoji} {style}{message}{Colors.ENDC}"

        # Append exception info if present
        if record.exc_info:
            # Cache the traceback text to avoid formatting it multiple times
            if not record.exc_text:
                record.exc_text = self.formatException(record.exc_info)

        if record.exc_text:
            formatted_msg += "\n" + record.exc_text

        return formatted_msg

def setup_colored_logging():
    """
    Configures the root logger to use the ColorFormatter.
    """
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Check if handlers already exist to avoid duplicates
    if logger.hasHandlers():
        logger.handlers.clear()

    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(ColorFormatter(datefmt='%H:%M:%S'))
    logger.addHandler(handler)
