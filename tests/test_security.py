import unittest
import os
import sys

# Add project root to path to import scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import MarkPositionScraperAsync

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        # Initialize scraper with dummy paths
        self.scraper = MarkPositionScraperAsync(
            output_json='dummy.json',
            output_csv='dummy.csv',
            output_txt='dummy.txt'
        )

    def test_csv_injection_sanitization(self):
        """Test that potential CSV injection formulas are sanitized."""

        # Test cases: (input, expected_output)
        test_cases = [
            ('=1+1', "'=1+1"),
            ('+1+1', "'+1+1"),
            ('-1+1', "'-1+1"),
            ('@SUM(1,1)', "'@SUM(1,1)"),
            ('Safe Text', 'Safe Text'),
            ('123', '123'),
            ('', ''),
            ('http://example.com', 'http://example.com'),
            # Leading whitespace should not bypass the check if stripped,
            # but clean_text usually runs before this.
            # If sanitize_for_csv handles raw input, it should probably be careful.
            # Assuming sanitize_for_csv receives cleaned text, but let's test if it handles it.
            # The vulnerability often persists if whitespace is around the operator.
            # Excel might execute " =1+1".
            # However, scraper.clean_text strips whitespace.
            # We'll test direct inputs to sanitize_for_csv.
        ]

        # Check if method exists
        if not hasattr(self.scraper, 'sanitize_for_csv'):
            self.fail("MarkPositionScraperAsync has no method 'sanitize_for_csv'")

        for input_text, expected in test_cases:
            with self.subTest(input_text=input_text):
                sanitized = self.scraper.sanitize_for_csv(input_text)
                self.assertEqual(sanitized, expected)

if __name__ == '__main__':
    unittest.main()
