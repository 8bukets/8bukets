"""
Security tests for MarkPosition Scraper.
"""
import csv
import sys
import os

# Ensure we can import the scraper module from parent directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import MarkPositionScraperAsync # pylint: disable=import-error

class TestSecurity:
    """Security verification tests."""
    def test_csv_injection_prevention(self, tmp_path):
        """
        Test that potential formula injection characters are escaped in CSV output.
        """
        output_json = tmp_path / "test.json"
        output_csv = tmp_path / "test.csv"
        output_txt = tmp_path / "test.txt"

        scraper = MarkPositionScraperAsync(str(output_json), str(output_csv), str(output_txt))

        # Test payloads starting with =, +, -, @
        malicious_data = [{
            'title': '=cmd|/C calc!A0',
            'author': '+MaliciousAuthor',
            'categories': ['@Category'],
            'external_link': '-http://evil.com',
            'domain': 'evil.com',
            'date': '2023-01-01',
            'post_url': 'http://example.com'
        }]

        scraper.save_data(malicious_data)

        # Read the generated CSV
        with open(output_csv, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            row = next(reader)

            # Assertions
            # The values should be prefixed with a single quote '
            assert row['Title'].startswith("'="), f"Title not escaped: {row['Title']}"
            assert row['Author'].startswith("'+"), f"Author not escaped: {row['Author']}"
            assert row['Categories'].startswith("'@"), f"Categories not escaped: {row['Categories']}"
            assert row['External Link'].startswith("'-"), f"External Link not escaped: {row['External Link']}"

            # Normal fields should stay same
            assert row['Domain'] == 'evil.com'
