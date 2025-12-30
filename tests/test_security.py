import unittest
import os
import shutil
from scraper import OracleNewsScraper
import analytics

class TestSecurity(unittest.TestCase):
    def setUp(self):
        self.test_dir = os.path.join(os.getcwd(), 'test_security_env')
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
        os.makedirs(self.test_dir)
        self.old_cwd = os.getcwd()
        os.chdir(self.test_dir)

    def tearDown(self):
        os.chdir(self.old_cwd)
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_scraper_valid_path(self):
        """Test that scraper accepts valid paths inside CWD."""
        scraper = OracleNewsScraper(
            output_json="test.json",
            output_csv="subdir/test.csv", # Subdir needs to exist for open(), but validate_path only checks path string
            output_txt="test.txt"
        )
        self.assertEqual(scraper.output_json, "test.json")

    def test_scraper_invalid_path_traversal(self):
        """Test that scraper rejects path traversal."""
        with self.assertRaises(ValueError) as cm:
            OracleNewsScraper(
                output_json="../evil.json",
                output_csv="test.csv",
                output_txt="test.txt"
            )
        self.assertIn("Security Error", str(cm.exception))

    def test_scraper_invalid_absolute_path(self):
        """Test that scraper rejects absolute paths outside CWD."""
        # /tmp is usually available and outside CWD
        with self.assertRaises(ValueError) as cm:
            OracleNewsScraper(
                output_json="/tmp/evil.json",
                output_csv="test.csv",
                output_txt="test.txt"
            )
        self.assertIn("Security Error", str(cm.exception))

    def test_analytics_valid_path(self):
        """Test that analytics validate_path accepts valid paths."""
        path = "report.md"
        self.assertEqual(analytics.validate_path(path), path)

    def test_analytics_invalid_path(self):
        """Test that analytics validate_path rejects invalid paths."""
        with self.assertRaises(ValueError):
            analytics.validate_path("../report.md")

        with self.assertRaises(ValueError):
            analytics.validate_path("/tmp/report.md")

if __name__ == '__main__':
    unittest.main()
