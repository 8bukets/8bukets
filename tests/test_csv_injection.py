"""
Tests for CSV injection prevention in scraper.py.
"""
import csv
from scraper import MarkPositionScraperAsync

class TestCSVInjection:
    """Test suite for CSV injection vulnerabilities."""

    def test_csv_injection_prevention(self, tmp_path):
        """Test that malicious fields are sanitized when writing to CSV."""
        # Setup
        output_json = tmp_path / "test.json"
        output_csv = tmp_path / "test.csv"
        output_txt = tmp_path / "test.txt"

        scraper = MarkPositionScraperAsync(
            output_json=str(output_json),
            output_csv=str(output_csv),
            output_txt=str(output_txt)
        )

        # Malicious data
        malicious_posts = [
            {
                "title": "=cmd|' /C calc'!A0",
                "date": "2023-01-01",
                "author": "@attacker",
                "categories": ["+malicious"],
                "external_link": "-http://evil.com",
                "domain": "evil.com",
                "post_url": "http://example.com"
            }
        ]

        # Act
        scraper.save_data(malicious_posts)

        # Assert
        with open(output_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            _ = next(reader)  # header
            row = next(reader)

            # Row structure: Title, Date, Author, Categories, External Link, Domain, Post URL

            # Check Title (was =cmd...)
            assert row[0].startswith("'"), f"Title vulnerable: {row[0]}"
            assert row[0] == "'=cmd|' /C calc'!A0"

            # Check Author (was @attacker)
            assert row[2].startswith("'"), f"Author vulnerable: {row[2]}"

            # Check Categories (was +malicious) - Note: categories are joined by comma
            assert row[3].startswith("'"), f"Categories vulnerable: {row[3]}"

            # Check External Link (was -http...)
            assert row[4].startswith("'"), f"External Link vulnerable: {row[4]}"
