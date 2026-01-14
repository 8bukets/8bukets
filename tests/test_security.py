import unittest
from unittest.mock import patch, MagicMock
from scraper import BlogScraper
import os

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        self.db_name = "test_security.db"
        self.json_name = "test_security.json"
        self.scraper = BlogScraper("https://wishlist.design.blog", self.json_name, self.db_name)

    def tearDown(self):
        if os.path.exists(self.db_name):
            os.remove(self.db_name)
        if os.path.exists(self.json_name):
            os.remove(self.json_name)

    @patch('requests.get')
    def test_ssrf_prevention_domain(self, mock_get):
        """Test that the scraper does not fetch URLs from different domains."""
        # Setup a malicious URL
        malicious_url = "http://evil.com/malicious"

        # Call fetch_page
        self.scraper.fetch_page(malicious_url)

        # assert that requests.get was NOT called
        mock_get.assert_not_called()

    @patch('requests.get')
    def test_ssrf_prevention_scheme(self, mock_get):
        """Test that the scraper does not fetch URLs with non-http/s schemes."""
        # Setup a URL with invalid scheme
        # Note: requests.get might raise an error for file:// but we want to ensure we don't even try
        file_url = "file:///etc/passwd"

        # Call fetch_page
        self.scraper.fetch_page(file_url)

        # assert that requests.get was NOT called
        mock_get.assert_not_called()
