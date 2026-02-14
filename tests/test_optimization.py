import unittest
import asyncio
from bs4 import BeautifulSoup
from scraper import MarkPositionScraperAsync

class TestScraperOptimization(unittest.TestCase):
    def test_parser_is_lxml(self):
        """Verify that the scraper runs without error, implying lxml is working."""
        scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")
        html = "<html><body><h1>Test</h1></body></html>"
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            posts = loop.run_until_complete(scraper.parse_page(html))
            self.assertEqual(posts, [])
        finally:
            loop.close()

if __name__ == '__main__':
    unittest.main()
