import sys
import os

class Palette:
    """
    A helper class for adding UX polish to the CLI output.
    Follows the philosophy: "Good UX is invisible - it just works."
    """

    # ANSI Color Codes
    RESET = "\033[0m"
    BOLD = "\033[1m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    GREY = "\033[90m"

    @staticmethod
    def _is_tty():
        """Check if output is a terminal."""
        return sys.stdout.isatty()

    @classmethod
    def color(cls, text, color_code):
        """Apply color if in TTY."""
        if cls._is_tty():
            return f"{color_code}{text}{cls.RESET}"
        return text

    @classmethod
    def display_summary(cls, report_data, report_path):
        """
        Displays a beautiful summary box of the operation.
        """
        # Data Extraction with Defaults
        research = report_data.get('research', {})
        posts = research.get('posts_scraped', 0)
        google = research.get('google_results', 0)

        draft = report_data.get('content_draft', {})
        draft_title = draft.get('draft_title', 'Untitled')

        # Truncate title if too long
        title_display = (draft_title[:40] + '...') if len(draft_title) > 40 else draft_title

        # Formatting
        width = 65

        # Helper for printing lines
        def print_line(content, align='left', color=cls.CYAN):
            stripped = content.replace(cls.RESET, '').replace(cls.BOLD, '').replace(cls.GREEN, '').replace(cls.BLUE, '').replace(cls.YELLOW, '').replace(cls.RED, '').replace(cls.CYAN, '').replace(cls.MAGENTA, '').replace(cls.GREY, '')
            padding = width - 4 - len(stripped)
            if align == 'center':
                pad_l = padding // 2
                pad_r = padding - pad_l
                print(f"{cls.color('║', cls.CYAN)} {' ' * pad_l}{content}{' ' * pad_r} {cls.color('║', cls.CYAN)}")
            else:
                print(f"{cls.color('║', cls.CYAN)} {content}{' ' * (padding - 1)} {cls.color('║', cls.CYAN)}")

        print()
        print(cls.color(f"╔{'═' * (width - 2)}╗", cls.CYAN))

        # Header
        print_line(f"{cls.color('🎨 Palette UX Summary', cls.BOLD + cls.MAGENTA)}", align='center')
        print(cls.color(f"╠{'═' * (width - 2)}╣", cls.CYAN))

        # Content
        print_line(f"  📝 Posts Scraped:   {cls.color(str(posts), cls.GREEN)}")
        print_line(f"  🔍 Google Results:  {cls.color(str(google), cls.YELLOW)}")
        print_line(f"  ✨ Draft Created:   {cls.color(title_display, cls.BLUE)}")

        print(cls.color(f"╠{'═' * (width - 2)}╣", cls.CYAN))

        # Footer
        print_line(f"  📄 Report: {cls.color(report_path, cls.BOLD)}")

        print(cls.color(f"╚{'═' * (width - 2)}╝", cls.CYAN))
        print()
