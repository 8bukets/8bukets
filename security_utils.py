def sanitize_for_markdown(text: str) -> str:
    """
    Sanitizes a string to be safely included in a Markdown document.
    Escapes characters that have special meaning in Markdown to prevent
    Markdown Injection / Stored XSS via Markdown.
    """
    if not isinstance(text, str):
        return str(text)

    # List of characters to escape
    special_chars = ['\\', '`', '*', '_', '{', '}', '[', ']', '(', ')', '#', '+', '-', '.', '!', '>', '~', '|']

    # Escape backslash first to avoid double escaping
    text = text.replace('\\', '\\\\')

    for char in special_chars:
        if char == '\\':
            continue
        text = text.replace(char, f'\\{char}')

    return text
