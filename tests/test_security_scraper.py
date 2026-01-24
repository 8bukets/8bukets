import unittest
import os
from scraper import BlogScraper

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        if not os.path.exists("subdir"):
            os.mkdir("subdir")

    def tearDown(self):
        if os.path.exists("valid.db"):
            os.remove("valid.db")
        if os.path.exists("subdir/valid.db"):
            os.remove("subdir/valid.db")
        if os.path.exists("subdir"):
            os.rmdir("subdir")

    def test_path_traversal_validation(self):
        """Test that the scraper rejects paths outside the current working directory."""

        # Valid paths (should not raise)
        try:
            BlogScraper("http://example.com", "valid.json", "valid.db")
            BlogScraper("http://example.com", "subdir/valid.json", "subdir/valid.db")
        except ValueError:
            self.fail("BlogScraper raised ValueError on valid paths")

        # Invalid paths (should raise ValueError)
        invalid_paths = [
            ("../outside.json", "valid.db"),
            ("valid.json", "../outside.db"),
            ("/etc/passwd", "valid.db"),
            ("valid.json", "/etc/passwd"),
            ("../../boot.ini", "valid.db")
        ]

        for json_path, db_path in invalid_paths:
            with self.assertRaises(ValueError, msg=f"Should have raised ValueError for {json_path}, {db_path}"):
                BlogScraper("http://example.com", json_path, db_path)

if __name__ == '__main__':
    unittest.main()
