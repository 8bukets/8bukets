import unittest
import os
import subprocess
import sys

class TestSecurity(unittest.TestCase):
    def test_scraper_path_traversal(self):
        target_file = "/tmp/vulnerable_test_scraper.txt"
        if os.path.exists(target_file):
            os.remove(target_file)

        result = subprocess.run(
            [sys.executable, "scraper.py", "--limit", "1", "--txt", target_file],
            capture_output=True,
            text=True
        )

        # Should not create file
        self.assertFalse(os.path.exists(target_file), "File created outside CWD!")
        # Should output error (logger goes to stderr)
        self.assertIn("Security Error", result.stderr)

    def test_analytics_path_traversal(self):
        result = subprocess.run(
            [sys.executable, "analytics.py", "--input", "/etc/passwd"],
            capture_output=True,
            text=True
        )
        # print goes to stdout usually, but let's check both just in case
        output = result.stdout + result.stderr
        self.assertIn("Security Error", output)

if __name__ == '__main__':
    unittest.main()
