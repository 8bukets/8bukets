import unittest
import os
import shutil
import tempfile
from scraper import MarkPositionScraperAsync

class TestPathTraversal(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for the test
        self.test_dir = tempfile.mkdtemp()
        self.original_cwd = os.getcwd()
        os.chdir(self.test_dir)

    def tearDown(self):
        # Restore CWD and remove temp directory
        os.chdir(self.original_cwd)
        shutil.rmtree(self.test_dir)

    def test_path_traversal_prevention(self):
        """Test that the scraper prevents writing files outside the CWD."""

        # Try to specify a path that traverses up
        target_file = "../vulnerable.json"

        with self.assertRaises(ValueError) as cm:
            MarkPositionScraperAsync(
                output_json=target_file,
                output_csv="dummy.csv",
                output_txt="dummy.txt"
            )

        self.assertIn("Security Error", str(cm.exception))
        self.assertIn("attempts to traverse outside the working directory", str(cm.exception))

    def test_valid_path(self):
        """Test that the scraper accepts valid paths within CWD."""
        valid_file = "valid.json"
        try:
            scraper = MarkPositionScraperAsync(
                output_json=valid_file,
                output_csv="valid.csv",
                output_txt="valid.txt"
            )
            self.assertEqual(scraper.output_json, valid_file)
        except ValueError:
            self.fail("MarkPositionScraperAsync raised ValueError for a valid path")

    def test_absolute_path_outside_cwd(self):
        """Test that absolute paths outside CWD are rejected."""
        # /tmp is usually available
        target_file = "/tmp/absolute_vulnerable.json"

        # If /tmp is the cwd (unlikely), skip
        if os.path.commonpath([os.getcwd(), target_file]) == os.getcwd():
            self.skipTest("/tmp is inside CWD, cannot test absolute path rejection")

        with self.assertRaises(ValueError) as cm:
             MarkPositionScraperAsync(
                output_json=target_file,
                output_csv="dummy.csv",
                output_txt="dummy.txt"
            )
        self.assertIn("Security Error", str(cm.exception))

if __name__ == '__main__':
    unittest.main()
