import unittest
from unittest.mock import MagicMock, patch
from scraper import BlogScraper

class TestDoSProtection(unittest.TestCase):
    def setUp(self):
        self.scraper = BlogScraper("http://mock.url")

    @patch('requests.get')
    def test_large_response_handling(self, mock_get):
        """Test that the scraper handles excessively large responses gracefully."""
        # Create a mock response object
        mock_response = MagicMock()
        mock_response.status_code = 200

        # This is CRITICAL: We need to mock __enter__ because the code uses 'with requests.get(...) as response:'
        mock_response.__enter__.return_value = mock_response
        mock_response.__exit__.return_value = None

        # Mock 15MB of data in 1MB chunks
        chunk_size = 1024 * 1024
        chunks = [b"x" * chunk_size for _ in range(15)]

        # iter_content returns an iterator over the chunks
        mock_response.iter_content.return_value = iter(chunks)

        # requests.get returns the mock response
        mock_get.return_value = mock_response

        # Call fetch_page
        content = self.scraper.fetch_page("http://mock.url")

        # It should return None because it exceeded the limit
        self.assertIsNone(content, "Scraper should return None for oversized responses")

    def test_invalid_scheme(self):
        """Test that non-HTTP/HTTPS URLs are rejected."""
        bad_urls = ["file:///etc/passwd", "ftp://example.com", "javascript:alert(1)"]
        for url in bad_urls:
            with patch('requests.get') as mock_get:
                content = self.scraper.fetch_page(url)
                self.assertIsNone(content, f"Scraper should reject non-http URL: {url}")
                mock_get.assert_not_called()
