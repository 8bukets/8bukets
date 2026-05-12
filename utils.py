import os
import sys

def validate_output_path(path: str) -> str:
    """
    Validates that the output path is within the current working directory.
    Prevents path traversal attacks (e.g., ../../etc/passwd).

    Args:
        path (str): The file path to validate.

    Returns:
        str: The absolute path if valid.

    Raises:
        ValueError: If the path is outside the current working directory.
    """
    if not path:
        return path

    # Get absolute path of the current directory
    base_dir = os.path.abspath(os.getcwd())

    # Get absolute path of the requested file
    requested_path = os.path.abspath(path)

    # Check if the requested path starts with the base directory
    # commonpath returns the longest common sub-path
    try:
        if os.path.commonpath([base_dir, requested_path]) != base_dir:
            raise ValueError(f"Security Error: Output path '{path}' attempts to traverse outside the current directory.")
    except ValueError:
        # On Windows, mixing drives might raise ValueError in commonpath, implying traversal/different root
        raise ValueError(f"Security Error: Output path '{path}' attempts to traverse outside the current directory.")

    return requested_path
