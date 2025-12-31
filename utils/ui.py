
import sys
import os
import re

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
    def _is_enabled():
        return sys.stdout.isatty() or os.environ.get('FORCE_COLOR')

    @classmethod
    def style(cls, text, color):
        if cls._is_enabled():
            return f"{color}{text}{cls.ENDC}"
        return text

    @staticmethod
    def strip_ansi(text):
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        return ansi_escape.sub('', text)

def print_step(step_num, title):
    prefix = Colors.style(f"Step {step_num}:", Colors.BOLD + Colors.CYAN)
    print(f"\n{prefix} {title}")

def print_summary_box(stats):
    """
    Prints a summary box of the execution stats.
    stats: dict of label -> value
    """
    # Calculate width
    labels = list(stats.keys())
    values = list(stats.values())

    # We need visible length for alignment
    max_label_len = max(len(l) for l in labels) if labels else 0
    max_value_len = max(len(str(Colors.strip_ansi(str(v)))) for v in values) if values else 0

    # Box width: border + padding + label + sep + value + padding + border
    # We want roughly: | Label: Value |
    # Min width 40
    # Current logic was: max_label_len + max_value_len + 7.
    # Where does 7 come from? "| " (2) + ": " (2) + " |" (2) + 1 extra?

    box_width = max(40, max_label_len + max_value_len + 10)

    border = Colors.style("=" * box_width, Colors.BLUE)
    title = Colors.style(" EXECUTION SUMMARY ", Colors.BOLD + Colors.HEADER)

    # Center title
    title_visible_len = len(" EXECUTION SUMMARY ")

    # Ensure non-negative padding
    if box_width > title_visible_len:
        padding_left = (box_width - title_visible_len) // 2
        padding_right = box_width - title_visible_len - padding_left
    else:
        padding_left = 0
        padding_right = 0

    print("\n" + border)
    print(" " * padding_left + title + " " * padding_right)
    print(border)

    for label, value in stats.items():
        # Strip ansi from value to calculate padding
        val_str = str(value)
        val_visible_len = len(Colors.strip_ansi(val_str))

        # Format is: "| LABEL: {PADDING}VALUE |"
        # Length = 2 + len(label) + 2 + len(padding) + len(value) + 2 = 6 + label + value + padding
        # padding = box_width - 6 - len(label) - len(value)

        needed_padding = box_width - 6 - len(label) - val_visible_len
        if needed_padding < 0: needed_padding = 0

        print(f"| {Colors.style(label, Colors.BOLD)}: {' ' * needed_padding}{val_str} |")

    print(border + "\n")
