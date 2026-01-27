import unittest
import os
from scraper import MarkPositionScraperAsync

class TestScraperSecurity(unittest.TestCase):
    def test_path_traversal_json(self):
        """Test that initializing scraper with a path traversal in json output raises ValueError."""
        with self.assertRaises(ValueError) as cm:
            MarkPositionScraperAsync(output_json="../test.json", output_csv="test.csv", output_txt="test.txt")
        self.assertIn("Security Error", str(cm.exception))

    def test_path_traversal_csv(self):
        """Test that initializing scraper with a path traversal in csv output raises ValueError."""
        with self.assertRaises(ValueError) as cm:
            MarkPositionScraperAsync(output_json="test.json", output_csv="/etc/passwd", output_txt="test.txt")
        self.assertIn("Security Error", str(cm.exception))

    def test_valid_paths(self):
        """Test that initializing scraper with valid paths works."""
        try:
            MarkPositionScraperAsync(output_json="test.json", output_csv="test.csv", output_txt="test.txt")
        except ValueError:
            self.fail("MarkPositionScraperAsync raised ValueError unexpectedly!")

    def test_nested_valid_path(self):
        """Test that initializing scraper with valid nested path works."""
        try:
            MarkPositionScraperAsync(output_json="results/test.json", output_csv="results/test.csv", output_txt="results/test.txt")
        except ValueError:
            self.fail("MarkPositionScraperAsync raised ValueError unexpectedly for nested path!")

if __name__ == "__main__":
    unittest.main()
