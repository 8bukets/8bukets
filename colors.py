import os
import sys

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

def colorize(text: str, color_code: str) -> str:
    """
    Applies color to text if supported by the environment.
    Respects FORCE_COLOR and NO_COLOR environment variables.
    """
    if os.environ.get('NO_COLOR'):
        return text

    # Check if connected to a terminal or FORCE_COLOR is set
    # Using sys.stdout because typical usage is print()
    if sys.stdout.isatty() or os.environ.get('FORCE_COLOR'):
        return f"{color_code}{text}{Colors.ENDC}"
    return text
