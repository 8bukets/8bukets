import logging

class ColorFormatter(logging.Formatter):
    """
    Custom formatter to add colors and emojis to log levels.
    """
    GREY = "\x1b[38;20m"
    GREEN = "\x1b[32;20m"
    YELLOW = "\x1b[33;20m"
    RED = "\x1b[31;20m"
    BOLD_RED = "\x1b[31;1m"
    RESET = "\x1b[0m"

    def format(self, record):
        emoji = ""
        color = self.RESET

        if record.levelno == logging.INFO:
            emoji = "✨ "
            color = self.GREEN
        elif record.levelno == logging.WARNING:
            emoji = "⚠️  "
            color = self.YELLOW
        elif record.levelno == logging.ERROR:
            emoji = "❌ "
            color = self.RED
        elif record.levelno == logging.CRITICAL:
            emoji = "🚨 "
            color = self.BOLD_RED
        elif record.levelno == logging.DEBUG:
            emoji = "🐛 "
            color = self.GREY

        # Format: Time - Name - Level - Message
        # Using the standard format but injecting color and emoji
        log_fmt = f"{color}%(asctime)s - %(name)s - {emoji}%(levelname)s - %(message)s{self.RESET}"
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)
