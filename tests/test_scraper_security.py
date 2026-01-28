import unittest
import csv
import os
import sys

# Ensure we can import scraper from root
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import MarkPositionScraperAsync

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        self.json_file = "test_links.json"
        self.csv_file = "test_links.csv"
        self.txt_file = "test_unique_links.txt"
        self.scraper = MarkPositionScraperAsync(
            self.json_file, self.csv_file, self.txt_file
        )

    def tearDown(self):
        if os.path.exists(self.json_file):
            os.remove(self.json_file)
        if os.path.exists(self.csv_file):
            os.remove(self.csv_file)
        if os.path.exists(self.txt_file):
            os.remove(self.txt_file)

    def test_csv_injection_sanitization(self):
        malicious_posts = [
            {
                "title": "=cmd|' /C calc'!A0",
                "date": "+2023-01-01",
                "author": "-Hacker",
                "categories": ["@BadCategory", "NormalCategory"],
                "external_link": "http://example.com",
                "domain": "example.com",
                "post_url": "http://wordpress.com/post/1"
            }
        ]

        # Save data (this should sanitize)
        self.scraper.save_data(malicious_posts)

        # Verify CSV content
        with open(self.csv_file, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader) # Skip headers
            row = next(reader)

            # Check Title
            self.assertTrue(row[0].startswith("'="), f"Title not sanitized: {row[0]}")
            self.assertEqual(row[0], "'=cmd|' /C calc'!A0")

            # Check Date
            self.assertTrue(row[1].startswith("'+"), f"Date not sanitized: {row[1]}")

            # Check Author
            self.assertTrue(row[2].startswith("'-"), f"Author not sanitized: {row[2]}")

            # Check Categories - Joined string should be sanitized if it starts with special char
            # In this case "@BadCategory, NormalCategory"
            self.assertTrue(row[3].startswith("'@"), f"Categories not sanitized: {row[3]}")

            # Check others (safe)
            self.assertFalse(row[4].startswith("'"), "External Link incorrectly sanitized")
            self.assertFalse(row[5].startswith("'"), "Domain incorrectly sanitized")
            self.assertFalse(row[6].startswith("'"), "Post URL incorrectly sanitized")

if __name__ == '__main__':
    unittest.main()
