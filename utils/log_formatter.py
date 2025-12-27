import logging

class ColorFormatter(logging.Formatter):
    """Logging formatter with colors and emojis."""

    grey = "\x1b[38;20m"
    blue = "\x1b[34;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    # Emojis for visual scanning
    ICONS = {
        logging.DEBUG: "🐛",
        logging.INFO: "🔹",
        logging.WARNING: "⚠️ ",
        logging.ERROR: "❌",
        logging.CRITICAL: "🚨"
    }

    COLORS = {
        logging.DEBUG: grey,
        logging.INFO: blue,
        logging.WARNING: yellow,
        logging.ERROR: red,
        logging.CRITICAL: bold_red,
    }

    def format(self, record):
        log_fmt = f"%(asctime)s {self.ICONS.get(record.levelno, '')}  %(name)s: %(message)s"
        formatter = logging.Formatter(log_fmt, datefmt='%H:%M:%S')

        # Add color to the entire line based on level
        color = self.COLORS.get(record.levelno, self.grey)
        formatted_message = formatter.format(record)
        return f"{color}{formatted_message}{self.reset}"
