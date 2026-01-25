import unittest
import os
import csv
import shutil
from scraper import MarkPositionScraperAsync

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        self.output_json = "test_links.json"
        self.output_csv = "test_links.csv"
        self.output_txt = "test_unique_links.txt"
        self.scraper = MarkPositionScraperAsync(
            output_json=self.output_json,
            output_csv=self.output_csv,
            output_txt=self.output_txt
        )

    def tearDown(self):
        for f in [self.output_json, self.output_csv, self.output_txt]:
            if os.path.exists(f):
                os.remove(f)

    def test_sanitize_for_csv_method_exists_and_works(self):
        """Test that the sanitize_for_csv method exists and works as expected."""
        # This checks if the method exists (it won't initially)
        if not hasattr(self.scraper, 'sanitize_for_csv'):
            self.fail("sanitize_for_csv method not found in MarkPositionScraperAsync")

        # Test cases for CSV Injection
        dangerous_inputs = [
            "=1+1",
            "+1+1",
            "-1+1",
            "@SUM(1,1)",
            "=cmd|' /C calc'!A0"
        ]

        safe_inputs = [
            "Normal Title",
            "1+1", # Not starting with special char (wait, 1+1 is safe? yes, generally, unless interpreted as date/number, but not formula)
            "email@example.com",
            "Just a normal string"
        ]

        for inp in dangerous_inputs:
            sanitized = self.scraper.sanitize_for_csv(inp)
            self.assertTrue(sanitized.startswith("'"), f"Dangerous input '{inp}' was not escaped: {sanitized}")
            self.assertEqual(sanitized[1:], inp)

        for inp in safe_inputs:
            sanitized = self.scraper.sanitize_for_csv(inp)
            self.assertFalse(sanitized.startswith("'"), f"Safe input '{inp}' was unnecessarily escaped: {sanitized}")
            self.assertEqual(sanitized, inp)

    def test_save_data_sanitization(self):
        """Test that save_data actually applies the sanitization."""
        # Mock data with dangerous payloads
        posts = [
            {
                'title': '=cmd|/C calc!A0',
                'date': '+2023-01-01',
                'author': '-Author',
                'categories': ['@Category'],
                'external_link': '=http://evil.com',
                'domain': '+evil.com',
                'post_url': '-http://markposition.com/post'
            }
        ]

        # We need to make sure sanitize_for_csv exists before running this,
        # or expect failure.

        self.scraper.save_data(posts)

        with open(self.output_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader) # Skip header
            row = next(reader)

            # Check each field in the row
            # Expected: All fields in the input started with dangerous chars, so all should be escaped
            for field in row:
                self.assertTrue(field.startswith("'"), f"Field '{field}' in CSV was not escaped")

if __name__ == '__main__':
    unittest.main()
