import unittest
import os
import shutil
import tempfile
from utils import validate_output_path

class TestSecurity(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = tempfile.mkdtemp()
        self.original_cwd = os.getcwd()
        os.chdir(self.test_dir)

    def tearDown(self):
        # Restore CWD and remove temp dir
        os.chdir(self.original_cwd)
        shutil.rmtree(self.test_dir)

    def test_valid_paths(self):
        """Test that paths inside the current directory are allowed."""
        valid_paths = [
            "data.json",
            "subdir/data.csv",
            "./report.md",
            "a/b/c/output.txt"
        ]

        for path in valid_paths:
            try:
                result = validate_output_path(path)
                # Ensure the result is an absolute path starting with test_dir
                self.assertTrue(result.startswith(self.test_dir))
            except ValueError as e:
                self.fail(f"Valid path '{path}' raised ValueError: {e}")

    def test_path_traversal(self):
        """Test that paths outside the current directory are rejected."""
        # Note: These checks depend on the filesystem structure, but ../ should always go up.
        invalid_paths = [
            "../secret.txt",
            "../../etc/passwd",
            "/tmp/evil.json",
            "/etc/shadow",
            "subdir/../../outside.txt"
        ]

        for path in invalid_paths:
            with self.assertRaises(ValueError, msg=f"Path '{path}' should have failed"):
                validate_output_path(path)

if __name__ == '__main__':
    unittest.main()
