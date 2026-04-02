import os

def validate_output_path(filepath: str) -> str:
    """
    Validates that the output path is within the current working directory.
    Returns the absolute path if valid, raises ValueError otherwise.
    """
    # Get absolute path of the requested file
    abs_path = os.path.abspath(filepath)

    # Get absolute path of current working directory
    cwd = os.path.abspath(os.getcwd())

    # Check if the file is within the CWD
    try:
        common = os.path.commonpath([abs_path, cwd])
    except ValueError:
        raise ValueError(f"Security Error: Path traversal attempt detected. File must be within {cwd}")

    if common != cwd:
        raise ValueError(f"Security Error: Path traversal attempt detected. File must be within {cwd}")

    return abs_path
