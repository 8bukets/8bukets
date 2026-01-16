import unittest
from unittest.mock import MagicMock, AsyncMock, patch
from scraper import MarkPositionScraperAsync
import asyncio

class TestScraper(unittest.TestCase):
    def test_clean_text(self):
        scraper = MarkPositionScraperAsync("out.json", "out.csv", "out.txt")
        self.assertEqual(scraper.clean_text("  hello   world  "), "hello world")
        self.assertEqual(scraper.clean_text("hello\xa0world"), "hello world")

    def test_is_url(self):
        scraper = MarkPositionScraperAsync("out.json", "out.csv", "out.txt")
        self.assertTrue(scraper.is_url("http://google.com"))
        self.assertTrue(scraper.is_url("https://google.com"))
        self.assertFalse(scraper.is_url("google.com"))

    def test_parse_page(self):
        html = """
        <article class="post category-tech">
            <h1 class="entry-title"><a href="http://example.com/post1">Test Post</a></h1>
            <div class="entry-content">
                <p>Some content here.</p>
                <a href="http://external.com">External Link</a>
            </div>
            <time class="entry-date" datetime="2023-01-01T12:00:00">January 1, 2023</time>
            <span class="author vcard"><span class="fn">Author Name</span></span>
        </article>
        """
        scraper = MarkPositionScraperAsync("out.json", "out.csv", "out.txt")
        # Since parse_page is now synchronous, we call it directly
        posts = scraper.parse_page(html)
        self.assertEqual(len(posts), 1)
        self.assertEqual(posts[0]['title'], "Test Post")
        self.assertEqual(posts[0]['author'], "Author Name")
        self.assertEqual(posts[0]['external_link'], "http://external.com")

    def test_fetch_and_parse(self):
        """Test that fetch_and_parse correctly offloads parsing to executor."""
        scraper = MarkPositionScraperAsync("out.json", "out.csv", "out.txt")

        # Mock fetch_page to return some HTML
        scraper.fetch_page = AsyncMock(return_value="<html></html>")

        # Mock parse_page
        scraper.parse_page = MagicMock(return_value=[{"title": "test"}])

        # We need a running loop for this test
        async def run_test():
            page_num, posts = await scraper.fetch_and_parse(None, 1)
            return page_num, posts

        page_num, posts = asyncio.run(run_test())

        self.assertEqual(page_num, 1)
        self.assertEqual(posts, [{"title": "test"}])
        scraper.parse_page.assert_called_once_with("<html></html>")

if __name__ == "__main__":
    unittest.main()
