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

    @staticmethod
    def style(text, color):
        if not sys.stdout.isatty() and not os.environ.get('FORCE_COLOR'):
            return text
        return f"{color}{text}{Colors.ENDC}"

def print_step(step_num, title, emoji_icon=""):
    """Prints a styled step header."""
    prefix = f"Step {step_num}:"
    colored_prefix = Colors.style(prefix, Colors.CYAN)
    colored_title = Colors.style(title, Colors.BOLD)
    print(f"\n{emoji_icon} {colored_prefix} {colored_title}")

def print_success(message):
    """Prints a success message."""
    print(f"{Colors.style('✔', Colors.GREEN)} {message}")

def print_error(message):
    """Prints an error message."""
    print(f"{Colors.style('✖', Colors.FAIL)} {message}")

def print_summary_box(stats):
    """
    Prints a summary box of the execution.
    stats: dict of label -> value
    """
    if not stats:
        return

    width = 50
    print("\n" + "═" * width)
    print(f"{Colors.style(' 🚀 EXECUTION SUMMARY', Colors.HEADER)}")
    print("─" * width)

    for label, value in stats.items():
        # Truncate label if too long to ensure alignment
        # 4 chars for border/spacing, value length
        val_str = str(value)
        # Adjusting padding calculation
        # Note: Emoji width can be tricky, assuming standard width for now
        # Ideally we would calculate visible length

        padding = width - len(label) - len(val_str) - 4
        if padding < 1:
            padding = 1

        dots = "." * padding
        colored_label = Colors.style(label, Colors.BLUE)
        print(f" {colored_label} {Colors.style(dots, Colors.ENDC)} {Colors.style(val_str, Colors.GREEN)}")

    print("═" * width + "\n")
