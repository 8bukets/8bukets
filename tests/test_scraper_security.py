import os
import pytest
import logging
from scraper import MarkPositionScraperAsync

def test_path_traversal_prevention(caplog):
    # Enable logging capture
    caplog.set_level(logging.ERROR)

    posts = [{'title': 'Test Post'}]

    # Define a path outside current directory
    malicious_path = "/tmp/vulnerable.json"

    # Ensure it doesn't exist
    if os.path.exists(malicious_path):
        os.remove(malicious_path)

    scraper = MarkPositionScraperAsync(
        output_json=malicious_path,
        output_csv="dummy.csv",
        output_txt="dummy.txt"
    )

    scraper.save_data(posts)

    # Verify file was NOT created
    assert not os.path.exists(malicious_path)

    # Verify error was logged
    assert "Path traversal detected" in caplog.text

def test_valid_path_allowed():
    posts = [{'title': 'Test Post'}]
    valid_path = "valid.json"

    if os.path.exists(valid_path):
        os.remove(valid_path)

    scraper = MarkPositionScraperAsync(
        output_json=valid_path,
        output_csv="dummy.csv",
        output_txt="dummy.txt"
    )

    scraper.save_data(posts)

    # Verify file WAS created
    assert os.path.exists(valid_path)

    # Cleanup
    os.remove(valid_path)
    if os.path.exists("dummy.csv"): os.remove("dummy.csv")
    if os.path.exists("dummy.txt"): os.remove("dummy.txt")
