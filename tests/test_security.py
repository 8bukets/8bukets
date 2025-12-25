import unittest
import csv
import os
from scraper import MarkPositionScraperAsync

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        self.scraper = MarkPositionScraperAsync(
            output_json="test.json",
            output_csv="test.csv",
            output_txt="test.txt"
        )

    def tearDown(self):
        for f in ["test.json", "test.csv", "test.txt"]:
            if os.path.exists(f):
                os.remove(f)

    def test_sanitize_for_csv(self):
        """Test that the sanitizer correctly escapes dangerous characters."""
        dangerous_inputs = [
            "=1+1",
            "+1+1",
            "-1+1",
            "@1+1",
            "=cmd|' /C calc'!A0",
        ]

        for inp in dangerous_inputs:
            sanitized = self.scraper.sanitize_for_csv(inp)
            self.assertTrue(sanitized.startswith("'"), f"Failed to sanitize: {inp}")
            self.assertEqual(sanitized, f"'{inp}")

        safe_inputs = [
            "Normal text",
            "123",
            "http://example.com?q=1", # contains =, but not at start
        ]

        for inp in safe_inputs:
            sanitized = self.scraper.sanitize_for_csv(inp)
            self.assertEqual(sanitized, inp, f"Should not have modified: {inp}")

    def test_csv_output_sanitization(self):
        """Test that save_data actually uses the sanitizer."""
        # Mock posts with dangerous data
        posts = [
            {
                'title': '=SUM(1+1)',
                'author': '+Malicious',
                'categories': ['-Category'],
                'external_link': '@Link'
            }
        ]

        self.scraper.save_data(posts)

        with open("test.csv", "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)

            # Row structure: Title, Date, Author, Categories, External Link, Domain, Post URL
            # indices: 0: Title, 2: Author, 3: Categories, 4: External Link

            self.assertTrue(row[0].startswith("'"), "Title not sanitized")
            self.assertTrue(row[2].startswith("'"), "Author not sanitized")
            self.assertTrue(row[3].startswith("'"), "Categories not sanitized")
            self.assertTrue(row[4].startswith("'"), "External Link not sanitized")

if __name__ == '__main__':
    unittest.main()
