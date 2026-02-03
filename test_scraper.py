import unittest
from scraper import MarkPositionScraperAsync

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        self.scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")

    def test_sanitize_for_csv_injection(self):
        """Test that CSV injection characters are escaped."""
        dangerous_inputs = [
            ("=cmd|' /C calc'!A0", "'=cmd|' /C calc'!A0"),
            ("+1+2", "'+1+2"),
            ("-1+2", "'-1+2"),
            ("@SUM(1,2)", "'@SUM(1,2)"),
        ]

        for unsafe, safe in dangerous_inputs:
            self.assertEqual(self.scraper.sanitize_for_csv(unsafe), safe)

    def test_sanitize_for_csv_safe(self):
        """Test that safe strings are unchanged."""
        safe_inputs = [
            ("Normal Title", "Normal Title"),
            ("http://example.com", "http://example.com"),
            ("12345", "12345"),
            ("", ""),
            (None, ""),
        ]

        for inp, expected in safe_inputs:
            self.assertEqual(self.scraper.sanitize_for_csv(inp), expected)

if __name__ == '__main__':
    unittest.main()
