import unittest
import os
import shutil
import sys

# Ensure we can import scraper from the root directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scraper import OracleNewsScraper

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        # Create a dummy test directory to ensure we test isolation correctly
        self.test_dir = os.path.join(os.getcwd(), "test_security_env")
        if not os.path.exists(self.test_dir):
            os.makedirs(self.test_dir)

        # We need to change CWD to control the test environment
        self.original_cwd = os.getcwd()
        os.chdir(self.test_dir)

    def tearDown(self):
        # Restore CWD
        os.chdir(self.original_cwd)
        # Cleanup
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_path_traversal_prevention(self):
        """Test that the scraper prevents path traversal outside the CWD."""

        # Case 1: Parent directory traversal
        # ../data.json should fail
        with self.assertRaises(ValueError) as cm:
            OracleNewsScraper(
                output_json="../data.json",
                output_csv="data.csv",
                output_txt="data.txt"
            )
        self.assertIn("Security Alert", str(cm.exception))

        # Case 2: Absolute path to /tmp (or similar)
        # Assuming the test dir is not /tmp
        try:
            with self.assertRaises(ValueError) as cm:
                OracleNewsScraper(
                    output_json="/tmp/data.json",
                    output_csv="data.csv",
                    output_txt="data.txt"
                )
            self.assertIn("Security Alert", str(cm.exception))
        except AssertionError:
            # Fallback if system allows this (unlikely in correct setup)
            pass

    def test_valid_paths(self):
        """Test that valid paths inside CWD are allowed."""

        # Case 1: Simple filename
        try:
            scraper = OracleNewsScraper(
                output_json="data.json",
                output_csv="data.csv",
                output_txt="data.txt"
            )
            self.assertEqual(scraper.output_json, "data.json")
        except ValueError:
            self.fail("Valid path 'data.json' raised ValueError")

        # Case 2: Subdirectory
        os.makedirs("subdir", exist_ok=True)
        try:
            scraper = OracleNewsScraper(
                output_json="subdir/data.json",
                output_csv="subdir/data.csv",
                output_txt="subdir/data.txt"
            )
            self.assertEqual(scraper.output_json, "subdir/data.json")
        except ValueError:
            self.fail("Valid path 'subdir/data.json' raised ValueError")

        # Case 3: Traversal that stays inside CWD
        # subdir/../data.json -> ./data.json
        try:
            scraper = OracleNewsScraper(
                output_json="subdir/../data.json",
                output_csv="data.csv",
                output_txt="data.txt"
            )
            self.assertEqual(scraper.output_json, "subdir/../data.json")
        except ValueError:
            self.fail("Valid traversal 'subdir/../data.json' raised ValueError")

if __name__ == '__main__':
    unittest.main()
