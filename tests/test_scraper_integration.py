import unittest
import asyncio
from unittest.mock import MagicMock, patch
import sys
import os

# Add parent dir to path to import scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import parse_html_content, MarkPositionScraperAsync
import concurrent.futures

class TestScraper(unittest.TestCase):
    def test_parse_html_content(self):
        html = """
        <html>
        <body>
            <article class="post category-tech">
                <h1 class="entry-title"><a href="http://example.com/post/1">Test Title</a></h1>
                <div class="entry-content">
                    <p>Content</p>
                    <a href="https://external.com">External Link</a>
                </div>
            </article>
        </body>
        </html>
        """
        results = parse_html_content(html)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['title'], 'Test Title')
        self.assertEqual(results[0]['external_link'], 'https://external.com')
        self.assertEqual(results[0]['categories'], ['Tech'])

    def test_fetch_and_parse_integration(self):
        # valid async test needs an event loop
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")

        # Mock fetch_page to return HTML
        async def mock_fetch_page(session, page):
            return """
            <html>
            <body>
                <article class="post">
                    <h1 class="entry-title"><a href="#">Test</a></h1>
                </article>
            </body>
            </html>
            """

        scraper.fetch_page = mock_fetch_page

        # We need a real executor
        with concurrent.futures.ProcessPoolExecutor(max_workers=1) as pool:
            # We mock session as it's not used by our mock_fetch_page
            session = MagicMock()

            result = loop.run_until_complete(scraper.fetch_and_parse(session, 1, pool))

            self.assertEqual(result[0], 1)
            self.assertEqual(len(result[1]), 1)
            self.assertEqual(result[1][0]['title'], 'Test')

        loop.close()

if __name__ == '__main__':
    unittest.main()
