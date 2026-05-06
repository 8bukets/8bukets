
import unittest
from unittest.mock import MagicMock, AsyncMock, patch
from scraper import OracleNewsScraper
import asyncio

class TestOracleNewsScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = OracleNewsScraper("test.json", "test.csv", "test.txt")

    def test_clean_text(self):
        self.assertEqual(self.scraper.clean_text("  hello   world  "), "hello world")
        self.assertEqual(self.scraper.clean_text(None), "")

    def test_sanitize_for_csv(self):
        self.assertEqual(self.scraper.sanitize_for_csv("=cmd"), "'=cmd")
        self.assertEqual(self.scraper.sanitize_for_csv("normal"), "normal")

    def test_parse_page(self):
        html = """
        <html>
            <body>
                <a href="/news/announcement/test-google-cloud-2023-01-01">Test Article</a>
                <a href="/news/announcement/ignore">Ignore</a>
                <a href="/other">Other</a>
            </body>
        </html>
        """
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        articles = loop.run_until_complete(self.scraper.parse_page(html))
        loop.close()

        self.assertEqual(len(articles), 1)
        self.assertEqual(articles[0]['title'], "Test Article")
        self.assertIn("google-cloud", articles[0]['post_url'])

if __name__ == '__main__':
    unittest.main()
