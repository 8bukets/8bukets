import unittest
import asyncio
from unittest.mock import MagicMock, AsyncMock
import sys
import os

# Add parent directory to path to import scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import MarkPositionScraperAsync

class TestDoS(unittest.TestCase):
    def test_large_response(self):
        # Create a mock session
        mock_session = MagicMock()

        # Create a mock response
        mock_response = AsyncMock()
        mock_response.status = 200

        async def mock_iter_chunked(chunk_size):
            # Yield chunks that sum up to > 10MB
            for _ in range(11):
                yield b"a" * (1024 * 1024)

        mock_response.content.iter_chunked = mock_iter_chunked
        mock_response.get_encoding = MagicMock(return_value='utf-8')

        mock_session.get.return_value.__aenter__.return_value = mock_response
        mock_session.get.return_value.__aexit__.return_value = None

        scraper = MarkPositionScraperAsync("json", "csv", "txt")
        result = asyncio.run(scraper.fetch_page(mock_session, 1))

        self.assertIsNone(result)

    def test_normal_response(self):
        # Create a mock session
        mock_session = MagicMock()

        # Create a mock response
        mock_response = AsyncMock()
        mock_response.status = 200

        async def mock_iter_chunked(chunk_size):
            yield b"Hello World"

        mock_response.content.iter_chunked = mock_iter_chunked
        mock_response.get_encoding = MagicMock(return_value='utf-8')

        mock_session.get.return_value.__aenter__.return_value = mock_response
        mock_session.get.return_value.__aexit__.return_value = None

        scraper = MarkPositionScraperAsync("json", "csv", "txt")
        result = asyncio.run(scraper.fetch_page(mock_session, 1))

        self.assertEqual(result, "Hello World")

    def test_missing_encoding(self):
        # Test fallback to utf-8 when get_encoding returns None
        mock_session = MagicMock()
        mock_response = AsyncMock()
        mock_response.status = 200

        async def mock_iter_chunked(chunk_size):
            yield b"Hello World"

        mock_response.content.iter_chunked = mock_iter_chunked
        # Simulate missing encoding
        mock_response.get_encoding = MagicMock(return_value=None)

        mock_session.get.return_value.__aenter__.return_value = mock_response
        mock_session.get.return_value.__aexit__.return_value = None

        scraper = MarkPositionScraperAsync("json", "csv", "txt")
        result = asyncio.run(scraper.fetch_page(mock_session, 1))

        self.assertEqual(result, "Hello World")

if __name__ == '__main__':
    unittest.main()
