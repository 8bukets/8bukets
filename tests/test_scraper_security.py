import os
import shutil
import unittest
import sys

# Add parent directory to path to import scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import OracleNewsScraper

class TestScraperPaths(unittest.TestCase):
    def setUp(self):
        self.cwd = os.getcwd()
        self.subdir = os.path.join(self.cwd, "subdir_test")
        os.makedirs(self.subdir, exist_ok=True)

    def tearDown(self):
        if os.path.exists(self.subdir):
            shutil.rmtree(self.subdir)

    def test_valid_paths(self):
        # Current dir
        OracleNewsScraper('test.json', 'test.csv', 'test.txt')

        # Subdir (file path string only, creation happens later, validation checks path string)
        OracleNewsScraper('subdir_test/test.json', 'test.csv', 'test.txt')

        # Absolute path in cwd
        abs_path = os.path.join(self.cwd, 'test_abs.json')
        OracleNewsScraper(abs_path, 'test.csv', 'test.txt')

    def test_invalid_paths(self):
        # Parent dir
        with self.assertRaises(ValueError):
            OracleNewsScraper('../test.json', 'test.csv', 'test.txt')

        # Root dir
        with self.assertRaises(ValueError):
             OracleNewsScraper('/test.json', 'test.csv', 'test.txt')

if __name__ == '__main__':
    unittest.main()
