
import csv
import os
import unittest
from scraper import MarkPositionScraperAsync

class TestCSVInjection(unittest.TestCase):
    def setUp(self):
        self.scraper = MarkPositionScraperAsync(
            output_json='test_links.json',
            output_csv='test_links.csv',
            output_txt='test_unique_links.txt'
        )
        self.malicious_data = [
            {
                'title': '=cmd|/C calc!A0',
                'date': '+2+2',
                'author': '@SUM(1+1)',
                'categories': ['-1'],
                'external_link': 'http://example.com',
                'domain': 'example.com',
                'post_url': 'http://example.com/post'
            }
        ]

    def test_csv_injection_vulnerability(self):
        """
        This test checks if malicious characters are currently written as-is (VULNERABLE)
        or if they are sanitized (FIXED).
        """
        self.scraper.save_data(self.malicious_data)

        with open('test_links.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)

            # Index 0 is Title: =cmd|/C calc!A0
            title = row[0]

            # If the title starts with '=', it's potentially vulnerable if opened in Excel.
            # We want to assert that we are sanitizing it (e.g. by prepending a tab or quote).

            # For the purpose of "reproducing" the issue before the fix,
            # we expect this to fail if we asserted it was safe.
            # So I will assert that it IS safe, and expect it to FAIL.

            # Check if sanitized (e.g., starts with single quote or tab if the original started with =)
            is_sanitized = title.startswith("'") or title.startswith("\t")

            if not is_sanitized and title.startswith("="):
                 print(f"VULNERABILITY CONFIRMED: Title '{title}' starts with '='")
                 self.fail("CSV Injection vulnerability detected: Field starts with '=' and is not sanitized.")

    def tearDown(self):
        for f in ['test_links.json', 'test_links.csv', 'test_unique_links.txt']:
            if os.path.exists(f):
                os.remove(f)

if __name__ == '__main__':
    unittest.main()
