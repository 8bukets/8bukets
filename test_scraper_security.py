import unittest
import os
from scraper import OracleNewsScraper
import logging

# Disable logging for tests to keep output clean
logging.disable(logging.CRITICAL)

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        self.vuln_file = "../vuln_test.json"
        self.safe_file = "safe_test.json"
        self.dummy_files = ["dummy.csv", "dummy.txt"]
        # Cleanup
        self._cleanup()

    def tearDown(self):
        self._cleanup()

    def _cleanup(self):
        if os.path.exists(self.safe_file):
            os.remove(self.safe_file)
        if os.path.exists(self.vuln_file):
            os.remove(self.vuln_file)
        for f in self.dummy_files:
            if os.path.exists(f):
                os.remove(f)

    def test_validate_path_direct(self):
        """Test validate_path method directly."""
        scraper = OracleNewsScraper("x","y","z")

        # Should raise ValueError
        with self.assertRaises(ValueError):
            scraper.validate_path("../vuln.json")

        with self.assertRaises(ValueError):
            scraper.validate_path("/tmp/vuln.json")

        # Should pass
        result = scraper.validate_path("safe.json")
        self.assertTrue(result.endswith("safe.json"))
        self.assertTrue(os.path.isabs(result))

    def test_save_data_traversal_prevention(self):
        """
        Test that save_data handles traversal attempts gracefully (logs error, doesn't write).
        """
        scraper = OracleNewsScraper(
            output_json=self.vuln_file,
            output_csv="dummy.csv",
            output_txt="dummy.txt"
        )

        # save_data catches the ValueError, so no exception raised here
        scraper.save_data([])

        # Verify file does NOT exist
        self.assertFalse(os.path.exists(self.vuln_file), "Vulnerable file should not exist")

    def test_safe_path(self):
        scraper = OracleNewsScraper(
            output_json=self.safe_file,
            output_csv="dummy.csv",
            output_txt="dummy.txt"
        )
        scraper.save_data([])
        self.assertTrue(os.path.exists(self.safe_file), "Safe file should be created")

if __name__ == '__main__':
    unittest.main()
