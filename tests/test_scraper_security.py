"""
Security tests for the scraper module.
"""
import csv
import pytest
from scraper import OracleNewsScraper

@pytest.fixture(name="scraper_instance")
def fixture_scraper(tmp_path):
    """Fixture to create a scraper instance with temporary paths."""
    output_json = tmp_path / "test_output.json"
    output_csv = tmp_path / "test_output.csv"
    output_txt = tmp_path / "test_output.txt"
    return OracleNewsScraper(str(output_json), str(output_csv), str(output_txt))

def test_csv_injection_prevention(scraper_instance):
    """Test that fields starting with dangerously characters are escaped in CSV."""
    malicious_posts = [
        {
            'title': '=cmd|/C calc!A0',
            'date': 'Oct 15, 2025',
            'author': '@Admin',
            'categories': ['+Math'],
            'external_link': '-http://example.com',
            'domain': 'example.com',
            'post_url': 'http://example.com/post'
        }
    ]

    scraper_instance.save_data(malicious_posts)

    # Verify CSV content
    with open(scraper_instance.output_csv, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader) # Skip header
        row = next(reader)

        # Check title (starts with =)
        assert row[0] == "'=cmd|/C calc!A0"
        # Check author (starts with @)
        assert row[2] == "'@Admin"
        # Check categories (starts with +)
        assert row[3] == "'+Math"
        # Check external_link (starts with -)
        assert row[4] == "'-http://example.com"

def test_csv_normal_data_untouched(scraper_instance):
    """Test that normal fields are not escaped."""
    normal_posts = [
        {
            'title': 'Normal Title',
            'date': 'Oct 15, 2025',
            'author': 'Oracle',
            'categories': ['News'],
            'external_link': 'http://example.com',
            'domain': 'example.com',
            'post_url': 'http://example.com/post'
        }
    ]

    scraper_instance.save_data(normal_posts)

    with open(scraper_instance.output_csv, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader) # Skip header
        row = next(reader)

        assert row[0] == "Normal Title"
        assert row[2] == "Oracle"
