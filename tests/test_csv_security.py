
import unittest
import csv
import os
import json
from scraper import MarkPositionScraperAsync

class TestCSVSecurity(unittest.TestCase):
    def test_csv_injection(self):
        output_json = "test_links.json"
        output_csv = "test_links.csv"
        output_txt = "test_unique_links.txt"

        # Cleanup
        for f in [output_json, output_csv, output_txt]:
            if os.path.exists(f):
                os.remove(f)

        scraper = MarkPositionScraperAsync(output_json, output_csv, output_txt)

        # Malicious data
        malicious_posts = [
            {
                'title': '=1+1',
                'date': '2023-01-01',
                'author': '@attacker',
                'categories': ['+category'],
                'external_link': '-http://evil.com',
                'domain': 'evil.com',
                'post_url': 'http://wordpress.com/post'
            }
        ]

        scraper.save_data(malicious_posts)

        # Verify CSV content
        with open(output_csv, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)

            # Check Title
            # If vulnerable, it is "=1+1"
            # If fixed, it should be "'=1+1" (or similar escaping)
            print(f"DEBUG: Title in CSV: {row[0]}")

            # We want to assertion to fail if it is NOT escaped
            # But "escaped" means starting with '

            # If the value starts with =, +, -, @, it is vulnerable if not preceded by '
            unsafe_chars = ('=', '+', '-', '@')

            if row[0].startswith(unsafe_chars):
                 self.fail(f"CSV Injection vulnerability detected in Title: {row[0]}")

            if row[2].startswith(unsafe_chars):
                 self.fail(f"CSV Injection vulnerability detected in Author: {row[2]}")

            # Categories are joined by ", ". If the first one starts with +, it's an issue.
            if row[3].startswith(unsafe_chars):
                 self.fail(f"CSV Injection vulnerability detected in Categories: {row[3]}")

            if row[4].startswith(unsafe_chars):
                 self.fail(f"CSV Injection vulnerability detected in External Link: {row[4]}")

        # Cleanup
        for f in [output_json, output_csv, output_txt]:
            if os.path.exists(f):
                os.remove(f)

if __name__ == '__main__':
    unittest.main()
