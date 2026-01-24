import pytest
from unittest.mock import patch, MagicMock
import sys
import os

# Add parent directory to path so we can import scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import MarkPositionScraperAsync

@pytest.mark.asyncio
async def test_path_traversal_prevention():
    # Setup scraper with malicious path for JSON, but valid for others
    scraper = MarkPositionScraperAsync(
        output_json="../malicious.json",
        output_csv="links.csv",
        output_txt="links.txt"
    )

    # Mock open
    with patch("builtins.open", new_callable=MagicMock) as mock_open:
        with patch("json.dump"):
            with patch("csv.writer"):
                # Call save_data
                scraper.save_data([{"title": "test"}])

                # Check arguments passed to open
                calls = [call.args[0] for call in mock_open.call_args_list]

                # Verify malicious path was NOT opened
                assert "../malicious.json" not in calls

                # Verify other valid paths WERE opened
                # Since we didn't mock _validate_path, and we are using real os.getcwd(),
                # "links.csv" is valid and should be opened.
                assert "links.csv" in calls
                assert "links.txt" in calls

@pytest.mark.asyncio
async def test_validate_path_method():
    scraper = MarkPositionScraperAsync("a.json", "b.csv", "c.txt")

    # Valid path
    assert scraper._validate_path("valid.json")

    # Invalid path (parent dir)
    with pytest.raises(ValueError, match="Security Error"):
        scraper._validate_path("../invalid.json")

    # Invalid path (absolute path outside CWD)
    # This assumes /tmp is not the CWD or a parent of CWD
    # In this environment, CWD is usually /app. /tmp is usually separate.
    try:
        scraper._validate_path("/tmp/invalid.json")
    except ValueError:
        pass # Expected
    except Exception as e:
        # If /tmp is valid (e.g. if CWD is /), this might fail.
        # But for specific test, we can try using a made up parent path
        cwd = os.getcwd()
        parent = os.path.dirname(cwd)
        outside_path = os.path.join(parent, "test.json")
        with pytest.raises(ValueError):
            scraper._validate_path(outside_path)
