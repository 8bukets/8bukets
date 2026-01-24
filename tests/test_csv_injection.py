import os
import csv
import pytest
from scraper import MarkPositionScraperAsync

class TestCSVInjection:
    def setup_method(self):
        self.output_json = "test_links.json"
        self.output_csv = "test_links.csv"
        self.output_txt = "test_unique_links.txt"
        self.scraper = MarkPositionScraperAsync(
            output_json=self.output_json,
            output_csv=self.output_csv,
            output_txt=self.output_txt
        )

    def teardown_method(self):
        if os.path.exists(self.output_json):
            os.remove(self.output_json)
        if os.path.exists(self.output_csv):
            os.remove(self.output_csv)
        if os.path.exists(self.output_txt):
            os.remove(self.output_txt)

    def test_csv_injection_prevention(self):
        # Malicious data
        malicious_posts = [
            {
                'title': '=cmd|\'/C calc\'!A0',
                'date': '+2021-01-01',
                'author': '@attacker',
                'categories': ['-bad_category'],
                'external_link': 'http://example.com',
                'domain': 'example.com',
                'post_url': 'http://wordpress.com/post/1'
            }
        ]

        self.scraper.save_data(malicious_posts)

        # Verify CSV content
        with open(self.output_csv, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader)
            row = next(reader)

            # Check if fields are sanitized
            # Title
            assert row[0].startswith("'"), f"Title not sanitized: {row[0]}"
            assert row[0] == "'=cmd|'/C calc'!A0"

            # Date
            assert row[1].startswith("'"), f"Date not sanitized: {row[1]}"

            # Author
            assert row[2].startswith("'"), f"Author not sanitized: {row[2]}"

            # Categories (joined by comma, check first char)
            assert row[3].startswith("'"), f"Categories not sanitized: {row[3]}"
