
import unittest
import asyncio
from bs4 import BeautifulSoup
from scraper import MarkPositionScraperAsync

class TestScraperOptimization(unittest.TestCase):
    def setUp(self):
        self.scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")

    def test_regex_precompilation(self):
        # Test clean_text with various inputs
        self.assertEqual(self.scraper.clean_text("  hello   world  "), "hello world")
        self.assertEqual(self.scraper.clean_text("foo\xa0bar"), "foo bar")
        self.assertEqual(self.scraper.clean_text(""), "")
        self.assertEqual(self.scraper.clean_text(None), "")

    def test_is_url(self):
        self.assertTrue(self.scraper.is_url("http://example.com"))
        self.assertTrue(self.scraper.is_url("https://example.com"))
        self.assertFalse(self.scraper.is_url("example.com"))
        self.assertFalse(self.scraper.is_url("ftp://example.com"))

    def test_parse_logic(self):
        html = """
        <article class="post">
            <h1 class="entry-title"><a href="http://link.com">Test Title</a></h1>
            <time class="entry-date" datetime="2023-01-01">Jan 1, 2023</time>
            <div class="entry-content">
                <p>Content</p>
            </div>
        </article>
        """
        # Run async method in sync test wrapper
        posts = asyncio.run(self.scraper.parse_page(html))
        self.assertEqual(len(posts), 1)
        self.assertEqual(posts[0]['title'], "Test Title")
        self.assertEqual(posts[0]['date'], "Jan 1, 2023")

if __name__ == '__main__':
    unittest.main()
