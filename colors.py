import os
import sys
import logging

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def _is_enabled():
        # Check if running in a TTY or if FORCE_COLOR is set
        return sys.stdout.isatty() or os.environ.get('FORCE_COLOR')

    @classmethod
    def style(cls, text, *styles):
        if not cls._is_enabled():
            return text

        start = "".join(styles)
        return f"{start}{text}{cls.ENDC}"

    @classmethod
    def header(cls, text): return cls.style(text, cls.HEADER, cls.BOLD)
    @classmethod
    def info(cls, text): return cls.style(text, cls.OKCYAN)
    @classmethod
    def success(cls, text): return cls.style(text, cls.OKGREEN)
    @classmethod
    def warning(cls, text): return cls.style(text, cls.WARNING)
    @classmethod
    def error(cls, text): return cls.style(text, cls.FAIL)
    @classmethod
    def bold(cls, text): return cls.style(text, cls.BOLD)

class ColoredFormatter(logging.Formatter):
    def format(self, record):
        message = super().format(record)
        if record.levelno == logging.ERROR:
            return Colors.error(message)
        elif record.levelno == logging.WARNING:
            return Colors.warning(message)
        elif "Saved" in message or "Found" in message:
            return Colors.success(message)
        elif "Starting" in message or "Pipeline Complete" in message or "Fetching" in message:
            return Colors.header(message) if "Starting" in message or "Pipeline" in message else Colors.info(message)
        return message
