import unittest
import os
import sys

# Add parent directory to path so we can import scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import MarkPositionScraperAsync

class TestPathTraversal(unittest.TestCase):
    def test_path_traversal_detection(self):
        """Test that initializing scraper with a path outside CWD raises ValueError."""

        # Test case 1: Parent directory traversal
        traversal_path = "../vulnerable.json"

        # We expect a ValueError (Security Error) when passing a traversal path
        # Currently this will fail (it won't raise) until we implement the fix
        with self.assertRaises(ValueError) as cm:
            MarkPositionScraperAsync(
                output_json=traversal_path,
                output_csv="links.csv",
                output_txt="links.txt"
            )

        # Verify the error message contains "Security Error" (once implemented)
        self.assertIn("Security Error", str(cm.exception))

    def test_valid_path(self):
        """Test that initializing scraper with a valid path works."""
        valid_path = "valid.json"
        subdir_path = "tests/valid_subdir.json"

        # Should not raise
        try:
            MarkPositionScraperAsync(
                output_json=valid_path,
                output_csv="links.csv",
                output_txt="links.txt"
            )
            MarkPositionScraperAsync(
                output_json=subdir_path,
                output_csv="links.csv",
                output_txt="links.txt"
            )
        except ValueError:
            self.fail("MarkPositionScraperAsync raised ValueError unexpectedly for valid path")

if __name__ == '__main__':
    unittest.main()
