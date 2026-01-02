import os
import sys

class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'

    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

    GRAY = '\033[90m'

def colorize(text, color_code):
    if os.getenv('NO_COLOR') or not sys.stdout.isatty():
        return text
    return f"{color_code}{text}{Colors.RESET}"
