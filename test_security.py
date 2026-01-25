import pytest
import os
import sys
from security_utils import validate_output_path
import subprocess

def test_valid_paths():
    """Test that valid paths within CWD are accepted."""
    cwd = os.getcwd()

    # Simple filename
    assert validate_output_path("test.txt") == os.path.join(cwd, "test.txt")

    # Path with subdirectory (assuming it resolves to inside CWD)
    # validate_output_path resolves abspath, so even if subdir doesn't exist, it checks the string path
    # relative to CWD.
    assert validate_output_path("subdir/test.txt") == os.path.join(cwd, "subdir/test.txt")

    # Path with ./
    assert validate_output_path("./test.txt") == os.path.join(cwd, "test.txt")

def test_path_traversal():
    """Test that path traversal attempts raise ValueError."""

    # Parent directory
    with pytest.raises(ValueError, match="Security Error"):
        validate_output_path("../test.txt")

    # Absolute path outside CWD (e.g., /tmp/test.txt)
    # This depends on where the test runs, but /tmp is usually outside /app
    with pytest.raises(ValueError, match="Security Error"):
        validate_output_path("/tmp/test.txt")

    # More complex traversal
    with pytest.raises(ValueError, match="Security Error"):
        validate_output_path("subdir/../../test.txt")

def test_integration_analytics():
    """
    Test analytics.py integration via subprocess to ensure it fails on traversal.
    """
    # Should fail
    result = subprocess.run(
        [sys.executable, "analytics.py", "--output", "../fail.md"],
        capture_output=True,
        text=True
    )
    assert result.returncode != 0
    assert "Security Error" in result.stderr

    # Should pass (we use a temp name to avoid overwriting real report)
    # But analytics.py prints to stdout "Report generated: ..."
    result = subprocess.run(
        [sys.executable, "analytics.py", "--output", "test_report_safe.md"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "Report generated" in result.stdout

    # Clean up
    if os.path.exists("test_report_safe.md"):
        os.remove("test_report_safe.md")
