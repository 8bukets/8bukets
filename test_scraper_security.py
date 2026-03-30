import unittest
import os
from scraper import OracleNewsScraper

class TestScraperSecurity(unittest.TestCase):
    def test_path_traversal_prevention(self):
        """Verify that path traversal attempts raise a ValueError."""
        traversal_path = "../evil.txt"

        with self.assertRaises(ValueError) as context:
            OracleNewsScraper(
                output_json=traversal_path,
                output_csv="links.csv",
                output_txt="unique_links.txt"
            )

        self.assertIn("Security violation", str(context.exception))

    def test_valid_path_acceptance(self):
        """Verify that valid paths are accepted."""
        try:
            OracleNewsScraper("valid.json", "valid.csv", "valid.txt")
        except ValueError:
            self.fail("Valid path raised ValueError unexpectedly!")

if __name__ == '__main__':
    unittest.main()
