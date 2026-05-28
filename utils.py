import os

def validate_output_path(filepath: str, base_dir: str = None) -> str:
    """
    Validates that the output path is within the base directory.

    Args:
        filepath: The path to validate.
        base_dir: The base directory to restrict access to. Defaults to current working directory.

    Returns:
        The absolute path if valid.

    Raises:
        ValueError: If the path is outside the base directory or invalid.
    """
    if not filepath:
        raise ValueError("Security Error: Output path cannot be empty.")

    if base_dir is None:
        base_dir = os.getcwd()

    abs_base = os.path.abspath(base_dir)

    # If I run `scraper.py --json foo.json`, filepath is "foo.json".
    # os.path.abspath("foo.json") resolves to CWD/foo.json.

    abs_path = os.path.abspath(filepath)

    # commonpath ensures that abs_path is a subdirectory of abs_base
    if os.path.commonpath([abs_base, abs_path]) != abs_base:
        raise ValueError(f"Security Error: Path '{filepath}' traverses outside the allowed directory.")

    return abs_path
