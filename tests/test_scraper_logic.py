import unittest
import asyncio
from scraper import OracleNewsScraper

class TestOracleNewsScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = OracleNewsScraper("test.json", "test.csv", "test.txt")

    def test_clean_text(self):
        text = "  This   is  a   test.  "
        cleaned = self.scraper.clean_text(text)
        self.assertEqual(cleaned, "This is a test.")

    def test_parse_page_logic(self):
        html = """
        <html>
            <body>
                <a href="/news/announcement/oracle-database-google-cloud-2025-01-01/">
                    <h3>Test Article Title</h3>
                </a>
                <a href="/other/link">Irrelevant</a>
                <a href="/news/announcement/ignore-me">No Google Cloud</a>
            </body>
        </html>
        """
        # Since parse_page is async in the original code, we run it with asyncio
        # After optimization, it might be sync or called via to_thread, but for now it is async

        # parse_page is now synchronous
        articles = self.scraper.parse_page(html)

        self.assertEqual(len(articles), 1)
        self.assertEqual(articles[0]['title'], "Test Article Title")
        self.assertEqual(articles[0]['date'], "2025-01-01")
        self.assertEqual(articles[0]['domain'], "oracle.com")

if __name__ == '__main__':
    unittest.main()
