import unittest
import asyncio
from scraper import MarkPositionScraperAsync

class TestScraperVuln(unittest.TestCase):
    def test_javascript_link_extraction(self):
        scraper = MarkPositionScraperAsync("json", "csv", "txt")
        html = """
        <article class="post">
            <h1 class="entry-title"><a href="http://example.com/post">Post Title</a></h1>
            <div class="entry-content">
                <a href="javascript:alert('XSS')">Click me</a>
            </div>
        </article>
        """

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        results = loop.run_until_complete(scraper.parse_page(html))
        loop.close()

        self.assertEqual(len(results), 1)
        # Should not extract dangerous schemes
        self.assertIsNone(results[0]['external_link'])

    def test_valid_link_extraction(self):
        scraper = MarkPositionScraperAsync("json", "csv", "txt")
        html = """
        <article class="post">
            <h1 class="entry-title"><a href="http://example.com/post">Post Title</a></h1>
            <div class="entry-content">
                <a href="https://example.com/valid">Click me</a>
            </div>
        </article>
        """

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        results = loop.run_until_complete(scraper.parse_page(html))
        loop.close()

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['external_link'], "https://example.com/valid")

if __name__ == '__main__':
    unittest.main()
