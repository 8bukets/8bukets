import unittest
import asyncio
from scraper import OracleNewsScraper
import os

class TestOracleNewsScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = OracleNewsScraper("test_links.json", "test_links.csv", "test_links.txt")

    def tearDown(self):
        # Clean up files if they were created (scraper init doesn't create them, scrape does)
        for f in ["test_links.json", "test_links.csv", "test_links.txt"]:
            if os.path.exists(f):
                os.remove(f)

    def test_parse_page(self):
        html = """
        <html>
            <body>
                <div class="news-list">
                    <a href="/news/announcement/oracle-database-google-cloud-2023-01-01/">
                        <h3>Oracle Database Service for Google Cloud</h3>
                    </a>
                    <!-- Irrelevant link -->
                    <a href="/news/other-thing">Other</a>
                </div>
            </body>
        </html>
        """

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            articles = loop.run_until_complete(self.scraper.parse_page(html))
        finally:
            loop.close()

        self.assertEqual(len(articles), 1)
        self.assertEqual(articles[0]['title'], "Oracle Database Service for Google Cloud")
        self.assertEqual(articles[0]['date'], "2023-01-01")
        self.assertIn("google-cloud", articles[0]['post_url'])

    def test_parse_page_no_match(self):
        html = """
        <html>
            <body>
                <a href="/news/announcement/irrelevant-topic/">Nothing here</a>
            </body>
        </html>
        """
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            articles = loop.run_until_complete(self.scraper.parse_page(html))
        finally:
            loop.close()

        self.assertEqual(len(articles), 0)

if __name__ == '__main__':
    unittest.main()
