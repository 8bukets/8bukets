def sanitize_for_markdown(text: str) -> str:
    """
    Sanitizes a string for safe inclusion in Markdown documents.
    Escapes special Markdown characters and HTML tags to prevent Injection and XSS.

    Args:
        text (str): The input text to sanitize.

    Returns:
        str: The sanitized text with special characters escaped.
    """
    if not text:
        return ""

    # Characters that have special meaning in Markdown and should be escaped
    # escaping backslash first to avoid double escaping
    text = text.replace('\\', '\\\\')

    # List of characters to escape:
    # * _ ` { } [ ] ( ) # + - . ! < > |
    chars_to_escape = ['*', '_', '`', '{', '}', '[', ']', '(', ')', '#', '+', '-', '.', '!', '<', '>', '|']

    for char in chars_to_escape:
        text = text.replace(char, f'\\{char}')

    return text
