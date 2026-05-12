import unittest
import os
import shutil
from utils import validate_output_path

class TestSecurity(unittest.TestCase):
    def test_validate_output_path_success(self):
        """Test that valid paths are accepted."""
        valid_paths = [
            "data.json",
            "subdir/data.json",
            "./data.json"
        ]
        # Create a subdir for the test
        os.makedirs("subdir", exist_ok=True)
        try:
            for path in valid_paths:
                try:
                    validate_output_path(path)
                except ValueError as e:
                    self.fail(f"validate_output_path raised ValueError unexpectedly for {path}: {e}")
        finally:
            shutil.rmtree("subdir")

    def test_validate_output_path_failure(self):
        """Test that path traversal attempts are rejected."""
        invalid_paths = [
            "../outside.json",
            "/tmp/outside.json",
            "subdir/../../outside.json",
            "/etc/passwd"
        ]

        for path in invalid_paths:
            with self.assertRaises(ValueError, msg=f"Should have rejected {path}"):
                validate_output_path(path)

    def test_empty_path(self):
        """Test that empty path is rejected."""
        with self.assertRaises(ValueError):
            validate_output_path("")

if __name__ == "__main__":
    unittest.main()
