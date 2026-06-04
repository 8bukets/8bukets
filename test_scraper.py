import unittest
import asyncio
from scraper import MarkPositionScraperAsync

class TestScraper(unittest.TestCase):
    def setUp(self):
        self.html = """
        <html>
        <body>
            <article class="post category-tech">
                <header class="entry-header">
                    <h1 class="entry-title"><a href="http://example.com/post1">Test Post 1</a></h1>
                    <time class="entry-date" datetime="2023-01-01">Jan 1, 2023</time>
                    <span class="author vcard"><span class="fn">Author One</span></span>
                </header>
                <div class="entry-content">
                    <a href="http://external.com/link1">External Link</a>
                </div>
            </article>
        </body>
        </html>
        """
        self.scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")

    def test_clean_text(self):
        self.assertEqual(self.scraper.clean_text("  Hello   World  "), "Hello World")

    def test_parse_page(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        results = loop.run_until_complete(self.scraper.parse_page(self.html))
        loop.close()

        self.assertEqual(len(results), 1)
        post = results[0]
        self.assertEqual(post['title'], "Test Post 1")
        self.assertEqual(post['author'], "Author One")
        self.assertEqual(post['external_link'], "http://external.com/link1")
        self.assertIn("Tech", post['categories'])
from scraper import MarkPositionScraperAsync

class TestMarkPositionScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")

    def test_clean_text(self):
        self.assertEqual(self.scraper.clean_text("  hello   world  "), "hello world")
        self.assertEqual(self.scraper.clean_text("hello\xa0world"), "hello world")
        self.assertEqual(self.scraper.clean_text("  \t\n hello \n "), "hello")
        self.assertEqual(self.scraper.clean_text(""), "")
        self.assertEqual(self.scraper.clean_text(None), "")

    def test_is_url(self):
        self.assertTrue(self.scraper.is_url("http://example.com"))
        self.assertTrue(self.scraper.is_url("https://example.com"))
        self.assertTrue(self.scraper.is_url(" https://example.com "))
        self.assertFalse(self.scraper.is_url("ftp://example.com"))
        self.assertFalse(self.scraper.is_url("example.com"))
        self.assertFalse(self.scraper.is_url(""))

    def test_clean_text_complex(self):
        text = "This   is  a    sample   text   with   lots  of   spaces.   "
        expected = "This is a sample text with lots of spaces."
        self.assertEqual(self.scraper.clean_text(text), expected)

if __name__ == '__main__':
    unittest.main()
