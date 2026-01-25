import subprocess
import sys
import os
import pytest

# Get the root directory (parent of tests/)
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRAPER_PATH = os.path.join(ROOT_DIR, "scraper.py")

def test_path_traversal_blocked():
    """Test that path traversal attempts are blocked."""
    # Try to write to a file in the parent directory of ROOT_DIR (if possible)
    # or just use ../attack.txt relative to CWD (ROOT_DIR)

    # Note: We run subprocess with cwd=ROOT_DIR
    result = subprocess.run(
        [sys.executable, SCRAPER_PATH, "--txt", "../attack.txt", "--limit", "1"],
        cwd=ROOT_DIR,
        capture_output=True,
        text=True
    )
    assert result.returncode != 0
    assert "Security Error" in result.stderr

def test_valid_path_allowed():
    """Test that valid paths are allowed."""
    output_file = "safe_test.txt"
    output_path = os.path.join(ROOT_DIR, output_file)

    if os.path.exists(output_path):
        os.remove(output_path)

    result = subprocess.run(
        [sys.executable, SCRAPER_PATH, "--txt", output_file, "--limit", "1"],
        cwd=ROOT_DIR,
        capture_output=True,
        text=True
    )
    assert result.returncode == 0

    # Clean up
    if os.path.exists(output_path):
        os.remove(output_path)
