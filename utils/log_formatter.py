import logging

class ColorFormatter(logging.Formatter):
    """
    Custom formatter to add colors and emojis to log messages based on level.
    """

    # ANSI escape codes
    GREY = "\x1b[38;20m"
    GREEN = "\x1b[32;20m"
    YELLOW = "\x1b[33;20m"
    RED = "\x1b[31;20m"
    BOLD_RED = "\x1b[31;1m"
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

    def __init__(self, fmt=None, datefmt=None, style='%'):
        super().__init__(fmt or self.FORMAT, datefmt, style)
        self.FORMATS = {
            logging.DEBUG: self.GREY + self.EMOJIS[logging.DEBUG] + " %(asctime)s - %(levelname)s - %(message)s" + self.RESET,
            logging.INFO: self.GREEN + self.EMOJIS[logging.INFO] + " %(asctime)s - %(levelname)s - %(message)s" + self.RESET,
            logging.WARNING: self.YELLOW + self.EMOJIS[logging.WARNING] + " %(asctime)s - %(levelname)s - %(message)s" + self.RESET,
            logging.ERROR: self.RED + self.EMOJIS[logging.ERROR] + " %(asctime)s - %(levelname)s - %(message)s" + self.RESET,
            logging.CRITICAL: self.BOLD_RED + self.EMOJIS[logging.CRITICAL] + " %(asctime)s - %(levelname)s - %(message)s" + self.RESET
        }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt='%H:%M:%S')
        return formatter.format(record)
