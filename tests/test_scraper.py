import unittest
import asyncio
from scraper import OracleNewsScraper

class TestOracleNewsScraper(unittest.TestCase):
    def test_clean_text(self):
        scraper = OracleNewsScraper("json", "csv", "txt")
        self.assertEqual(scraper.clean_text("  Hello   World  "), "Hello World")
        self.assertEqual(scraper.clean_text("Hello\xa0World"), "Hello World")

    def test_sanitize_for_csv(self):
        scraper = OracleNewsScraper("json", "csv", "txt")
        self.assertEqual(scraper.sanitize_for_csv("=cmd"), "'=cmd")
        self.assertEqual(scraper.sanitize_for_csv("Normal"), "Normal")

    def test_parse_page_logic(self):
        html = """
        <html>
            <body>
                <a href="/news/announcement/test-article-2025-01-01/"><h3>Test Title</h3></a>
                <a href="/other/link">Irrelevant</a>
                <a href="/news/announcement/google-cloud-article-2025-01-01/">Google Cloud Article</a>
            </body>
        </html>
        """
        scraper = OracleNewsScraper("json", "csv", "txt")

        # We need to run the async method
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        articles = loop.run_until_complete(scraper.parse_page(html))
        loop.close()

        # Only the google-cloud article should be found based on the logic in scraper.py
        # "Filter for "google-cloud" as requested"
        self.assertEqual(len(articles), 1)
        self.assertEqual(articles[0]['title'], "Google Cloud Article")
        self.assertTrue("google-cloud" in articles[0]['external_link'])

if __name__ == '__main__':
    unittest.main()
