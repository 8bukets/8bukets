import pytest
import aiohttp
from unittest.mock import AsyncMock, Mock
from scraper import OracleNewsScraper

@pytest.mark.asyncio
async def test_fetch_page_success():
    scraper = OracleNewsScraper("json", "csv", "txt")
    mock_session = AsyncMock(spec=aiohttp.ClientSession)
    mock_context = AsyncMock()
    # Use Mock for non-async attributes/methods if possible, or configure AsyncMock
    mock_response = AsyncMock()

    mock_response.status = 200
    mock_response.headers = {}
    mock_response.content.read.return_value = b"<html>Content</html>"

    # get_encoding is a synchronous method on ClientResponse
    # AsyncMock by default makes everything async.
    # We need to replace it with a Mock or set side_effect to return value directly if called.
    # But since mock_response is an AsyncMock, its children are AsyncMocks.

    # We can assign a Mock to the attribute name
    mock_response.get_encoding = Mock(return_value="utf-8")

    mock_context.__aenter__.return_value = mock_response
    mock_context.__aexit__.return_value = None
    mock_session.get.return_value = mock_context

    content = await scraper.fetch_page(mock_session, "http://example.com")
    assert content == "<html>Content</html>"

@pytest.mark.asyncio
async def test_fetch_page_content_length_exceeded():
    scraper = OracleNewsScraper("json", "csv", "txt")
    mock_session = AsyncMock(spec=aiohttp.ClientSession)
    mock_context = AsyncMock()
    mock_response = AsyncMock()

    mock_response.status = 200
    mock_response.headers = {'Content-Length': str(10 * 1024 * 1024 + 1)}

    mock_context.__aenter__.return_value = mock_response
    mock_context.__aexit__.return_value = None
    mock_session.get.return_value = mock_context

    content = await scraper.fetch_page(mock_session, "http://example.com")
    assert content is None

@pytest.mark.asyncio
async def test_fetch_page_actual_size_exceeded():
    scraper = OracleNewsScraper("json", "csv", "txt")
    mock_session = AsyncMock(spec=aiohttp.ClientSession)
    mock_context = AsyncMock()
    mock_response = AsyncMock()

    mock_response.status = 200
    mock_response.headers = {}
    mock_response.content.read.return_value = b"A" * (10 * 1024 * 1024 + 1)

    mock_context.__aenter__.return_value = mock_response
    mock_context.__aexit__.return_value = None
    mock_session.get.return_value = mock_context

    content = await scraper.fetch_page(mock_session, "http://example.com")
    assert content is None
