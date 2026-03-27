import pytest
import asyncio
from scraper import MarkPositionScraperAsync

class TestScraper:
    def setup_method(self):
        self.scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")

    def test_clean_text(self):
        assert self.scraper.clean_text("  Hello   World  ") == "Hello World"
        assert self.scraper.clean_text("Hello\xa0World") == "Hello World"

    def test_is_url(self):
        assert self.scraper.is_url("http://google.com")
        assert self.scraper.is_url("https://google.com")
        assert not self.scraper.is_url("google.com")

    @pytest.mark.asyncio
    async def test_parse_page(self):
        html = """
        <article class="post">
            <h1 class="entry-title"><a href="http://example.com/post1">Test Title</a></h1>
            <time class="entry-date" datetime="2023-01-01">January 1, 2023</time>
            <div class="author vcard"><span class="fn">Author Name</span></div>
            <div class="entry-content">
                <p>Content</p>
            </div>
        </article>
        """
        # Handle both async (current) and sync (future) implementation
        if asyncio.iscoroutinefunction(self.scraper.parse_page):
            posts = await self.scraper.parse_page(html)
        else:
            posts = self.scraper.parse_page(html)

        assert len(posts) == 1
        assert posts[0]['title'] == "Test Title"
        assert posts[0]['author'] == "Author Name"
        assert posts[0]['date'] == "January 1, 2023"
