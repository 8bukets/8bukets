
import pytest
import aiohttp
import asyncio
from unittest.mock import MagicMock, patch, AsyncMock
from scraper import MarkPositionScraperAsync

# Mocking the response object
class MockResponse:
    def __init__(self, text_content=None, content_length=None, chunks=None):
        self.status = 200
        self._text_content = text_content
        self._content_length = content_length
        self._chunks = chunks or []
        self.content = MagicMock()

        # Mock iter_chunked
        async def iter_chunked(n):
            for chunk in self._chunks:
                yield chunk
        self.content.iter_chunked = iter_chunked

    async def text(self):
        return self._text_content

    def raise_for_status(self):
        pass

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        pass

@pytest.mark.asyncio
async def test_fetch_page_large_response_dos():
    """
    Test that the scraper handles large responses.
    The scraper should reject responses larger than 10MB.
    """
    scraper = MarkPositionScraperAsync("json", "csv", "txt")

    # 15MB content
    large_content = b"a" * (15 * 1024 * 1024)

    # We need to mock session.get to return our MockResponse
    with patch('aiohttp.ClientSession.get') as mock_get:
        session = MagicMock(spec=aiohttp.ClientSession)
        session.get = mock_get

        # Prepare chunks for the fix verification
        chunks = [b"a" * 1024 * 1024] * 15 # 15 chunks of 1MB
        mock_response_chunked = MockResponse(chunks=chunks, text_content=large_content.decode('utf-8'))
        mock_get.return_value = mock_response_chunked

        # If the fix works, it should return None because 15MB > 10MB limit.
        result = await scraper.fetch_page(session, 1)

        assert result is None, "Expected fetch_page to return None for oversize response, but got content."

if __name__ == "__main__":
    asyncio.run(test_fetch_page_large_response_dos())
