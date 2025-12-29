
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def colorize(text, color):
        """
        Returns the text wrapped in the color code, but only if stdout is a tty
        or FORCE_COLOR env var is set.
        """
        import sys
        import os
        if not sys.stdout.isatty() and not os.environ.get('FORCE_COLOR'):
            return text
        return f"{color}{text}{Colors.RESET}"

def strip_ansi(text):
    import re
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)

def print_summary_box(title, items):
    """
    Prints a summary box to stdout.
    items: list of (label, value, color)
    """
    if not items:
        return

    # Calculate widths based on visible length (stripping ANSI)
    max_label_len = max(len(strip_ansi(str(item[0]))) for item in items)
    max_val_len = max(len(strip_ansi(str(item[1]))) for item in items)

    # Title width handling
    title_len = len(title)
    box_width = max(title_len + 4, max_label_len + max_val_len + 7) # 7 = "  " + " . " + "  "

    border = Colors.colorize("=" * box_width, Colors.CYAN)
    print(f"\n{border}")
    print(f"{Colors.colorize(title.center(box_width), Colors.BOLD)}")
    print(border)

    for label, value, color in items:
        visible_label = strip_ansi(str(label))
        visible_value = strip_ansi(str(value))

        # Calculate dots needed
        padding_len = box_width - 4 - len(visible_label) - len(visible_value)
        dots = "." * max(1, padding_len)

        colored_dots = Colors.colorize(dots, Colors.BLUE)
        colored_value = Colors.colorize(value, color)

        print(f"  {label} {colored_dots} {colored_value}")

    print(border + "\n")
