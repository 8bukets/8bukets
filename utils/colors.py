import sys
import os

class Colors:
    """
    ANSI color codes for terminal output.
    Respects FORCE_COLOR env var and isatty().
    """
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def _is_enabled():
        """
        Check if colors should be enabled.
        Returns True if FORCE_COLOR is set (regardless of value) OR if stdout is a TTY.
        """
        if os.environ.get('FORCE_COLOR'):
            return True
        return sys.stdout.isatty()

    @classmethod
    def style(cls, text: str, color_code: str) -> str:
        """Apply a color code to text if colors are enabled."""
        if cls._is_enabled():
            return f"{color_code}{text}{cls.ENDC}"
        return text

    # Convenience methods for common styles
    @classmethod
    def header(cls, text: str) -> str: return cls.style(text, cls.HEADER)
    @classmethod
    def blue(cls, text: str) -> str: return cls.style(text, cls.BLUE)
    @classmethod
    def cyan(cls, text: str) -> str: return cls.style(text, cls.CYAN)
    @classmethod
    def green(cls, text: str) -> str: return cls.style(text, cls.GREEN)
    @classmethod
    def warning(cls, text: str) -> str: return cls.style(text, cls.WARNING)
    @classmethod
    def fail(cls, text: str) -> str: return cls.style(text, cls.FAIL)
    @classmethod
    def bold(cls, text: str) -> str: return cls.style(text, cls.BOLD)
