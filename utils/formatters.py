def create_markdown_table(headers, rows):
    """
    Creates a Markdown table from headers and rows.

    Args:
        headers (list): List of column headers.
        rows (list): List of rows, where each row is a list of values.

    Returns:
        str: The formatted Markdown table string.
    """
    if not headers or not rows:
        return ""

    # Calculate column widths
    col_widths = [len(str(h)) for h in headers]
    for row in rows:
        for i, val in enumerate(row):
            if i < len(col_widths):
                col_widths[i] = max(col_widths[i], len(str(val)))

    # Create header row
    header_row = "| " + " | ".join(str(h).ljust(col_widths[i]) for i, h in enumerate(headers)) + " |"

    # Create separator row
    separator_row = "| " + " | ".join("-" * col_widths[i] for i in range(len(headers))) + " |"

    # Create data rows
    data_rows = []
    for row in rows:
        data_rows.append("| " + " | ".join(str(val).ljust(col_widths[i]) for i, val in enumerate(row)) + " |")

    return "\n".join([header_row, separator_row] + data_rows) + "\n"

def create_ascii_progress_bar(value, total, length=20):
    """
    Creates an ASCII progress bar.

    Args:
        value (int/float): Current value.
        total (int/float): Total/max value.
        length (int): Length of the bar in characters.

    Returns:
        str: The ASCII progress bar string.
    """
    if total <= 0:
        percent = 0
    else:
        percent = min(1.0, value / total)

    filled_length = int(length * percent)
    bar = "█" * filled_length + "░" * (length - filled_length)

    return f"[{bar}] {int(percent * 100)}%"
