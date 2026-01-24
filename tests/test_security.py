import sys
import unittest
from unittest.mock import MagicMock, patch
import os
import argparse

# Ensure current dir is in sys.path
sys.path.append(os.getcwd())

import scrape_informatic
import google_search_scraper

class TestSecurityFixes(unittest.TestCase):

    @patch('scrape_informatic.get_session')
    @patch('builtins.open', new_callable=MagicMock)
    @patch('json.dump')
    def test_scrape_informatic_path_traversal(self, mock_json_dump, mock_open, mock_get_session):
        # Setup mock
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b"<html></html>"
        mock_session.get.return_value = mock_response
        mock_get_session.return_value = mock_session

        unsafe_path = "../unsafe_file.json"

        # Expect ValueError
        with self.assertRaises(ValueError) as cm:
            scrape_informatic.scrape(unsafe_path, max_pages=1)

        self.assertIn("outside the current working directory", str(cm.exception))

        # Verify open NOT called
        mock_open.assert_not_called()

    @patch('scrape_informatic.get_session')
    @patch('builtins.open', new_callable=MagicMock)
    @patch('json.dump')
    def test_scrape_informatic_valid_path(self, mock_json_dump, mock_open, mock_get_session):
         # Setup mock
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b"<html></html>"
        mock_session.get.return_value = mock_response
        mock_get_session.return_value = mock_session

        valid_path = "valid_output.json"

        # Should NOT raise ValueError
        scrape_informatic.scrape(valid_path, max_pages=1)

        # Verify open CALLED
        mock_open.assert_called_with(valid_path, 'w', encoding='utf-8')

    @patch('google_search_scraper.perform_google_search')
    @patch('builtins.open', new_callable=MagicMock)
    @patch('json.dump')
    @patch('argparse.ArgumentParser.parse_args')
    def test_google_scraper_path_traversal(self, mock_args, mock_json_dump, mock_open, mock_search):
        mock_search.return_value = []
        mock_args.return_value = argparse.Namespace(query="test", output="../unsafe.json", limit=1, verbose=False)

        with self.assertRaises(ValueError) as cm:
             google_search_scraper.main()

        self.assertIn("outside the current working directory", str(cm.exception))
        mock_open.assert_not_called()

if __name__ == '__main__':
    unittest.main()
