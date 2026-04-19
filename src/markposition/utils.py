import os

def validate_output_path(path: str) -> str:
    """
    Validates that the output path is within the current working directory.
    Returns the absolute path if valid, otherwise raises ValueError.
    """
    # Get absolute path of the requested file
    abs_path = os.path.abspath(path)

    # Get absolute path of current working directory
    cwd = os.getcwd()

    # Check if the file path is within the CWD
    # commonpath returns the longest common sub-path
    # We put both paths in a list. If the common path is the CWD (or CWD is a prefix), it's okay.
    # Note: commonpath works on paths, not strings, so it handles separators correctly.

    try:
        common = os.path.commonpath([abs_path, cwd])
    except ValueError:
        # Can happen on Windows if drives are different
        raise ValueError(f"Security Error: Output path '{path}' is on a different drive/location than current working directory.")

    if common != cwd:
        # There's a subtle edge case: if cwd is /a/b and abs_path is /a/b/c, common is /a/b. Correct.
        # If abs_path is /a/b, common is /a/b. Correct.
        # If abs_path is /a/x, common is /a. Incorrect.
        raise ValueError(f"Security Error: Output path '{path}' is outside the current working directory.")

    return abs_path
