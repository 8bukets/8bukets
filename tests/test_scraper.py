import os
import csv
import json
import pytest
from unittest.mock import MagicMock, AsyncMock, patch
from scraper import MarkPositionScraperAsync

@pytest.mark.asyncio
async def test_csv_injection_prevention(tmp_path):
    """
    Test that CSV injection vectors are sanitized by prepending a single quote.
    """
    # Setup paths
    output_json = tmp_path / "test.json"
    output_csv = tmp_path / "test.csv"
    output_txt = tmp_path / "test.txt"

    # Initialize scraper
    scraper = MarkPositionScraperAsync(
        output_json=str(output_json),
        output_csv=str(output_csv),
        output_txt=str(output_txt),
        max_pages=1,
        concurrency=1
    )

    # Mock data with malicious payloads
    malicious_posts = [{
        'title': '=1+1',
        'date': '2023-01-01',
        'author': '@SUM(1,1)',
        'categories': ['+Test', '-Category'],
        'external_link': 'http://example.com',
        'domain': 'example.com',
        'post_url': 'http://example.com/post'
    }]

    # Run save_data directly
    scraper.save_data(malicious_posts)

    # Verify CSV content
    with open(output_csv, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        row = next(reader)

        # Check title (starts with =)
        assert row[0] == "'=1+1", "Title starting with = should be sanitized"
        # Check author (starts with @)
        assert row[2] == "'@SUM(1,1)", "Author starting with @ should be sanitized"
        # Check categories (one starts with +)
        # categories are joined by ", ". If the first one starts with +, the string starts with +
        assert row[3].startswith("'+Test"), "Categories starting with + should be sanitized"
