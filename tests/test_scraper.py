import unittest
import asyncio
from scraper import MarkPositionScraperAsync

class TestScraper(unittest.IsolatedAsyncioTestCase):
    async def test_parse_page(self):
        html = """
        <html>
            <body>
                <article class="post">
                    <header>
                        <h1 class="entry-title"><a href="http://example.com/1">Test Post 1</a></h1>
                        <time class="entry-date" datetime="2023-01-01">January 1, 2023</time>
                        <div class="author vcard"><span class="fn">Author 1</span></div>
                    </header>
                </article>
                <div class="sidebar">Ignore this</div>
            </body>
        </html>
        """
        scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")
        result = await scraper.parse_page(html)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['title'], "Test Post 1")

if __name__ == '__main__':
    unittest.main()
