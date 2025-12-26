import unittest
import csv
import os
from scraper import MarkPositionScraperAsync

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        self.scraper = MarkPositionScraperAsync(
            output_json='test_links.json',
            output_csv='test_links.csv',
            output_txt='test_unique.txt'
        )

    def tearDown(self):
        # Cleanup
        for f in ['test_links.json', 'test_links.csv', 'test_unique.txt']:
            if os.path.exists(f):
                os.remove(f)

    def test_csv_injection_sanitization(self):
        """Test that potential CSV injection payloads are neutralized."""
        malicious_inputs = [
            "=SUM(1+1)",
            "+SUM(1+1)",
            "-SUM(1+1)",
            "@SUM(1+1)",
            "=cmd|' /C calc'!A0"
        ]

        for inp in malicious_inputs:
            sanitized = self.scraper.sanitize_for_csv(inp)
            self.assertTrue(sanitized.startswith("'"), f"Input '{inp}' should be quoted")
            self.assertEqual(sanitized, "'" + inp)

        safe_input = "Safe Title"
        self.assertEqual(self.scraper.sanitize_for_csv(safe_input), safe_input)

    def test_save_data_csv_injection(self):
        """Test that save_data actually applies the sanitization."""
        malicious_post = {
            'title': '=Dangerous Title',
            'date': '2023-01-01',
            'author': '+Author',
            'categories': ['-Category'],
            'external_link': '@Link',
            'domain': 'example.com',
            'post_url': 'http://example.com'
        }

        self.scraper.save_data([malicious_post])

        with open('test_links.csv', 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader) # header
            row = next(reader)

            # Check fields
            self.assertTrue(row[0].startswith("'="), "Title not sanitized")
            self.assertTrue(row[2].startswith("'+"), "Author not sanitized")
            self.assertTrue(row[3].startswith("'-"), "Category not sanitized")
            self.assertTrue(row[4].startswith("'@"), "Link not sanitized")

if __name__ == '__main__':
    unittest.main()
