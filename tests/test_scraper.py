import unittest
import asyncio
from scraper import MarkPositionScraperAsync
from bs4 import BeautifulSoup

class TestScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = MarkPositionScraperAsync("dummy.json", "dummy.csv", "dummy.txt")
        self.sample_html = """
        <html><body>
        <article class="post">
            <h1 class="entry-title"><a href="http://example.com/1">Title 1</a></h1>
            <time class="entry-date" datetime="2023-01-01">January 1, 2023</time>
        </article>
        <div class="sidebar">Ignore me</div>
        <article class="post-123 post type-post">
            <h1 class="entry-title"><a href="http://example.com/2">Title 2</a></h1>
        </article>
        </body></html>
        """

    def test_clean_text(self):
        self.assertEqual(self.scraper.clean_text("  Hello   World  "), "Hello World")
        self.assertEqual(self.scraper.clean_text("Hello\xa0World"), "Hello World")

    def test_parse_page(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        results = loop.run_until_complete(self.scraper.parse_page(self.sample_html))
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]['title'], "Title 1")
        self.assertEqual(results[1]['title'], "Title 2")
        loop.close()

if __name__ == '__main__':
    unittest.main()
