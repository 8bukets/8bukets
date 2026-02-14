
import unittest
from bs4 import BeautifulSoup, SoupStrainer
from scraper import MarkPositionScraperAsync
import asyncio

class TestScraperOptimization(unittest.TestCase):
    def setUp(self):
        self.scraper = MarkPositionScraperAsync("links.json", "links.csv", "unique_links.txt")
        self.html_content = """
        <html>
        <body>
            <div id="header">Header content</div>
            <div id="sidebar">Sidebar content</div>
            <main>
                <article class="post category-tech">
                    <header class="entry-header">
                        <h1 class="entry-title"><a href="http://example.com/post">Test Post Title</a></h1>
                        <time class="entry-date published" datetime="2023-10-27">October 27, 2023</time>
                        <span class="author vcard"><span class="fn">John Doe</span></span>
                    </header>
                    <div class="entry-content">
                        <p>Some content here with a <a href="https://external.com">link</a>.</p>
                    </div>
                </article>
            </main>
        </body>
        </html>
        """

    def test_clean_text_optimization(self):
        text = "   Some   text   with   spaces   "
        self.assertEqual(self.scraper.clean_text(text), "Some text with spaces")
        self.assertEqual(self.scraper.clean_text(None), "")

    def test_is_url_optimization(self):
        self.assertTrue(self.scraper.is_url("https://example.com"))
        self.assertTrue(self.scraper.is_url("http://example.com"))
        self.assertFalse(self.scraper.is_url("example.com"))

    def test_parse_page_optimization(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        results = loop.run_until_complete(self.scraper.parse_page(self.html_content))
        loop.close()

        self.assertEqual(len(results), 1)
        post = results[0]
        self.assertEqual(post['title'], "Test Post Title")
        self.assertEqual(post['date'], "October 27, 2023")
        self.assertEqual(post['author'], "John Doe")
        self.assertEqual(post['external_link'], "https://external.com")
        self.assertIn("Tech", post['categories'])

if __name__ == "__main__":
    unittest.main()
