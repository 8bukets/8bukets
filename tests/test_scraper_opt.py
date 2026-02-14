
import unittest
import asyncio
from scraper import MarkPositionScraperAsync

class TestScraper(unittest.IsolatedAsyncioTestCase):
    async def test_parse_page_integration(self):
        scraper = MarkPositionScraperAsync("dummy.json", "dummy.csv", "dummy.txt")

        html = """
        <html>
            <head><title>Test</title></head>
            <body>
                <header>Header</header>
                <article class="post">
                    <h1 class="entry-title"><a href="http://example.com/post1">Post 1</a></h1>
                    <time class="entry-date" datetime="2021-01-01">January 1, 2021</time>
                    <div class="entry-content">
                        <a href="http://external.com/1">External Link 1</a>
                    </div>
                </article>
                <div class="sidebar">Sidebar</div>
                <article class="post">
                    <h1 class="entry-title"><a href="http://example.com/post2">Post 2</a></h1>
                    <time class="entry-date" datetime="2021-01-02">January 2, 2021</time>
                </article>
                <footer>Footer</footer>
            </body>
        </html>
        """

        results = await scraper.parse_page(html)

        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]['title'], "Post 1")
        self.assertEqual(results[0]['external_link'], "http://external.com/1")
        self.assertEqual(results[1]['title'], "Post 2")

        # Ensure that unrelated content didn't break parsing
        # (SoupStrainer('article') should have allowed finding these articles)

if __name__ == '__main__':
    unittest.main()
