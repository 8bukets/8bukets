import unittest
import os
from scraper import MarkPositionScraperAsync

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        # We don't need to initialize the full object with real files for this test
        # but we need to pass something to init, which calls validate_path immediately.
        # So we can test validation via the constructor.
        pass

    def test_valid_paths(self):
        scraper = MarkPositionScraperAsync("links.json", "links.csv", "unique_links.txt")
        self.assertEqual(scraper.output_json, "links.json")
        self.assertEqual(scraper.output_csv, "links.csv")
        self.assertEqual(scraper.output_txt, "unique_links.txt")

    def test_path_traversal_parent(self):
        with self.assertRaises(ValueError):
            MarkPositionScraperAsync("../links.json", "links.csv", "unique_links.txt")

    def test_path_traversal_absolute(self):
        with self.assertRaises(ValueError):
            MarkPositionScraperAsync("/tmp/links.json", "links.csv", "unique_links.txt")

    def test_path_traversal_subdir(self):
        with self.assertRaises(ValueError):
            MarkPositionScraperAsync("subdir/links.json", "links.csv", "unique_links.txt")

    def test_empty_path(self):
        with self.assertRaises(ValueError):
            MarkPositionScraperAsync("", "links.csv", "unique_links.txt")

    def test_dot_path(self):
        with self.assertRaises(ValueError):
             MarkPositionScraperAsync(".", "links.csv", "unique_links.txt")

if __name__ == '__main__':
    unittest.main()
