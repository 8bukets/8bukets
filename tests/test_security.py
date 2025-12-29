import unittest
import os
from scraper import MarkPositionScraperAsync

class TestScraperSecurity(unittest.TestCase):
    def test_path_traversal_prevention(self):
        # Test parent directory traversal
        with self.assertRaises(ValueError) as cm:
            MarkPositionScraperAsync(
                output_json="../unsafe.json",
                output_csv="safe.csv",
                output_txt="safe.txt"
            )
        self.assertIn("Security Error", str(cm.exception))

        # Test absolute path outside CWD
        unsafe_abs_path = os.path.abspath("/tmp/unsafe.json")
        # Note: This might fail if /tmp is not available or handled differently in windows,
        # but the concept holds. In container, we usually are in /app

        # Only test if it's actually outside CWD
        if os.path.commonpath([os.getcwd(), unsafe_abs_path]) != os.getcwd():
             with self.assertRaises(ValueError) as cm:
                MarkPositionScraperAsync(
                    output_json=unsafe_abs_path,
                    output_csv="safe.csv",
                    output_txt="safe.txt"
                )
             self.assertIn("Security Error", str(cm.exception))

    def test_safe_paths(self):
        # Test safe relative path
        try:
            MarkPositionScraperAsync(
                output_json="safe.json",
                output_csv="safe.csv",
                output_txt="safe.txt"
            )
        except ValueError:
            self.fail("MarkPositionScraperAsync raised ValueError unexpectedly for safe path!")

        # Test safe subdirectory path
        # Ensure dir exists or scraper handles it? Scraper opens file, so dir should exist usually,
        # but validation logic doesn't check existence, only path.
        subdir = "results"
        if not os.path.exists(subdir):
            os.makedirs(subdir)

        try:
            MarkPositionScraperAsync(
                output_json=f"{subdir}/safe.json",
                output_csv=f"{subdir}/safe.csv",
                output_txt=f"{subdir}/safe.txt"
            )
        except ValueError:
            self.fail("MarkPositionScraperAsync raised ValueError unexpectedly for subdirectory path!")

if __name__ == "__main__":
    unittest.main()
