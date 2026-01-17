import unittest
from unittest.mock import MagicMock, patch
import logging
import os
from scraper import BlogScraper

# Disable logging during tests to keep output clean
logging.disable(logging.CRITICAL)

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        self.db_name = "test_security.db"
        self.json_name = "test_security.json"
        self.scraper = BlogScraper("http://example.com", self.json_name, self.db_name)

    def tearDown(self):
        if os.path.exists(self.db_name):
            try:
                os.remove(self.db_name)
            except OSError:
                pass
        if os.path.exists(self.json_name):
            try:
                os.remove(self.json_name)
            except OSError:
                pass

    @patch('requests.get')
    def test_ssrf_prevention(self, mock_get):
        """Test that the scraper blocks unsafe URLs (SSRF protection)."""
        # Setup mock to return success for valid URLs
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b"<html></html>"
        mock_get.return_value = mock_response

        # List of unsafe URLs
        unsafe_urls = [
            "http://localhost",
            "http://localhost:8080",
            "http://127.0.0.1",
            "http://127.0.0.1/admin",
            "ftp://example.com",
            "file:///etc/passwd",
            "gopher://example.com",
            "http://0.0.0.0",
            "http://[::1]"
        ]

        for url in unsafe_urls:
            # We must reset the mock to ensure we are testing the current call
            mock_get.reset_mock()

            content = self.scraper.fetch_page(url)

            # Should return None (blocked)
            self.assertIsNone(content, f"Scraper should not fetch unsafe URL: {url}")

            # Ensure requests.get was NOT called
            mock_get.assert_not_called()

        # Test a valid URL
        mock_get.reset_mock()
        content = self.scraper.fetch_page("http://example.com/valid")
        self.assertIsNotNone(content)
        mock_get.assert_called_once()
        args, _ = mock_get.call_args
        self.assertEqual(args[0], "http://example.com/valid")

if __name__ == '__main__':
    unittest.main()
