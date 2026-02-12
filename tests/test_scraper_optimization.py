
import unittest
import asyncio
from bs4 import BeautifulSoup
from scraper import MarkPositionScraperAsync

class TestScraperOptimization(unittest.TestCase):
    def setUp(self):
        self.scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")
        self.sample_html = """
        <html>
            <body>
                <div class="header">Ignore me</div>
                <article class="post-123 post type-post status-publish">
                    <h1 class="entry-title"><a href="http://example.com/post1">Test Post 1</a></h1>
                    <time class="entry-date" datetime="2023-01-01T12:00:00+00:00">January 1, 2023</time>
                    <div class="entry-content">
                        <a href="https://external.com">Link</a>
                    </div>
                </article>
                <article class="other-class">Ignore me too</article>
                <div class="sidebar">Ignore me too</div>
                <article class="post-124 post">
                    <h1 class="entry-title"><a href="http://example.com/post2">Test Post 2</a></h1>
                </article>
            </body>
        </html>
        """

    def test_parse_page_correctness(self):
        # Run async method
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        results = loop.run_until_complete(self.scraper.parse_page(self.sample_html))
        loop.close()

        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]['title'], "Test Post 1")
        self.assertEqual(results[0]['external_link'], "https://external.com")
        self.assertEqual(results[1]['title'], "Test Post 2")

    def test_parse_page_empty(self):
        html = "<html><body>No posts here</body></html>"
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        results = loop.run_until_complete(self.scraper.parse_page(html))
        loop.close()
        self.assertEqual(len(results), 0)

if __name__ == '__main__':
    unittest.main()
