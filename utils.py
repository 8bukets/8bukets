import os

def validate_output_path(file_path):
    """
    Validates that the output path is within the current working directory.
    Raises ValueError if the path attempts to traverse outside.
    """
    if not file_path:
        raise ValueError("Output path cannot be empty.")

    # Get absolute paths
    cwd = os.getcwd()
    abs_path = os.path.abspath(file_path)

    # Check if the path is within the current directory
    # os.path.commonpath returns the longest common sub-path
    # We expect the common path to be the cwd
    if os.path.commonpath([cwd, abs_path]) != cwd:
        raise ValueError(f"Security Error: Output path '{file_path}' traverses outside the current directory.")

    return abs_path
