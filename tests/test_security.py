import unittest
import subprocess
import os
import shutil
import sys
import json

class TestSecurity(unittest.TestCase):
    def setUp(self):
        self.test_dir = os.path.abspath("temp_security_test")
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
        os.makedirs(self.test_dir)

        self.original_cwd = os.getcwd()
        os.chdir(self.test_dir)

        # Path to scripts (relative to test_dir, which is one level down)
        self.scraper_script = os.path.join("..", "scraper.py")
        self.analytics_script = os.path.join("..", "analytics.py")

        # Create a dummy json for analytics
        with open('valid.json', 'w') as f:
            f.write("[]")

    def tearDown(self):
        os.chdir(self.original_cwd)
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_scraper_traversal(self):
        # Attempt to write to parent directory (repo root)
        cmd = [sys.executable, self.scraper_script, "--limit", "1", "--json", "../hacked.json"]
        result = subprocess.run(cmd, capture_output=True, text=True)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Security Error", result.stderr)

    def test_scraper_valid(self):
        # Write to current directory
        # We need to provide all args to prevent defaults writing to current dir (which is fine)
        # but we want to be explicit.
        # Actually defaults are just filenames, so they write to CWD. That is safe.
        cmd = [sys.executable, self.scraper_script, "--limit", "1", "--json", "safe.json"]
        result = subprocess.run(cmd, capture_output=True, text=True)

        self.assertEqual(result.returncode, 0)
        self.assertTrue(os.path.exists("safe.json"))

    def test_analytics_traversal(self):
        # Attempt to read from parent
        cmd = [sys.executable, self.analytics_script, "--input", "../analytics.py"]
        result = subprocess.run(cmd, capture_output=True, text=True)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Security Error", result.stdout)

    def test_analytics_valid(self):
        cmd = [sys.executable, self.analytics_script, "--input", "valid.json", "--output", "report.md"]
        result = subprocess.run(cmd, capture_output=True, text=True)

        self.assertEqual(result.returncode, 0)
        self.assertTrue(os.path.exists("report.md"))

if __name__ == "__main__":
    unittest.main()
