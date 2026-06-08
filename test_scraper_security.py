import unittest
from scraper import MarkPositionScraperAsync

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        # Initialize scraper with dummy paths
        self.scraper = MarkPositionScraperAsync("dummy.json", "dummy.csv", "dummy.txt")

    def test_sanitize_csv_field_formulas(self):
        """Test that fields starting with formula characters are sanitized."""
        vulnerable_inputs = [
            "=1+1",
            "+1+1",
            "-1+1",
            "@SUM(1,1)",
            "=cmd|' /C calc'!A0"
        ]
        for input_text in vulnerable_inputs:
            sanitized = self.scraper.sanitize_csv_field(input_text)
            self.assertTrue(sanitized.startswith("'"), f"Input '{input_text}' was not sanitized")
            self.assertEqual(sanitized, "'" + input_text)

    def test_sanitize_csv_field_safe(self):
        """Test that safe fields are not modified."""
        safe_inputs = [
            "Normal Text",
            "12345",
            "http://example.com",
            "Title with = inside",
            " user@example.com" # @ not at start
        ]
        for input_text in safe_inputs:
            sanitized = self.scraper.sanitize_csv_field(input_text)
            self.assertEqual(sanitized, input_text, f"Safe input '{input_text}' was modified")

    def test_sanitize_csv_field_empty(self):
        """Test handling of empty or None inputs."""
        self.assertEqual(self.scraper.sanitize_csv_field(""), "")
        self.assertEqual(self.scraper.sanitize_csv_field(None), "")

if __name__ == '__main__':
    unittest.main()
