import unittest
from scraper import MarkPositionScraperAsync

class TestScraper(unittest.TestCase):

    def setUp(self):
        self.scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")

    def test_sanitize_for_csv_vulnerable(self):
        """Test that vulnerable strings are sanitized."""
        vulnerable_inputs = [
            "=cmd|' /C calc'!A0",
            "@SUM(1+1)",
            "+1-2",
            "-1+2",
        ]
        for inp in vulnerable_inputs:
            sanitized = self.scraper.sanitize_for_csv(inp)
            self.assertTrue(sanitized.startswith("'"), f"Failed to sanitize: {inp}")
            self.assertEqual(sanitized[1:], inp)

    def test_sanitize_for_csv_safe(self):
        """Test that safe strings are not modified."""
        safe_inputs = [
            "Hello World",
            "http://example.com",
            "12345",
            " Just a normal string",
        ]
        for inp in safe_inputs:
            sanitized = self.scraper.sanitize_for_csv(inp)
            self.assertEqual(sanitized, inp, f"Modified safe string: {inp}")

    def test_sanitize_for_csv_empty(self):
        """Test empty string handling."""
        self.assertEqual(self.scraper.sanitize_for_csv(""), "")
        self.assertEqual(self.scraper.sanitize_for_csv(None), "")

if __name__ == '__main__':
    unittest.main()
