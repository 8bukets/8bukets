import re

def sanitize_markdown(text):
    """
    Escapes Markdown special characters to prevent injection attacks.
    """
    if not text:
        return ""

    # Escape characters that have special meaning in Markdown
    # This list includes: \ ` * _ { } [ ] ( ) # + - . !
    escape_chars = r"\\`*_{}[]()#+-.!"

    # Use re.sub to escape each character
    return re.sub(f"([{re.escape(escape_chars)}])", r"\\\1", text)
