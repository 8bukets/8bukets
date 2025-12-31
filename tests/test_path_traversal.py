import unittest
import os
import shutil
from scraper import OracleNewsScraper

class TestPathTraversal(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for safe testing
        self.test_dir = "test_output"
        os.makedirs(self.test_dir, exist_ok=True)
        self.scraper = OracleNewsScraper("test.json", "test.csv", "test.txt")

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_valid_path(self):
        """Test that a path within the current working directory is accepted."""
        valid_path = os.path.join(os.getcwd(), self.test_dir, "valid.json")
        try:
            result = self.scraper.validate_output_path(valid_path)
            self.assertEqual(result, valid_path)
        except ValueError:
            self.fail("validate_output_path raised ValueError for a valid path")

    def test_valid_relative_path(self):
        """Test that a relative path within CWD is accepted."""
        relative_path = os.path.join(self.test_dir, "relative.json")
        try:
            result = self.scraper.validate_output_path(relative_path)
            self.assertTrue(result.startswith(os.getcwd()))
        except ValueError:
            self.fail("validate_output_path raised ValueError for a valid relative path")

    def test_path_traversal_parent(self):
        """Test that a path attempting to go to parent directory is rejected."""
        # This assumes the test is run from a subdirectory or that accessing the parent of root is restricted/checked
        # A simpler check is to try to write to /tmp or similar if on linux

        # Construct a path that is definitely outside the current working directory
        # e.g. /tmp/hacked.json
        unsafe_path = "/tmp/hacked.json"

        with self.assertRaises(ValueError) as cm:
            self.scraper.validate_output_path(unsafe_path)
        self.assertIn("outside the current working directory", str(cm.exception))

    def test_path_traversal_dots(self):
        """Test that using .. to escape CWD is rejected."""
        unsafe_path = "../hacked.json"

        # We need to make sure we are not at the filesystem root for this test to be meaningful
        # If we are at /, ../ is still /, so it might be technically "inside" if CWD is /
        # But generally in this env, we are in /app or similar.

        cwd = os.getcwd()
        if cwd != "/":
             with self.assertRaises(ValueError) as cm:
                self.scraper.validate_output_path(unsafe_path)
             self.assertIn("outside the current working directory", str(cm.exception))

if __name__ == '__main__':
    unittest.main()
