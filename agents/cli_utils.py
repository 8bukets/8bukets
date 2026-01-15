"""
CLI Utilities for Visual Enhancements
"""

class Palette:
    """Provides ANSI color codes and helper methods for CLI output."""
    RESET = "\033[0m"
    BOLD = "\033[1m"
    GREEN = "\033[32m"
    CYAN = "\033[36m"
    RED = "\033[31m"

    @staticmethod
    def print_summary(agents_count, report_path, status="Success"):
        """Prints a formatted summary box of the execution."""
        width = 60
        color = Palette.GREEN if status == "Success" else Palette.RED
        print(f"\n{color}┌{'─' * (width - 2)}┐{Palette.RESET}")

        title = "Execution Summary"
        padding = width - 4 - len(title)
        print(f"{color}│ {Palette.RESET}{Palette.BOLD}{title}{Palette.RESET}"
              f"{' ' * padding}{color}│{Palette.RESET}")
        print(f"{color}├{'─' * (width - 2)}┤{Palette.RESET}")

        items = [
            ("Status:", status),
            ("Agents Run:", str(agents_count)),
            ("Report:", report_path)
        ]

        for label, value in items:
            avail = width - 4 - len(label) - 1
            if len(value) > avail:
                value = value[:avail-3] + "..."
            pad = width - 4 - len(label) - 1 - len(value)
            print(f"{color}│ {Palette.RESET}{label} {value}{' ' * pad}{color}│{Palette.RESET}")

        print(f"{color}└{'─' * (width - 2)}┘{Palette.RESET}\n")
