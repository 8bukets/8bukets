import pytest
import asyncio
from unittest.mock import MagicMock, patch, AsyncMock
from scraper import OracleNewsScraper

@pytest.mark.asyncio
async def test_parse_page():
    scraper = OracleNewsScraper("json", "csv", "txt")

    html = """
    <html>
        <body>
            <a href="/news/announcement/test-article-2025-01-01/"><h3>Test Article</h3></a>
            <a href="/news/announcement/ignore-me/"><h3>Ignore Me</h3></a>
            <a href="/news/announcement/google-cloud-article-2025-01-02/"><h3>Google Cloud Article</h3></a>
        </body>
    </html>
    """

    # The current logic filters for 'google-cloud' in href

    articles = await scraper.parse_page(html)

    # We expect 1 article because one matches 'google-cloud'
    assert len(articles) == 1
    assert articles[0]['title'] == "Google Cloud Article"
    assert articles[0]['date'] == "2025-01-02"
    assert articles[0]['domain'] == "oracle.com"

def test_clean_text():
    scraper = OracleNewsScraper("json", "csv", "txt")
    text = "  Hello   World \xa0 "
    cleaned = scraper.clean_text(text)
    assert cleaned == "Hello World"

@pytest.mark.asyncio
async def test_scrape_flow():
    # Mocking the network parts to test the flow
    scraper = OracleNewsScraper("json", "csv", "txt")

    # Mock check_robots_txt
    scraper.check_robots_txt = AsyncMock(return_value=True)

    # Mock fetch_page
    scraper.fetch_page = MagicMock(return_value=asyncio.Future())
    scraper.fetch_page.return_value.set_result("""
    <html>
        <body>
            <a href="/news/announcement/google-cloud-article-2025-01-02/"><h3>Google Cloud Article</h3></a>
        </body>
    </html>
    """)

    # Mock save_data to prevent file writes
    scraper.save_data = MagicMock()

    await scraper.scrape()

    assert scraper.check_robots_txt.called
    scraper.save_data.assert_called_once()
    saved_posts = scraper.save_data.call_args[0][0]
    assert len(saved_posts) == 1
    assert saved_posts[0]['title'] == "Google Cloud Article"
