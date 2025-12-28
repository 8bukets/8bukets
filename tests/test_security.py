import unittest
import os
import shutil
import tempfile
from scraper import MarkPositionScraperAsync

class TestSecurity(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.cwd = os.getcwd()
        os.chdir(self.test_dir)

    def tearDown(self):
        os.chdir(self.cwd)
        shutil.rmtree(self.test_dir)

    def test_path_traversal_prevention(self):
        """Test that path traversal attempts are blocked."""
        # Parent directory
        with self.assertRaises(ValueError) as cm:
            MarkPositionScraperAsync(
                output_json="../unsafe.json",
                output_csv="safe.csv",
                output_txt="safe.txt"
            )
        self.assertIn("Security Error", str(cm.exception))

        # Sibling directory prefix match attempt (if cwd is /tmp/test, try /tmp/test_suffix/file)
        # We simulate this by checking if it allows a path that starts with cwd but is a different dir
        # Hard to test without chdir hacks, but let's try a tricky relative path

        # Since we use abspath, we can trust the OS handling, but we need to ensure our logic
        # doesn't allow "/tmp/test_suffix" when we are in "/tmp/test".

        # Valid paths should work
        try:
            MarkPositionScraperAsync(
                output_json="safe.json",
                output_csv="safe.csv",
                output_txt="safe.txt"
            )
        except ValueError:
            self.fail("MarkPositionScraperAsync raised ValueError unexpectedly for valid path")

        # Subdirectory
        os.mkdir("subdir")
        try:
            MarkPositionScraperAsync(
                output_json="subdir/safe.json",
                output_csv="safe.csv",
                output_txt="safe.txt"
            )
        except ValueError:
             self.fail("MarkPositionScraperAsync raised ValueError unexpectedly for valid subdirectory path")


    def test_csv_injection_sanitization(self):
        """Test that CSV injection characters are escaped."""
        scraper = MarkPositionScraperAsync("a.json", "a.csv", "a.txt")

        test_cases = [
            ("=1+1", "'=1+1"),
            ("+1+1", "'+1+1"),
            ("-1+1", "'-1+1"),
            ("@1+1", "'@1+1"),
            ("Normal text", "Normal text"),
            ("", ""),
            (None, None)
        ]

        for input_text, expected in test_cases:
            with self.subTest(input_text=input_text):
                self.assertEqual(scraper.sanitize_for_csv(input_text), expected)

if __name__ == '__main__':
    unittest.main()
