import os
import sys

class Colors:
    """ANSI color codes for terminal output."""
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
    def style(text: str, color: str) -> str:
        """Apply a color to the text if stdout is a TTY or FORCE_COLOR is set."""
        if sys.stdout.isatty() or os.environ.get('FORCE_COLOR'):
            return f"{color}{text}{Colors.ENDC}"
        return text

    @staticmethod
    def success(text: str) -> str:
        return Colors.style(text, Colors.OKGREEN)

    @staticmethod
    def fail(text: str) -> str:
        return Colors.style(text, Colors.FAIL)

    @staticmethod
    def warning(text: str) -> str:
        return Colors.style(text, Colors.WARNING)

    @staticmethod
    def info(text: str) -> str:
        return Colors.style(text, Colors.OKCYAN)

    @staticmethod
    def header(text: str) -> str:
        return Colors.style(text, Colors.HEADER)

    @staticmethod
    def underline(text: str) -> str:
        return Colors.style(text, Colors.UNDERLINE)
