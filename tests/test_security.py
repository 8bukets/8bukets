import unittest
import os
import csv
from scraper import MarkPositionScraperAsync

class TestSecurity(unittest.TestCase):
    def setUp(self):
        self.output_json = 'test_security_links.json'
        self.output_csv = 'test_security_links.csv'
        self.output_txt = 'test_security_unique_links.txt'
        self.scraper = MarkPositionScraperAsync(
            self.output_json, self.output_csv, self.output_txt
        )

    def tearDown(self):
        for f in [self.output_json, self.output_csv, self.output_txt]:
            if os.path.exists(f):
                os.remove(f)

    def test_sanitize_for_csv(self):
        """Test that CSV injection characters are neutralized."""
        self.assertEqual(self.scraper.sanitize_for_csv('=cmd'), "'=cmd")
        self.assertEqual(self.scraper.sanitize_for_csv('+123'), "'+123")
        self.assertEqual(self.scraper.sanitize_for_csv('-123'), "'-123")
        self.assertEqual(self.scraper.sanitize_for_csv('@ echo'), "'@ echo")

        # Safe strings should remain unchanged
        self.assertEqual(self.scraper.sanitize_for_csv('Safe Title'), "Safe Title")
        self.assertEqual(self.scraper.sanitize_for_csv('http://example.com'), "http://example.com")
        self.assertEqual(self.scraper.sanitize_for_csv(''), "")

    def test_save_data_sanitization(self):
        """Test that save_data actually uses the sanitization."""
        malicious_posts = [
            {
                'title': '=cmd|/C calc!A0',
                'date': '+2023-01-01',
                'author': '@attacker',
                'categories': ['News'],
                'external_link': 'http://example.com',
                'domain': 'example.com',
                'post_url': 'http://example.com/post'
            }
        ]

        self.scraper.save_data(malicious_posts)

        with open(self.output_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader)
            row = next(reader)

            # Check Title
            self.assertEqual(row[0], "'=cmd|/C calc!A0")
            # Check Date
            self.assertEqual(row[1], "'+2023-01-01")
            # Check Author
            self.assertEqual(row[2], "'@attacker")

if __name__ == '__main__':
    unittest.main()
