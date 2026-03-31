import unittest
import asyncio
from scraper import MarkPositionScraperAsync
from bs4 import BeautifulSoup
import os

class TestScraper(unittest.TestCase):
    def test_clean_text(self):
        scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")
        self.assertEqual(scraper.clean_text("  hello   world  "), "hello world")
        self.assertEqual(scraper.clean_text("hello\xa0world"), "hello world")

    def test_is_url(self):
        scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")
        self.assertTrue(scraper.is_url("https://example.com"))
        self.assertTrue(scraper.is_url("http://example.com"))
        self.assertFalse(scraper.is_url("example.com"))

    def test_extract_domain(self):
        scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")
        self.assertEqual(scraper.extract_domain("https://www.example.com/foo"), "example.com")
        self.assertEqual(scraper.extract_domain("http://example.com"), "example.com")

    def test_parse_page_structure(self):
        # Create a dummy HTML with article posts
        html = """
        <html>
            <body>
                <div class="header">Irrelevant content</div>
                <article class="post category-tech">
                    <h1 class="entry-title"><a href="http://example.com/post1">Post 1</a></h1>
                    <time class="entry-date" datetime="2023-01-01">Jan 1, 2023</time>
                    <div class="entry-content">
                        <a href="https://external.com">External Link</a>
                    </div>
                </article>
                <article class="post category-life">
                    <h1 class="entry-title"><a href="http://example.com/post2">Post 2</a></h1>
                    <div class="entry-content">
                        No external link here.
                    </div>
                </article>
                <div class="footer">Irrelevant footer</div>
            </body>
        </html>
        """
        scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        posts = loop.run_until_complete(scraper.parse_page(html))

        self.assertEqual(len(posts), 2)
        self.assertEqual(posts[0]['title'], "Post 1")
        self.assertEqual(posts[0]['categories'], ["Tech"])
        self.assertEqual(posts[0]['external_link'], "https://external.com")

        self.assertEqual(posts[1]['title'], "Post 2")
        self.assertEqual(posts[1]['categories'], ["Life"])
        # Post 2 has no external link and title is not a URL, so external_link might be None
        # Logic says: if not external_link and title_text and is_url(title_text)...
        self.assertIsNone(posts[1]['external_link'])

if __name__ == '__main__':
    unittest.main()
