import pytest
from unittest.mock import MagicMock
import sys
import os

# Ensure we can import from root
sys.path.append(os.getcwd())

import scrape_informatic

class TestScraperDoS:
    def test_content_length_limit(self):
        """Test that safe_get_content raises error if Content-Length header is too large."""
        session = MagicMock()
        mock_response = MagicMock()
        # 11MB
        mock_response.headers = {'Content-Length': str(11 * 1024 * 1024)}
        session.get.return_value = mock_response

        # We assume safe_get_content will be added to scrape_informatic
        with pytest.raises(ValueError, match="Content-Length .* exceeds maximum"):
            scrape_informatic.safe_get_content(session, "http://example.com/large")

    def test_stream_limit(self):
        """Test that safe_get_content raises error if actual content stream is too large."""
        session = MagicMock()
        mock_response = MagicMock()
        mock_response.headers = {} # No content length

        # Simulate a stream larger than 10MB
        def chunk_generator(chunk_size=8192):
            # Yield 10 chunks of 1MB + 1 chunk of 1KB to exceed 10MB
            # 10MB = 10 * 1024 * 1024 bytes
            chunk_1mb = b'a' * (1024 * 1024)
            for _ in range(10):
                yield chunk_1mb
            yield b'a' * 1024

        mock_response.iter_content = chunk_generator
        session.get.return_value = mock_response

        with pytest.raises(ValueError, match="Response size exceeds maximum"):
            scrape_informatic.safe_get_content(session, "http://example.com/stream")

    def test_safe_content(self):
        """Test that safe_get_content works for small content."""
        session = MagicMock()
        mock_response = MagicMock()
        mock_response.headers = {'Content-Length': '11'}
        mock_response.iter_content = lambda chunk_size=8192: [b'hello', b' world']
        session.get.return_value = mock_response

        content = scrape_informatic.safe_get_content(session, "http://example.com/safe")
        assert content == b'hello world'
