import csv
import os
import unittest
from scraper import MarkPositionScraperAsync

class TestCSVInjectionFix(unittest.TestCase):

    def setUp(self):
        self.output_csv = 'test_verify_fix.csv'
        self.output_json = 'test_verify_fix.json'
        self.output_txt = 'test_verify_fix.txt'

        self.scraper = MarkPositionScraperAsync(
            output_json=self.output_json,
            output_csv=self.output_csv,
            output_txt=self.output_txt
        )

        # Mock data with malicious payloads
        self.mock_posts = [
            {
                'title': '=1+1',
                'date': '2023-10-27',
                'author': '@attacker',
                'categories': ['+ malicious'],
                'external_link': '-http://evil.com',
                'domain': 'evil.com',
                'post_url': 'http://example.com/post'
            }
        ]

    def tearDown(self):
        for f in [self.output_csv, self.output_json, self.output_txt]:
            if os.path.exists(f):
                os.remove(f)

    def test_sanitize_method(self):
        """Test the sanitize_for_csv method directly."""
        self.assertEqual(self.scraper.sanitize_for_csv('=1+1'), "'=1+1")
        self.assertEqual(self.scraper.sanitize_for_csv('+1+1'), "'+1+1")
        self.assertEqual(self.scraper.sanitize_for_csv('-1+1'), "'-1+1")
        self.assertEqual(self.scraper.sanitize_for_csv('@attacker'), "'@attacker")
        self.assertEqual(self.scraper.sanitize_for_csv('Safe Title'), "Safe Title")
        self.assertEqual(self.scraper.sanitize_for_csv(''), "")
        self.assertEqual(self.scraper.sanitize_for_csv(None), "")

    def test_csv_output_sanitization(self):
        """Test that the CSV output is actually sanitized."""
        self.scraper.save_data(self.mock_posts)

        with open(self.output_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader) # Skip header
            row = next(reader)

            # Check Title
            self.assertEqual(row[0], "'=1+1")
            # Check Author
            self.assertEqual(row[2], "'@attacker")
            # Check Categories
            self.assertEqual(row[3], "'+ malicious")
            # Check External Link
            self.assertEqual(row[4], "'-http://evil.com")

if __name__ == '__main__':
    unittest.main()
