import unittest
from scraper import MarkPositionScraperAsync

class TestSecurity(unittest.TestCase):
    def setUp(self):
        # Instantiate scraper with dummy paths
        self.scraper = MarkPositionScraperAsync(
            output_json='dummy.json',
            output_csv='dummy.csv',
            output_txt='dummy.txt'
        )

    def test_csv_injection_sanitization(self):
        """Test that strings starting with formula characters are sanitized."""

        # Test cases: (input, expected_output)
        test_cases = [
            ('=SUM(1+1)', "'=SUM(1+1)"),
            ('+cmd|/C calc', "'+cmd|/C calc"),
            ('-1+1', "'-1+1"),
            ('@echo', "'@echo"),
            ('  =cmd', "'=cmd"), # Leading whitespace stripped
            ('  Normal text  ', 'Normal text'), # Whitespace stripped
            ('Normal text', 'Normal text'),
            ('http://example.com', 'http://example.com'),
            ('', ''),  # Empty string
            (None, "") # None should return empty string per updated logic
        ]

        for input_str, expected in test_cases:
            if input_str is None:
                # The method implementation: if text and text.startswith(...)
                # If text is None, it returns None?
                # Let's check implementation:
                # if text and text.startswith...
                # if text is None, `if text` is False.
                # returns text (which is None).
                pass

            result = self.scraper.sanitize_for_csv(input_str)
            self.assertEqual(result, expected, f"Failed for input: {input_str}")

if __name__ == '__main__':
    unittest.main()
