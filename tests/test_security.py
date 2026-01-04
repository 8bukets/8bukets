import os
import csv
import pytest
from scraper import OracleNewsScraper

@pytest.fixture
def scraper():
    return OracleNewsScraper("test_links.json", "test_links.csv", "test_unique_links.txt")

def test_csv_injection_prevention(scraper):
    """
    Test that fields starting with =, +, -, @ are escaped with a single quote
    to prevent CSV formula injection.
    """
    malicious_posts = [
        {
            'title': '=cmd|/C calc!A0',
            'date': '+2025-01-01',
            'author': '-Hacker',
            'categories': ['@Hack'],
            'external_link': 'http://example.com',
            'domain': 'example.com',
            'post_url': 'http://example.com'
        }
    ]

    scraper.save_data(malicious_posts)

    with open("test_links.csv", 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader) # Skip header
        row = next(reader)

        # Verify sanitization
        assert row[0] == "'=cmd|/C calc!A0"
        assert row[1] == "'+2025-01-01"
        assert row[2] == "'-Hacker"
        # Categories are joined, so the first character of the string should be checked
        assert row[3] == "'@Hack"

def teardown_module(module):
    """Cleanup generated files."""
    files = ["test_links.json", "test_links.csv", "test_unique_links.txt"]
    for f in files:
        if os.path.exists(f):
            os.remove(f)
