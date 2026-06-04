import unittest
import sys
import os

# Add root directory to path to allow importing scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import MarkPositionScraperAsync

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        # Instantiate with dummy files
        self.scraper = MarkPositionScraperAsync("dummy.json", "dummy.csv", "dummy.txt")

    def test_sanitize_for_csv_injection(self):
        """Test that dangerous characters are escaped."""
        dangerous_inputs = [
            "=1+1",
            "+1+1",
            "-1+1",
            "@SUM(1,1)",
            "=cmd|' /C calc'!A0"
        ]

        for input_str in dangerous_inputs:
            # We expect sanitize_for_csv to be available
            sanitized = self.scraper.sanitize_for_csv(input_str)
            self.assertTrue(sanitized.startswith("'"), f"Input '{input_str}' should be sanitized with a leading quote")
            self.assertEqual(sanitized, "'" + input_str)

    def test_sanitize_for_csv_safe(self):
        """Test that safe inputs are not modified."""
        safe_inputs = [
            "Normal text",
            "123",
            "http://example.com",
            " param=value", # starts with space
            "user@example.com" # @ not at start
        ]

        for input_str in safe_inputs:
            sanitized = self.scraper.sanitize_for_csv(input_str)
            self.assertEqual(sanitized, input_str, f"Input '{input_str}' should not be modified")

    def test_sanitize_for_csv_non_string(self):
        """Test that non-string inputs are handled gracefully."""
        inputs = [None, 123, 45.6]
        for val in inputs:
            sanitized = self.scraper.sanitize_for_csv(val)
            self.assertEqual(sanitized, val, f"Input '{val}' should be returned as is")

if __name__ == '__main__':
    unittest.main()
