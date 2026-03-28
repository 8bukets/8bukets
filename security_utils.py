import re

def sanitize_for_markdown(text: str) -> str:
    """
    Sanitize text to prevent Markdown injection.
    Escapes characters that could be interpreted as Markdown formatting.
    """
    if not text:
        return ""
    # Escape characters that have special meaning in Markdown
    # We escape: \ ` * _ { } [ ] ( ) # + - . ! |
    # Note: escaping everything might be overkill and make text hard to read,
    # but for security we want to be safe.
    # However, simple text usually doesn't need aggressive escaping.
    # The most critical are [ ] ( ) for links, and < > for HTML.

    # Using a list of characters to escape
    special_chars = r"\\`*_{}[]()#+-.!|>"

    # We use re.sub with a callback or a character class
    return re.sub(f"([{re.escape(special_chars)}])", r"\\\1", text)

def sanitize_for_csv(text: str) -> str:
    """
    Sanitize text to prevent CSV Injection (Formula Injection).
    If the text starts with =, +, -, or @, prepend a single quote.
    """
    if not text:
        return ""
    if isinstance(text, str) and text.startswith(('=', '+', '-', '@')):
        return f"'{text}"
    return text
