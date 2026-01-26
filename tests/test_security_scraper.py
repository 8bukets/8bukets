import unittest
import os
import sys
from unittest.mock import MagicMock, patch

# Add root directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import scrape_informatic

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        self.attack_file = "../test_hack.json"
        # Clean up before
        if os.path.exists(self.attack_file):
            os.remove(self.attack_file)

    def tearDown(self):
        # Clean up after
        if os.path.exists(self.attack_file):
            os.remove(self.attack_file)
        if os.path.exists("test_valid.json"):
            os.remove("test_valid.json")

    @patch('scrape_informatic.get_session')
    def test_path_traversal_vulnerability(self, mock_get_session):
        """
        Attempts to write to a file outside the current directory.
        Should fail (raise ValueError).
        """
        # Setup mock to return no posts so it finishes quickly
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.content = b"<html></html>"
        mock_session.get.return_value = mock_response
        mock_get_session.return_value = mock_session

        print(f"\nAttempting to write to {self.attack_file}...")

        with self.assertRaises(ValueError):
            scrape_informatic.scrape(self.attack_file, max_pages=1)

    @patch('scrape_informatic.get_session')
    def test_valid_path(self, mock_get_session):
        # Setup mock for valid path
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.content = b"<html></html>"
        mock_session.get.return_value = mock_response
        mock_get_session.return_value = mock_session

        valid_file = "valid_output.json"
        if os.path.exists(valid_file):
            os.remove(valid_file)

        try:
            scrape_informatic.scrape(valid_file, max_pages=1)
            # Should create file (even if empty content due to logic)
            self.assertTrue(os.path.exists(valid_file), "Valid path failed to create file")
        finally:
            if os.path.exists(valid_file):
                os.remove(valid_file)

if __name__ == '__main__':
    unittest.main()
