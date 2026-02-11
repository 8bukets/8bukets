import csv
import os
import pytest
from scraper import MarkPositionScraperAsync

@pytest.fixture
def scraper_output():
    output_json = "test_security.json"
    output_csv = "test_security.csv"
    output_txt = "test_security.txt"
    yield output_json, output_csv, output_txt
    # Cleanup
    if os.path.exists(output_json): os.remove(output_json)
    if os.path.exists(output_csv): os.remove(output_csv)
    if os.path.exists(output_txt): os.remove(output_txt)

def test_csv_injection_prevention(scraper_output):
    output_json, output_csv, output_txt = scraper_output
    scraper = MarkPositionScraperAsync(output_json, output_csv, output_txt)

    malicious_posts = [
        {
            'title': '=cmd|/C calc!A0',
            'date': '2023-10-27',
            'author': '@attacker',
            'categories': ['Security'],
            'external_link': 'http://example.com',
            'domain': 'example.com',
            'post_url': 'http://example.com/post'
        },
        {
            'title': '+1+1',
            'date': '2023-10-27',
            'author': 'Normal User',
            'categories': ['Tech'],
            'external_link': 'http://example.com',
            'domain': 'example.com',
            'post_url': 'http://example.com/post2'
        }
    ]

    scraper.save_data(malicious_posts)

    with open(output_csv, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        row1 = next(reader)
        row2 = next(reader)

    # Assertions
    assert row1[0].startswith("'"), "Row 1 title should be escaped"
    assert row1[0] == "'=cmd|/C calc!A0"
    assert row2[0].startswith("'"), "Row 2 title should be escaped"
    assert row2[0] == "'+1+1"

    # Check author field which also had malicious input
    assert row1[2].startswith("'"), "Row 1 author should be escaped"
    assert row1[2] == "'@attacker"
