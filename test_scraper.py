import unittest
import asyncio
from bs4 import BeautifulSoup
from scraper import MarkPositionScraperAsync

SAMPLE_HTML = """
<html>
<body>
    <header>Some header</header>
    <article class="post">
        <h1 class="entry-title"><a href="http://example.com/post1">Post 1</a></h1>
        <time class="entry-date" datetime="2023-01-01">January 1, 2023</time>
        <div class="author vcard"><span class="fn">John Doe</span></div>
        <div class="entry-content">
            <p>Some content</p>
            <a href="https://external.com">External Link</a>
        </div>
    </article>
    <article class="post category-tech">
        <h1 class="entry-title"><a href="http://example.com/post2">Post 2</a></h1>
        <div class="entry-content">
            <iframe src="https://video.com"></iframe>
        </div>
    </article>
    <footer>Some footer</footer>
</body>
</html>
"""

class TestScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = MarkPositionScraperAsync("json", "csv", "txt")

    def test_clean_text(self):
        self.assertEqual(self.scraper.clean_text("  hello   world  "), "hello world")
        self.assertEqual(self.scraper.clean_text("hello\xa0world"), "hello world")
        self.assertEqual(self.scraper.clean_text(None), "")

    def test_is_url(self):
        self.assertTrue(self.scraper.is_url("https://example.com"))
        self.assertTrue(self.scraper.is_url("http://example.com"))
        self.assertFalse(self.scraper.is_url("example.com"))
        self.assertFalse(self.scraper.is_url("ftp://example.com")) # Regex is ^https?://

    def test_parse_page(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        posts = loop.run_until_complete(self.scraper.parse_page(SAMPLE_HTML))

        self.assertEqual(len(posts), 2)

        # Post 1
        p1 = posts[0]
        self.assertEqual(p1['title'], "Post 1")
        self.assertEqual(p1['date'], "January 1, 2023")
        self.assertEqual(p1['author'], "John Doe")
        self.assertEqual(p1['external_link'], "https://external.com")

        # Post 2
        p2 = posts[1]
        self.assertEqual(p2['title'], "Post 2")
        self.assertEqual(p2['external_link'], "https://video.com")
        self.assertIn("Tech", p2['categories'])

if __name__ == '__main__':
    unittest.main()
