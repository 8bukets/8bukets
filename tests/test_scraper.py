import pytest
import asyncio
from unittest.mock import AsyncMock, MagicMock, patch
from scraper import MarkPositionScraperAsync

SAMPLE_HTML = """
<!DOCTYPE html>
<html>
<body>
    <article class="post category-tech">
        <header>
            <h1 class="entry-title"><a href="https://example.com/post1">Test Post Title</a></h1>
            <time class="entry-date" datetime="2023-10-27T10:00:00+00:00">October 27, 2023</time>
        </header>
        <div class="entry-content">
            <p>Some content here.</p>
            <a href="https://external-link.com">External Link</a>
        </div>
        <div class="author vcard"><span class="fn">John Doe</span></div>
    </article>
</body>
</html>
"""

@pytest.mark.asyncio
async def test_parse_page_extracts_data():
    scraper = MarkPositionScraperAsync("links.json", "links.csv", "unique_links.txt")

    posts = await scraper.parse_page(SAMPLE_HTML)

    assert len(posts) == 1
    post = posts[0]
    assert post['title'] == "Test Post Title"
    assert post['date'] == "October 27, 2023"
    assert post['datetime'] == "2023-10-27T10:00:00+00:00"
    assert post['author'] == "John Doe"
    assert "Tech" in post['categories']
    assert post['external_link'] == "https://external-link.com"
    assert post['domain'] == "external-link.com"

@pytest.mark.asyncio
async def test_parse_page_no_articles():
    scraper = MarkPositionScraperAsync("links.json", "links.csv", "unique_links.txt")
    posts = await scraper.parse_page("<html><body>No posts here</body></html>")
    assert len(posts) == 0

@pytest.mark.asyncio
async def test_scrape_flow():
    # Mocking the network call
    with patch('aiohttp.ClientSession.get') as mock_get:
        mock_response = AsyncMock()
        mock_response.status = 200
        mock_response.text.return_value = SAMPLE_HTML
        mock_response.__aenter__.return_value = mock_response
        mock_get.return_value = mock_response

        scraper = MarkPositionScraperAsync("links.json", "links.csv", "unique_links.txt", max_pages=1, concurrency=1)

        # We need to mock save_data to avoid file writes during test
        scraper.save_data = MagicMock()

        await scraper.scrape()

        scraper.save_data.assert_called_once()
        args, _ = scraper.save_data.call_args
        assert len(args[0]) == 1
        assert args[0][0]['title'] == "Test Post Title"
