import unittest
import os
import shutil
import tempfile
from scraper import MarkPositionScraperAsync

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = tempfile.mkdtemp()
        self.original_cwd = os.getcwd()
        os.chdir(self.test_dir)

    def tearDown(self):
        # Cleanup
        os.chdir(self.original_cwd)
        shutil.rmtree(self.test_dir)

    def test_validate_output_path_safe(self):
        """Test that safe paths are accepted."""
        # Simple filename
        scraper = MarkPositionScraperAsync(
            output_json="safe.json",
            output_csv="safe.csv",
            output_txt="safe.txt"
        )
        self.assertEqual(scraper.output_json, os.path.abspath("safe.json"))

        # Subdirectory (created)
        os.makedirs("subdir")
        scraper = MarkPositionScraperAsync(
            output_json="subdir/safe.json",
            output_csv="safe.csv",
            output_txt="safe.txt"
        )
        self.assertEqual(scraper.output_json, os.path.abspath("subdir/safe.json"))

    def test_validate_output_path_traversal(self):
        """Test that path traversal attempts raise ValueError."""
        # Parent directory
        with self.assertRaises(ValueError):
            MarkPositionScraperAsync(
                output_json="../unsafe.json",
                output_csv="safe.csv",
                output_txt="safe.txt"
            )

        # Absolute path outside CWD
        unsafe_abs = os.path.abspath(os.path.join(self.test_dir, "..", "unsafe.json"))
        with self.assertRaises(ValueError):
            MarkPositionScraperAsync(
                output_json=unsafe_abs,
                output_csv="safe.csv",
                output_txt="safe.txt"
            )

    def test_validate_output_path_traversal_complex(self):
        """Test complex traversal attempts."""
        # Subdirectory then out
        with self.assertRaises(ValueError):
            MarkPositionScraperAsync(
                output_json="subdir/../../unsafe.json",
                output_csv="safe.csv",
                output_txt="safe.txt"
            )

if __name__ == '__main__':
    unittest.main()
