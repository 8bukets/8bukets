import unittest
import os
import shutil
from scraper import MarkPositionScraperAsync

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        self.dummy_json = "test_links.json"
        self.dummy_csv = "test_links.csv"
        self.dummy_txt = "test_unique_links.txt"

    def tearDown(self):
        for f in [self.dummy_json, self.dummy_csv, self.dummy_txt]:
            if os.path.exists(f):
                os.remove(f)

    def test_path_traversal_prevention(self):
        """Test that initialization fails with paths outside CWD."""
        bad_paths = [
            "../outside.csv",
            "/tmp/absolute.csv",
            "subdir/../../escape.csv"
        ]

        for path in bad_paths:
            with self.assertRaises(ValueError) as cm:
                MarkPositionScraperAsync(
                    output_json=self.dummy_json,
                    output_csv=path,
                    output_txt=self.dummy_txt
                )
            self.assertIn("Security Error", str(cm.exception))

    def test_valid_paths(self):
        """Test that valid paths are accepted."""
        try:
            MarkPositionScraperAsync(
                output_json="subdir/ok.json",
                output_csv="ok.csv",
                output_txt="./also_ok.txt"
            )
        except ValueError:
            self.fail("Valid paths raised ValueError unexpectedly!")

    def test_csv_sanitization(self):
        """Test that CSV formulas are sanitized."""
        scraper = MarkPositionScraperAsync(
            output_json=self.dummy_json,
            output_csv=self.dummy_csv,
            output_txt=self.dummy_txt
        )

        # Test cases: (input, expected_output)
        test_cases = [
            ("=SUM(1,2)", "'=SUM(1,2)"),
            ("+1+2", "'+1+2"),
            ("-1-2", "'-1-2"),
            ("@echo", "'@echo"),
            ("Normal text", "Normal text"),
            ("", ""),
            (None, None)
        ]

        for input_text, expected in test_cases:
            self.assertEqual(scraper.sanitize_for_csv(input_text), expected)

if __name__ == '__main__':
    unittest.main()
