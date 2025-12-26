import unittest
import csv
import os
from scraper import MarkPositionScraperAsync

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        self.output_json = 'test_links.json'
        self.output_csv = 'test_links.csv'
        self.output_txt = 'test_unique_links.txt'
        self.scraper = MarkPositionScraperAsync(
            output_json=self.output_json,
            output_csv=self.output_csv,
            output_txt=self.output_txt
        )

    def tearDown(self):
        # Cleanup
        for f in [self.output_json, self.output_csv, self.output_txt]:
            if os.path.exists(f):
                os.remove(f)

    def test_sanitize_for_csv(self):
        """Test the sanitize_for_csv method directly."""
        # Dangerous inputs
        self.assertEqual(self.scraper.sanitize_for_csv('=cmd|/C calc!A0'), "'=cmd|/C calc!A0")
        self.assertEqual(self.scraper.sanitize_for_csv('+SUM(1+1)*cmd|/C calc!A0'), "'+SUM(1+1)*cmd|/C calc!A0")
        self.assertEqual(self.scraper.sanitize_for_csv('-10+20'), "'-10+20")
        self.assertEqual(self.scraper.sanitize_for_csv('@SUM(1+1)'), "'@SUM(1+1)")

        # Safe inputs
        self.assertEqual(self.scraper.sanitize_for_csv('Safe Title'), "Safe Title")
        self.assertEqual(self.scraper.sanitize_for_csv(''), "")
        self.assertEqual(self.scraper.sanitize_for_csv('http://example.com'), "http://example.com")

    def test_csv_output_sanitization(self):
        """Test that the CSV output is actually sanitized."""
        malicious_post = {
            'title': '=cmd|/C calc!A0',
            'date': '+2023-01-01',
            'author': '-Hacker',
            'categories': ['@Category'],
            'external_link': '=http://evil.com',
            'domain': '+evil.com',
            'post_url': '-http://example.com/post'
        }

        self.scraper.save_data([malicious_post])

        with open(self.output_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader) # Skip header
            row = next(reader)

            # Check each field
            self.assertTrue(row[0].startswith("'="), "Title not sanitized")
            self.assertTrue(row[1].startswith("'+"), "Date not sanitized")
            self.assertTrue(row[2].startswith("'-"), "Author not sanitized")
            self.assertTrue(row[3].startswith("'@"), "Categories not sanitized")
            self.assertTrue(row[4].startswith("'="), "External Link not sanitized")
            self.assertTrue(row[5].startswith("'+"), "Domain not sanitized")
            self.assertTrue(row[6].startswith("'-"), "Post URL not sanitized")

if __name__ == '__main__':
    unittest.main()
