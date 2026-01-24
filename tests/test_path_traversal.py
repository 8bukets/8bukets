import pytest
import os
from scraper import MarkPositionScraperAsync

def test_path_traversal_prevention():
    """Verify that the scraper prevents writing to files outside the current working directory."""

    # Valid paths (inside CWD) should not raise exception
    try:
        scraper = MarkPositionScraperAsync(
            output_json="safe.json",
            output_csv="subdir/safe.csv", # assuming subdir handling is strict or just resolved
            output_txt="safe.txt"
        )
    except ValueError:
        pytest.fail("ValueError raised for safe path")

    # Invalid paths should raise ValueError

    # 1. Absolute path outside CWD
    # We use /tmp which is definitely outside the project root
    with pytest.raises(ValueError, match="Path traversal detected"):
        MarkPositionScraperAsync(
            output_json="/tmp/malicious.json",
            output_csv="safe.csv",
            output_txt="safe.txt"
        )

    # 2. Relative path traversal
    with pytest.raises(ValueError, match="Path traversal detected"):
        MarkPositionScraperAsync(
            output_json="../malicious.json",
            output_csv="safe.csv",
            output_txt="safe.txt"
        )

    # 3. Check CSV and TXT arguments too
    with pytest.raises(ValueError, match="Path traversal detected"):
        MarkPositionScraperAsync(
            output_json="safe.json",
            output_csv="/tmp/malicious.csv",
            output_txt="safe.txt"
        )

    with pytest.raises(ValueError, match="Path traversal detected"):
        MarkPositionScraperAsync(
            output_json="safe.json",
            output_csv="safe.csv",
            output_txt="/tmp/malicious.txt"
        )
