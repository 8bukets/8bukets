import asyncio
import unittest
from unittest.mock import AsyncMock, MagicMock
import aiohttp
from scraper import MarkPositionScraperAsync

class TestScraperSecurity(unittest.IsolatedAsyncioTestCase):

    async def test_fetch_page_large_response(self):
        # Create a mock session and response
        mock_response = AsyncMock()
        mock_response.status = 200

        # Configure get_encoding to be a regular Mock returning a string
        mock_response.get_encoding = MagicMock(return_value='utf-8')

        # Configure headers to be a dict (or Mock behaving like one)
        mock_response.headers = MagicMock()
        mock_response.headers.get.side_effect = lambda k: str(20 * 1024 * 1024) if k == 'Content-Length' else None

        # Mock content iterator to yield a large amount of data
        # Each chunk is 1MB, yield 20 chunks
        chunk_size = 1024 * 1024

        async def iter_chunked_mock(n):
            for _ in range(20):
                yield b'a' * chunk_size

        mock_response.content.iter_chunked = iter_chunked_mock

        mock_response.raise_for_status = MagicMock()

        mock_response.__aenter__.return_value = mock_response
        mock_response.__aexit__.return_value = None

        mock_session = MagicMock(spec=aiohttp.ClientSession)
        mock_session.get.return_value = mock_response

        scraper = MarkPositionScraperAsync("json", "csv", "txt")

        # Run fetch_page
        result = await scraper.fetch_page(mock_session, 1)

        # With fix, it should return None (because it hits limit and returns None)
        self.assertIsNone(result, "Expected None for large response, but got content")


    async def test_fetch_page_normal_response(self):
        # Verify normal small response still works
        mock_response = AsyncMock()
        mock_response.status = 200

        # Fix: make get_encoding synchronous mock
        mock_response.get_encoding = MagicMock(return_value='utf-8')

        # Fix: make headers synchronous mock
        mock_response.headers = MagicMock()
        mock_response.headers.get.return_value = None

        async def iter_chunked_mock(n):
            yield b'Hello World'

        mock_response.content.iter_chunked = iter_chunked_mock
        mock_response.raise_for_status = MagicMock()
        mock_response.__aenter__.return_value = mock_response
        mock_response.__aexit__.return_value = None

        mock_session = MagicMock(spec=aiohttp.ClientSession)
        mock_session.get.return_value = mock_response

        scraper = MarkPositionScraperAsync("json", "csv", "txt")
        result = await scraper.fetch_page(mock_session, 1)

        self.assertEqual(result, "Hello World", "Expected 'Hello World' for normal response")

if __name__ == "__main__":
    unittest.main()
