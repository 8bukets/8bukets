import unittest
import os
import subprocess
import sys

class TestSecurity(unittest.TestCase):
    def test_path_traversal_scrape_informatic(self):
        # Attempt to write to a file in /tmp (outside CWD)
        output_file = "/tmp/security_test_scrape.json"

        # Ensure file doesn't exist
        if os.path.exists(output_file):
            os.remove(output_file)

        cmd = [sys.executable, "scrape_informatic.py", "-o", output_file, "-n", "1"]

        # Run process
        result = subprocess.run(cmd, capture_output=True, text=True)

        # Check that it failed
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Security Error", result.stderr)
        self.assertFalse(os.path.exists(output_file))

    def test_path_traversal_google_search(self):
        # Attempt to write to a file in /tmp (outside CWD)
        output_file = "/tmp/security_test_google.json"

        # Ensure file doesn't exist
        if os.path.exists(output_file):
            os.remove(output_file)

        cmd = [sys.executable, "google_search_scraper.py", "-o", output_file, "-n", "1"]

        # Run process
        result = subprocess.run(cmd, capture_output=True, text=True)

        # Check that it failed
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Security Error", result.stderr)
        self.assertFalse(os.path.exists(output_file))

if __name__ == '__main__':
    unittest.main()
