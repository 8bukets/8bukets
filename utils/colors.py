import os
import sys
import re

class Colors:
    """
    ANSI color codes for terminal output and helper methods for styling.
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

    # Emojis
    CHECK = "✅"
    CROSS = "❌"
    ROCKET = "🚀"
    CHART = "📊"
    DOC = "📄"
    TIME = "⏱️"
    GEAR = "⚙️"
    INFO = "ℹ️"
    WARN = "⚠️"
    CALENDAR = "📅"

    @staticmethod
    def strip_ansi(text):
        """Removes ANSI escape codes from text."""
        ansi_escape = re.compile(r'\x1b\[[0-9;]*m')
        return ansi_escape.sub('', text)

    @staticmethod
    def style(text, color=None, bold=False):
        """Apply style to text if stdout is a TTY or FORCE_COLOR is set."""
        if not sys.stdout.isatty() and not os.environ.get('FORCE_COLOR'):
            return text

        styled_text = text
        if color:
            styled_text = f"{color}{styled_text}"
        if bold:
            styled_text = f"{Colors.BOLD}{styled_text}"

        return f"{styled_text}{Colors.ENDC}"

    @staticmethod
    def get_visible_length(text):
        """
        Calculates the visual length of the string, accounting for:
        1. Stripping invisible ANSI codes.
        2. Counting double-width emojis as 2 columns.
        """
        clean_text = Colors.strip_ansi(text)

        # Manually adjust for specific emojis we use that are visually 2 chars wide
        # but often counted as 1 char by len() (depending on python version/build, but standard is 1 codepoint for these)
        # Note: ⏱️ and ℹ️ are often 2 chars (symbol + selector), so len() matches visual width (2).
        # ✅, ❌, 🚀, 📊, 📄, 📅, ⚙️, ⚠️ are often len()=1.

        # Simple heuristic: add +1 for emojis we know are wide but short in len()
        extras = 0
        len_1_wide = ["✅", "❌", "🚀", "📊", "📄", "📅", "⚙️", "⚠️"]

        for e in len_1_wide:
            extras += clean_text.count(e)

        return len(clean_text) + extras

    @staticmethod
    def print_summary(title, items):
        """
        Prints a summary box with auto-alignment.
        """
        width = 60
        border_color = Colors.BLUE

        # Helper to print a horizontal line
        def print_line(left, mid, right):
            print(f"{border_color}{left}{mid * (width - 2)}{right}{Colors.ENDC}")

        # Top border
        print("")
        print_line("╔", "═", "╗")

        # Title
        vis_title_len = Colors.get_visible_length(title)
        padding_total = width - 4 - vis_title_len
        if padding_total < 0: padding_total = 0
        pad_l = padding_total // 2
        pad_r = padding_total - pad_l

        print(f"{border_color}║{Colors.ENDC} {' ' * pad_l}{Colors.style(title, bold=True)}{' ' * pad_r} {border_color}║{Colors.ENDC}")

        # Separator
        print_line("╠", "═", "╣")

        # Items
        for key, value in items.items():
            str_val = str(value)

            clean_key = Colors.strip_ansi(key)
            vis_key_len = Colors.get_visible_length(clean_key)

            # Target: "║ key: [padding] value ║"
            # Space available for (padding + value) = Width - 4 - 1 (colon) - vis_key_len
            avail_space = width - 5 - vis_key_len

            if avail_space < 5:
                avail_space = 5

            clean_val = Colors.strip_ansi(str_val)
            vis_val_len = Colors.get_visible_length(clean_val)

            if vis_val_len > avail_space:
                # Truncate
                target_len = avail_space - 3
                truncated = str_val
                while Colors.get_visible_length(truncated) > target_len:
                    truncated = truncated[:-1]
                str_val = truncated + "..."
                vis_val_len = Colors.get_visible_length(str_val) # Re-calc

            padding = avail_space - vis_val_len
            if padding < 0: padding = 0

            line_content = f"{key}:{Colors.ENDC}{' ' * padding}{str_val}"
            print(f"{border_color}║{Colors.ENDC} {line_content} {border_color}║{Colors.ENDC}")

        # Bottom border
        print_line("╚", "═", "╝")
        print("")
