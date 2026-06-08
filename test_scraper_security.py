import unittest
import os
import shutil
import tempfile
from scraper import MarkPositionScraperAsync

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for safe testing
        self.test_dir = tempfile.mkdtemp()
        self.original_cwd = os.getcwd()
        os.chdir(self.test_dir)

    def tearDown(self):
        # Restore CWD and clean up
        os.chdir(self.original_cwd)
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_path_traversal_detection(self):
        """Test that paths traversing up are rejected."""
        traversal_paths = [
            '../pwned.json',
            '../../etc/passwd',
            '/etc/passwd', # Absolute path outside CWD
            'subdir/../../traversal.txt'
        ]

        for path in traversal_paths:
            with self.subTest(path=path):
                with self.assertRaises(ValueError) as cm:
                    MarkPositionScraperAsync(
                        output_json=path,
                        output_csv='valid.csv',
                        output_txt='valid.txt'
                    )
                self.assertIn("attempts to traverse outside", str(cm.exception))

    def test_valid_paths(self):
        """Test that valid paths within CWD are accepted."""
        valid_paths = [
            'output.json',
            'subdir/output.json',
            './output.json'
        ]

        # Create subdir for test
        os.makedirs('subdir', exist_ok=True)

        for path in valid_paths:
            with self.subTest(path=path):
                try:
                    MarkPositionScraperAsync(
                        output_json=path,
                        output_csv='valid.csv',
                        output_txt='valid.txt'
                    )
                except ValueError as e:
                    self.fail(f"Valid path '{path}' raised ValueError: {e}")

if __name__ == '__main__':
    unittest.main()
