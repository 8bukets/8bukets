import unittest
import os
from scraper import MarkPositionScraperAsync

class TestScraperSecurity(unittest.TestCase):
    def test_path_traversal_prevention(self):
        """Test that scraper rejects paths with directory components."""
        unsafe_paths = [
            ("../evil.json", "links.csv", "unique.txt"),
            ("links.json", "/tmp/evil.csv", "unique.txt"),
            ("links.json", "links.csv", "./evil.txt")
        ]

        for json_path, csv_path, txt_path in unsafe_paths:
            with self.assertRaises(ValueError, msg=f"Should reject paths: {json_path}, {csv_path}, {txt_path}"):
                MarkPositionScraperAsync(json_path, csv_path, txt_path)

if __name__ == '__main__':
    unittest.main()
