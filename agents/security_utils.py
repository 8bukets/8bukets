def sanitize_for_markdown(text):
    """
    Escapes Markdown special characters in the text to prevent Markdown injection.

    Args:
        text (str): The text to sanitize.

    Returns:
        str: The sanitized text.
    """
    if text is None:
        return ""
    if not isinstance(text, str):
        return str(text)

    # List of characters to escape: \ ` * _ { } [ ] ( ) # + - . ! | < >
    # We use a translation table for efficiency
    escape_chars = {
        '\\': r'\\',
        '`': r'\`',
        '*': r'\*',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '[': r'\[',
        ']': r'\]',
        '(': r'\(',
        ')': r'\)',
        '#': r'\#',
        '+': r'\+',
        '-': r'\-',
        '.': r'\.',
        '!': r'\!',
        '|': r'\|',
        '<': r'\<',
        '>': r'\>',
    }

    return "".join(escape_chars.get(c, c) for c in text)

def sanitize_url(url):
    """
    Sanitizes a URL for use in Markdown links [text](url).
    Mainly ensures that closing parentheses are encoded to avoid breaking the link syntax.
    Also strips potential control characters and encodes spaces.

    Args:
        url (str): The URL to sanitize.

    Returns:
        str: The sanitized URL.
    """
    if url is None:
        return ""
    if not isinstance(url, str):
        return str(url)

    # Remove control characters
    url = "".join(c for c in url if ord(c) >= 32)

    # Encode ) as %29 to prevent breaking Markdown links
    url = url.replace(')', '%29')

    # Encode spaces as %20
    url = url.replace(' ', '%20')

    return url
