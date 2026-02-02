import unittest
import os
import sys

# Add root to path so we can import scrape_informatic
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scrape_informatic import validate_output_path

class TestScrapeSecurity(unittest.TestCase):
    def test_validate_output_path_safe(self):
        # Should not raise
        cwd = os.getcwd()
        path = "data.json"
        expected = os.path.join(cwd, path)
        self.assertEqual(validate_output_path(path), expected)

        path = "subdir/data.json"
        # Since the function uses abspath, we must ensure subdir handling works
        # If subdir doesn't exist, abspath still resolves it.
        expected = os.path.join(cwd, "subdir", "data.json")
        self.assertEqual(validate_output_path(path), expected)

    def test_validate_output_path_unsafe_traversal(self):
        # Depending on where we run, ../ might be outside or still inside if we are deep.
        # But assuming we run from root, ../ is outside.
        # If we are at /, ../ is still /.
        cwd = os.getcwd()
        if cwd == "/":
             print("Skipping traversal test at root")
             return

        with self.assertRaises(ValueError):
            validate_output_path("../escape.json")

        with self.assertRaises(ValueError):
            validate_output_path("subdir/../../escape.json")

    def test_validate_output_path_unsafe_absolute(self):
        # Only fails if it's outside CWD.
        cwd = os.getcwd()

        # Pick a path definitely outside CWD (unless CWD is /)
        if cwd.startswith("/tmp"):
             target = "/home/escape.json"
        else:
             target = "/tmp/escape.json"

        # Check if target is actually outside
        try:
             common = os.path.commonpath([target, cwd])
             if common == cwd:
                 print(f"Skipping absolute test: {target} is inside {cwd}")
                 return
        except ValueError:
             pass # different drives

        with self.assertRaises(ValueError):
            validate_output_path(target)

if __name__ == '__main__':
    unittest.main()
