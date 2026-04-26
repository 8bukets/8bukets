import os
import re

def validate_output_path(path: str) -> str:
    """
    Validates that the output path is within the current working directory and has a valid extension.
    Returns the absolute path if valid, otherwise raises ValueError.
    """
    if not path:
        raise ValueError("Security Error: Output path cannot be empty.")

    abs_path = os.path.abspath(path)
    cwd = os.getcwd()

    try:
        common = os.path.commonpath([abs_path, cwd])
    except ValueError:
        raise ValueError(f"Security Error: Output path '{path}' is on a different drive/location than current working directory.")

    if common != cwd:
        raise ValueError(f"Security Error: Output path '{path}' is outside the current working directory.")

    # Restrict to allowed extensions to prevent writing arbitrary executable files (.py, .sh, etc)
    allowed_extensions = {'.json', '.csv', '.txt', '.md'}
    _, ext = os.path.splitext(abs_path)
    if ext.lower() not in allowed_extensions:
        raise ValueError(f"Security Error: File extension '{ext}' is not allowed.")

    return abs_path

import urllib.parse

def is_safe_url(url: str) -> bool:
    """Validates that a URL uses safe schemes to prevent SSRF"""
    try:
        parsed = urllib.parse.urlparse(url)
        return parsed.scheme in ('http', 'https')
    except Exception:
        return False
