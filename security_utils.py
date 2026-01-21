import re

def sanitize_for_markdown(text: str) -> str:
    """
    Sanitizes text to prevent Markdown injection and Stored XSS.
    Escapes special Markdown characters to prevent them from being interpreted as formatting or links.

    Args:
        text: The text to sanitize.

    Returns:
        The sanitized text.
    """
    if not text:
        return ""

    # Cast to string just in case
    text = str(text)

    # Escape backslash first so we don't double escape later added backslashes
    text = text.replace('\\', '\\\\')

    # Escape characters that could form links or HTML
    # escaping [ ] ( ) < > should cover most malicious links and HTML
    escaped = text.replace('[', '\\[').replace(']', '\\]')
    escaped = escaped.replace('(', '\\(').replace(')', '\\)')
    escaped = escaped.replace('<', '&lt;').replace('>', '&gt;')

    # Also escape * and _ to prevent bold/italic injection which might be used to obfuscate or break layout
    escaped = escaped.replace('*', '\\*').replace('_', '\\_')
    escaped = escaped.replace('`', '\\`')

    # Escape pipes for table compatibility
    escaped = escaped.replace('|', '\\|')

    return escaped
