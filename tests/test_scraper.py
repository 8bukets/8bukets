import unittest
from scraper import OracleNewsScraper
import asyncio

class TestScraper(unittest.TestCase):
    def test_clean_text(self):
        scraper = OracleNewsScraper("dummy", "dummy", "dummy")
        self.assertEqual(scraper.clean_text("  hello   world  "), "hello world")
        self.assertEqual(scraper.clean_text("hello\xa0world"), "hello world")

    def test_sanitize_for_csv(self):
        scraper = OracleNewsScraper("dummy", "dummy", "dummy")
        self.assertEqual(scraper.sanitize_for_csv("normal"), "normal")
        self.assertEqual(scraper.sanitize_for_csv("=cmd"), "'=cmd")
        self.assertEqual(scraper.sanitize_for_csv("+cmd"), "'+cmd")
        self.assertEqual(scraper.sanitize_for_csv("-cmd"), "'-cmd")
        self.assertEqual(scraper.sanitize_for_csv("@cmd"), "'@cmd")

    def test_parse_page_logic(self):
        # We can test parsing logic with a small HTML snippet
        html = """
        <html>
            <a href="/news/announcement/oracle-database-at-google-cloud-is-now-available-in-region-2025-12-11/">
                <h3>Test Title</h3>
            </a>
            <a href="/other/link">Ignore me</a>
        </html>
        """
        scraper = OracleNewsScraper("dummy", "dummy", "dummy")

        async def run_test():
            results = await scraper.parse_page(html)
            self.assertEqual(len(results), 1)
            self.assertEqual(results[0]['title'], "Test Title")
            self.assertIn("oracle-database-at-google-cloud", results[0]['external_link'])

        asyncio.run(run_test())

if __name__ == '__main__':
    unittest.main()
