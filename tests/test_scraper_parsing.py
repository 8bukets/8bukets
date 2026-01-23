import asyncio
import unittest
from scraper import MarkPositionScraperAsync

class TestScraper(unittest.TestCase):
    def test_parse_page(self):
        scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")
        html = """
        <html>
            <body>
                <article class="post category-tech">
                    <h1 class="entry-title"><a href="http://example.com/post">Test Title</a></h1>
                    <time class="entry-date" datetime="2023-01-01">January 1, 2023</time>
                    <div class="entry-content">
                        <a href="https://external.com">External Link</a>
                    </div>
                </article>
            </body>
        </html>
        """

        async def run_test():
            results = await scraper.parse_page(html)
            return results

        results = asyncio.run(run_test())

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['title'], "Test Title")
        self.assertEqual(results[0]['categories'], ["Tech"])
        self.assertEqual(results[0]['external_link'], "https://external.com")

if __name__ == '__main__':
    unittest.main()
