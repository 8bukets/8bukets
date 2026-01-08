import unittest
from unittest.mock import MagicMock, AsyncMock, patch, Mock
import aiohttp
import asyncio
from scraper import MarkPositionScraperAsync

class TestScraper(unittest.IsolatedAsyncioTestCase):
    async def test_parse_page(self):
        scraper = MarkPositionScraperAsync("json", "csv", "txt")
        html = """
        <html>
            <body>
                <article class="post">
                    <h1 class="entry-title"><a href="http://example.com/post">Test Title</a></h1>
                    <time class="entry-date" datetime="2023-01-01">January 1, 2023</time>
                    <div class="author vcard"><span class="fn">Test Author</span></div>
                    <div class="entry-content">
                        <a href="http://external.com">External Link</a>
                    </div>
                </article>
            </body>
        </html>
        """
        # parse_page is now synchronous
        posts = scraper.parse_page(html)
        self.assertEqual(len(posts), 1)
        self.assertEqual(posts[0]['title'], "Test Title")
        self.assertEqual(posts[0]['external_link'], "http://external.com")

    async def test_fetch_and_parse(self):
        scraper = MarkPositionScraperAsync("json", "csv", "txt")
        # fetch_page remains async
        scraper.fetch_page = AsyncMock(return_value="<html></html>")
        # parse_page is now synchronous, so we mock it with a regular Mock
        scraper.parse_page = Mock(return_value=[])

        sem = asyncio.Semaphore(1)
        session = MagicMock()

        result = await scraper.fetch_and_parse(session, 1, sem)
        self.assertEqual(result, [])
        scraper.fetch_page.assert_called_once()
        scraper.parse_page.assert_called_once()

if __name__ == '__main__':
    unittest.main()
