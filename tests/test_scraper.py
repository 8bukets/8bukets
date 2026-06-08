import unittest
import asyncio
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import MarkPositionScraperAsync

class TestScraper(unittest.TestCase):
    def test_parse_page(self):
        scraper = MarkPositionScraperAsync("json", "csv", "txt")
        html = """
        <html>
            <article class="post">
                <h1 class="entry-title"><a href="http://example.com/post">Test Title</a></h1>
                <time class="entry-date" datetime="2023-01-01">January 1, 2023</time>
                <div class="entry-content">
                    <a href="http://external.com">External Link</a>
                </div>
            </article>
        </html>
        """

        # Check if parse_page is async or sync
        if asyncio.iscoroutinefunction(scraper.parse_page):
            result = asyncio.run(scraper.parse_page(html))
        else:
            result = scraper.parse_page(html)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['title'], "Test Title")
        self.assertEqual(result[0]['external_link'], "http://external.com")

if __name__ == '__main__':
    unittest.main()
