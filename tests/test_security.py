import unittest
import os
from scraper import MarkPositionScraperAsync

class TestSecurity(unittest.TestCase):
    def test_path_traversal_prevention(self):
        """Test that scraper rejects paths with directory components."""
        unsafe_paths = [
            "../outside.json",
            "subdir/inside.json",
            "/tmp/absolute.json",
            "../.ssh/id_rsa"
        ]

        for path in unsafe_paths:
            with self.assertRaises(ValueError) as context:
                MarkPositionScraperAsync(
                    output_json=path,
                    output_csv="safe.csv",
                    output_txt="safe.txt"
                )
            self.assertIn("Security Error", str(context.exception))
            self.assertIn("Path traversal detected", str(context.exception))

    def test_valid_filenames(self):
        """Test that scraper accepts valid filenames."""
        # These should not raise
        try:
            MarkPositionScraperAsync(
                output_json="safe_output.json",
                output_csv="safe_output.csv",
                output_txt="safe_output.txt"
            )
        except ValueError:
            self.fail("MarkPositionScraperAsync raised ValueError unexpectedly for valid filenames")

if __name__ == '__main__':
    unittest.main()
