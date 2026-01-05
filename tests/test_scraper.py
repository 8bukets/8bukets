import csv
import unittest
import os
import sys

# Add parent directory to path to import scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import MarkPositionScraperAsync

class TestCSVInjectionFix(unittest.TestCase):
    def test_sanitize_csv(self):
        scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")

        # Test dangerous characters
        self.assertEqual(scraper.sanitize_for_csv("=1+1"), "'=1+1")
        self.assertEqual(scraper.sanitize_for_csv("+1+1"), "'+1+1")
        self.assertEqual(scraper.sanitize_for_csv("-1+1"), "'-1+1")
        self.assertEqual(scraper.sanitize_for_csv("@SUM(1+1)"), "'@SUM(1+1)")

        # Test safe characters
        self.assertEqual(scraper.sanitize_for_csv("Safe Title"), "Safe Title")
        self.assertEqual(scraper.sanitize_for_csv("123"), "123")
        self.assertEqual(scraper.sanitize_for_csv(""), "")
        self.assertEqual(scraper.sanitize_for_csv(None), None)

    def test_save_batch_sanitization(self):
        output_csv = "test_output.csv"
        scraper = MarkPositionScraperAsync("test.json", output_csv, "test.txt")

        malicious_posts = [{
            'title': '=1+1',
            'date': '+2023',
            'author': '-Hacker',
            'categories': ['@Category'],
            'external_link': '=http://evil.com',
            'domain': '+evil.com',
            'post_url': '@http://wordpress.com/post'
        }]

        # Create dummy file objects
        with open("test.json", 'w') as json_f, \
             open(output_csv, 'w', newline='') as csv_f, \
             open("test.txt", 'w') as txt_f:

            csv_writer = csv.writer(csv_f)
            seen_links = set()

            scraper.save_batch(malicious_posts, json_f, csv_writer, txt_f, seen_links, True)

        # Verify CSV content
        with open(output_csv, 'r') as f:
            reader = csv.reader(f)
            row = next(reader)

            # Expected: All fields should start with '
            expected = ["'=1+1", "'+2023", "'-Hacker", "'@Category", "'=http://evil.com", "'+evil.com", "'@http://wordpress.com/post"]
            self.assertEqual(row, expected)

        # Cleanup
        for f in ["test.json", output_csv, "test.txt"]:
            if os.path.exists(f):
                os.remove(f)

if __name__ == "__main__":
    unittest.main()
