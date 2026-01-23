import unittest
import os
import sys
import shutil

# Add parent directory to path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import OracleNewsScraper
import analytics

class TestPathTraversal(unittest.TestCase):
    def setUp(self):
        self.test_dir = "test_jail"
        if not os.path.exists(self.test_dir):
            os.makedirs(self.test_dir)

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
        # Cleanup potential output files
        for f in ["dummy.json", "dummy.csv", "pwned.txt", "safe.txt"]:
            if os.path.exists(f):
                os.remove(f)

    def test_prevent_path_traversal(self):
        """Ensure that paths outside the current working directory raise ValueError."""
        unsafe_path = "../pwned.txt"

        with self.assertRaises(ValueError) as cm:
            OracleNewsScraper(
                output_json="dummy.json",
                output_csv="dummy.csv",
                output_txt=unsafe_path,
                concurrency=1
            )
        self.assertIn("Path traversal detected", str(cm.exception))
        self.assertIn("outside current directory", str(cm.exception))

    def test_allow_safe_paths(self):
        """Ensure that paths inside the current working directory are allowed."""
        safe_path = "safe.txt"
        # Should not raise
        scraper = OracleNewsScraper(
            output_json="dummy.json",
            output_csv="dummy.csv",
            output_txt=safe_path,
            concurrency=1
        )
        self.assertEqual(scraper.output_txt, safe_path)

    def test_allow_resolved_safe_paths(self):
        """Ensure that paths with '..' that resolve to inside CWD are allowed."""
        # 'agents/../safe.txt' resolves to 'safe.txt' in CWD
        complex_safe_path = "agents/../safe.txt"
        scraper = OracleNewsScraper(
            output_json="dummy.json",
            output_csv="dummy.csv",
            output_txt=complex_safe_path,
            concurrency=1
        )
        self.assertEqual(scraper.output_txt, complex_safe_path)

    def test_analytics_path_traversal(self):
        """Ensure analytics.py prevents path traversal."""
        unsafe_path = "../pwned_report.md"
        # Mock data for generate_report
        data = [{'external_link': 'http://example.com'}]

        with self.assertRaises(ValueError) as cm:
            analytics.generate_report(data, unsafe_path)
        self.assertIn("Path traversal detected", str(cm.exception))

    def test_analytics_load_data_traversal(self):
        unsafe_path = "../links.json"
        with self.assertRaises(ValueError) as cm:
            analytics.load_data(unsafe_path)
        self.assertIn("Path traversal detected", str(cm.exception))

if __name__ == '__main__':
    unittest.main()
