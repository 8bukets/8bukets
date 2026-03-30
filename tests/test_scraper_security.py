import unittest
import csv
import io
import json
import os
from scraper import MarkPositionScraperAsync

class TestScraperSecurity(unittest.TestCase):
    def test_csv_injection_sanitization(self):
        scraper = MarkPositionScraperAsync("dummy.json", "dummy.csv", "dummy.txt")

        # Test sanitization method directly
        self.assertEqual(scraper.sanitize_for_csv("=1+1"), "'=1+1")
        self.assertEqual(scraper.sanitize_for_csv("+1+1"), "'+1+1")
        self.assertEqual(scraper.sanitize_for_csv("-1+1"), "'-1+1")
        self.assertEqual(scraper.sanitize_for_csv("@attacker"), "'@attacker")
        self.assertEqual(scraper.sanitize_for_csv("Normal Title"), "Normal Title")
        self.assertEqual(scraper.sanitize_for_csv(""), "")
        self.assertEqual(scraper.sanitize_for_csv(None), "")

    def test_save_batch_sanitization(self):
        scraper = MarkPositionScraperAsync("dummy.json", "dummy.csv", "dummy.txt")
        malicious_posts = [
            {
                'title': '=1+1',
                'date': '2021-01-01',
                'author': '@attacker',
                'categories': ['+category'],
                'external_link': '-http://evil.com',
                'domain': 'evil.com',
                'post_url': 'http://example.com'
            }
        ]

        # Use StringIO to capture CSV output
        csv_output = io.StringIO()
        csv_writer = csv.writer(csv_output)

        # Mock file objects for json and txt
        with open("dummy.json", "w") as jf, open("dummy.txt", "w") as tf:
             scraper.save_batch(malicious_posts, jf, csv_writer, tf, set(), True)

        csv_content = csv_output.getvalue()

        # Verify
        self.assertIn("'=1+1", csv_content)
        self.assertIn("'@attacker", csv_content)
        self.assertIn("'+category", csv_content)
        self.assertIn("'-http://evil.com", csv_content)
        self.assertIn("evil.com", csv_content) # Should NOT have quote

        # Clean up
        os.remove("dummy.json")
        os.remove("dummy.txt")

if __name__ == '__main__':
    unittest.main()
