import logging

class ColorFormatter(logging.Formatter):
    grey = "\x1b[38;20m"
    cyan = "\x1b[36;20m"
    green = "\x1b[32;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    def __init__(self, include_name=False):
        super().__init__()
        self.include_name = include_name
        format_str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s" if include_name else "%(asctime)s - %(levelname)s - %(message)s"

        self.FORMATS_STR = {
            logging.DEBUG: self.grey + "🐛 " + format_str + self.reset,
            logging.INFO: self.cyan + "ℹ️  " + format_str + self.reset,
            logging.WARNING: self.yellow + "⚠️  " + format_str + self.reset,
            logging.ERROR: self.red + "❌ " + format_str + self.reset,
            logging.CRITICAL: self.bold_red + "🚨 " + format_str + self.reset
        }

        self.formatters = {
            level: logging.Formatter(fmt, datefmt='%H:%M:%S')
            for level, fmt in self.FORMATS_STR.items()
        }

    def format(self, record):
        formatter = self.formatters.get(record.levelno)
        if formatter is None:
             # Fallback for custom levels or if something is weird
             formatter = self.formatters.get(logging.INFO)
        return formatter.format(record)
