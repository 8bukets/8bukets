import logging
import sys

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
    UNDERLINE = "\033[4m"

class UXFormatter(logging.Formatter):
    """
    Custom formatter to add colors and emojis to log messages for better UX.
    """

    FORMATS = {
        logging.DEBUG: Colors.CYAN + "🐛 %(asctime)s - %(name)s - %(levelname)s - %(message)s" + Colors.RESET,
        logging.INFO: Colors.WHITE + "ℹ️  %(asctime)s - %(name)s - %(levelname)s - %(message)s" + Colors.RESET,
        logging.WARNING: Colors.YELLOW + "⚠️  %(asctime)s - %(name)s - %(levelname)s - %(message)s" + Colors.RESET,
        logging.ERROR: Colors.RED + "❌ %(asctime)s - %(name)s - %(levelname)s - %(message)s" + Colors.RESET,
        logging.CRITICAL: Colors.RED + Colors.BOLD + "🚨 %(asctime)s - %(name)s - %(levelname)s - %(message)s" + Colors.RESET
    }

    EMOJI_MAP = {
        "starting": "🚀",
        "finished": "🏁",
        "complete": "✅",
        "saved": "💾",
        "scraped": "📥",
        "found": "🔍",
        "error": "❌",
        "warning": "⚠️",
        "analyzing": "🧠",
        "health": "🏥",
        "research": "📚",
        "intelligence": "💡",
        "advertising": "📢",
        "monetization": "💰",
        "content": "✍️",
        "creative": "🎨",
        "draft": "📝",
        "report": "📊",
        "evolution": "🧬"
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno, self.FORMATS[logging.INFO])
        formatter = logging.Formatter(log_fmt, datefmt="%H:%M:%S")

        # Add emojis based on keywords in the message
        message = record.getMessage().lower()
        emoji_prefix = ""

        for keyword, emoji in self.EMOJI_MAP.items():
            if keyword in message:
                emoji_prefix = emoji + " "
                break

        # If we found a specific emoji, use it. Otherwise, the default level emoji is already in the format string.
        # But wait, the format string has an emoji at the start.
        # Let's replace the default level emoji if we find a more specific one.

        formatted_message = formatter.format(record)

        # This is a bit tricky because we want to replace the FIRST emoji if we have a better one.
        # The default formats start with an emoji.

        if emoji_prefix:
            # Split by the first space to replace the first part (the emoji)
            parts = formatted_message.split(" ", 1)
            if len(parts) > 1:
                # We replace the default emoji (part[0]) with our specific emoji
                # But we need to keep the color code if it's there.
                # The color code is at the start of the string.

                # Let's re-construct carefully.
                # The color code is likely part of the first split if we are not careful.
                # Actually, the color code is prepended to the format string.

                # Simpler approach: Just inject the emoji into the message itself?
                # No, that modifies the message.

                # Let's just modify the record.msg temporarily? No, that's side-effect heavy.

                # Let's try to find the default emoji and replace it.
                default_emojis = ["🐛", "ℹ️", "⚠️", "❌", "🚨"]
                for default_emoji in default_emojis:
                     if default_emoji in formatted_message:
                         formatted_message = formatted_message.replace(default_emoji, emoji_prefix.strip(), 1)
                         break

        return formatted_message

def configure_ux_logging(logger_name=None, verbose=False):
    """
    Configures the logger with the UXFormatter.
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG if verbose else logging.INFO)

    # Check if handlers already exist to avoid duplicates
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(UXFormatter())
        logger.addHandler(handler)
    else:
        # If handlers exist, update their formatter
        for handler in logger.handlers:
            handler.setFormatter(UXFormatter())

    # Prevent propagation to root logger if we have a handler on this logger
    # This prevents duplicate logs if root logger also has a handler
    if logger.handlers and logger.name != "root":
        logger.propagate = False

    # Also configure the root logger to catch everything else
    root_logger = logging.getLogger()
    # Only change level if not already set or if explicitly requested (simplified here)
    if verbose:
        root_logger.setLevel(logging.DEBUG)

    if not root_logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(UXFormatter())
        root_logger.addHandler(handler)
    else:
            for handler in root_logger.handlers:
                handler.setFormatter(UXFormatter())

    return logger
