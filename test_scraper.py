
import pytest
import asyncio
from scraper import MarkPositionScraperAsync

class MockResponse:
    def __init__(self, text, status=200):
        self._text = text
        self.status = status

    async def text(self):
        return self._text

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass

    def raise_for_status(self):
        pass

class MockSession:
    def __init__(self, html):
        self.html = html

    def get(self, url):
        return MockResponse(self.html)

HTML_CONTENT = """
<article class="post category-tech">
 <h1 class="entry-title"><a href="http://example.com/post1">Title 1</a></h1>
 <time class="entry-date" datetime="2023-01-01">January 1, 2023</time>
 <div class="author vcard"><span class="fn">Author Name</span></div>
 <div class="entry-content">
  <a href="http://external.com/1">External Link 1</a>
 </div>
</article>
"""

@pytest.mark.asyncio
async def test_scraper_parsing():
    scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")

    # Test parse_page directly (it is now sync)
    posts = scraper.parse_page(HTML_CONTENT)
    assert len(posts) == 1
    assert posts[0]['title'] == "Title 1"
    assert posts[0]['external_link'] == "http://external.com/1"

@pytest.mark.asyncio
async def test_fetch_and_parse_integration():
    scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")
    sem = asyncio.Semaphore(1)

    # Mock fetch_page to return HTML_CONTENT
    async def mock_fetch(session, page_num):
        return HTML_CONTENT

    scraper.fetch_page = mock_fetch

    posts = await scraper.fetch_and_parse(None, 1, sem)
    assert len(posts) == 1
    assert posts[0]['title'] == "Title 1"

def test_clean_text():
    scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")
    assert scraper.clean_text("  hello   world  ") == "hello world"
    assert scraper.clean_text("hello\xa0world") == "hello world"
