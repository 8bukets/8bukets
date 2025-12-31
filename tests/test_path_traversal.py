import unittest
import os
import shutil
from scraper import MarkPositionScraperAsync

class TestPathTraversal(unittest.TestCase):
    def setUp(self):
        # Create a sandbox directory structure
        self.test_dir = os.path.abspath("test_sandbox")
        self.safe_dir = os.path.join(self.test_dir, "safe")
        self.unsafe_target = os.path.join(self.test_dir, "hacked.txt")

        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
        os.makedirs(self.safe_dir)

        # We must change CWD to safe_dir because validate_output_path checks relative to CWD.
        # But changing CWD in tests is side-effecty.
        # However, MarkPositionScraperAsync's validation uses os.getcwd().
        # So we must either mock os.getcwd or run the test from a known CWD.
        # We will assume CWD is the project root (where the test is run from)
        # and create a subdirectory for outputs.
        self.output_dir = os.path.join(os.getcwd(), "test_outputs")
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
        if os.path.exists(self.output_dir):
            shutil.rmtree(self.output_dir)

    def test_traversal_attempt(self):
        # Attempt to write to a path outside CWD (which is project root)

        # 1. Absolute path outside CWD (e.g. /tmp/hacked.txt)
        unsafe_abs_path = "/tmp/hacked.txt"

        with self.assertRaises(ValueError) as cm:
            MarkPositionScraperAsync(
                output_json=unsafe_abs_path,
                output_csv="safe.csv",
                output_txt="safe.txt"
            )
        self.assertIn("Security Error", str(cm.exception))

        # 2. Relative path traversal (e.g. ../hacked.txt)
        unsafe_rel_path = "../hacked.txt"
        with self.assertRaises(ValueError) as cm:
             MarkPositionScraperAsync(
                output_json=unsafe_rel_path,
                output_csv="safe.csv",
                output_txt="safe.txt"
            )
        self.assertIn("Security Error", str(cm.exception))

        # 3. Valid path inside CWD should pass
        valid_path = os.path.join(self.output_dir, "valid.json")
        # Relative path inside CWD
        valid_rel_path = "test_outputs/valid.json"

        try:
             MarkPositionScraperAsync(
                output_json=valid_rel_path,
                output_csv=os.path.join(self.output_dir, "valid.csv"),
                output_txt=os.path.join(self.output_dir, "valid.txt")
            )
        except ValueError:
            self.fail("Valid path raised ValueError")

    def test_csv_injection_attempt(self):
        # This test checks for sanitation
        unsafe_data = [
            {'title': '=cmd| /C calc!A0', 'author': 'Attacker', 'categories': [], 'date': '2021-01-01'}
        ]

        json_path = os.path.join(self.output_dir, "test_sanitized.json")
        csv_path = os.path.join(self.output_dir, "test_sanitized.csv")
        txt_path = os.path.join(self.output_dir, "test_sanitized.txt")

        scraper = MarkPositionScraperAsync(
            output_json=json_path,
            output_csv=csv_path,
            output_txt=txt_path
        )
        # We invoke save_data manually to check the output
        scraper.save_data(unsafe_data)

        with open(csv_path, "r") as f:
            content = f.read()
            # The content should now be escaped with a single quote
            self.assertIn("'=cmd| /C calc!A0", content)

            # Use csv module to read back and verify exact value
            f.seek(0)
            import csv
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)
            title = row[0]
            self.assertEqual(title, "'=cmd| /C calc!A0")

if __name__ == '__main__':
    unittest.main()
