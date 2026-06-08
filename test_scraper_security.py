import unittest
import os
import shutil
from scraper import MarkPositionScraperAsync

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        self.test_dir = "test_security_output"
        os.makedirs(self.test_dir, exist_ok=True)
        self.cwd = os.getcwd()
        os.chdir(self.test_dir)

    def tearDown(self):
        os.chdir(self.cwd)
        shutil.rmtree(self.test_dir)

    def test_path_traversal_in_save_data(self):
        """Test that path traversal attempts in save_data are blocked."""
        target = "../hacked.json"
        scraper = MarkPositionScraperAsync(output_json=target, output_csv="links.csv", output_txt="links.txt")
        posts = [{"title": "Test"}]

        # save_data catches the exception, so we verify file existence
        scraper.save_data(posts)

        parent_file = os.path.join(self.cwd, "hacked.json")
        self.assertFalse(os.path.exists(parent_file), "File should not be written outside CWD")

    def test_validate_path_method(self):
        """Test the validate_path method directly."""
        scraper = MarkPositionScraperAsync("a", "b", "c")

        # Valid path (relative)
        abs_path = scraper.validate_path("test.json")
        self.assertTrue(os.path.isabs(abs_path))
        self.assertTrue(abs_path.startswith(os.getcwd()))

        # Invalid path (parent directory)
        with self.assertRaises(ValueError):
            scraper.validate_path("../test.json")

        # Invalid path (absolute path to elsewhere)
        # Note: /tmp is usually safe but strictly outside CWD if CWD is /app/test_security_output
        with self.assertRaises(ValueError):
            scraper.validate_path("/tmp/hacked.json")

if __name__ == '__main__':
    unittest.main()
