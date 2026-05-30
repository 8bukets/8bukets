import unittest
from unittest.mock import patch, MagicMock
import asyncio
from bs4 import BeautifulSoup
from scraper import WordpressScraperAsync

class TestWordpressScraperAsync(unittest.TestCase):
    def setUp(self):
        self.scraper = WordpressScraperAsync(
            base_url="https://example.com/",
            output_json="test.json",
            output_csv="test.csv",
            output_txt="test.txt"
        )

    def test_clean_text(self):
        self.assertEqual(self.scraper.clean_text("  Hello   World  "), "Hello World")
        self.assertEqual(self.scraper.clean_text("No\xa0Break"), "No Break")
        self.assertEqual(self.scraper.clean_text(None), "")

    def test_is_url(self):
        self.assertTrue(self.scraper.is_url("https://example.com"))
        self.assertTrue(self.scraper.is_url("http://example.com"))
        self.assertFalse(self.scraper.is_url("example.com"))
        self.assertFalse(self.scraper.is_url("Not a URL"))

    def test_extract_domain(self):
        self.assertEqual(self.scraper.extract_domain("https://www.example.com/page"), "example.com")
        self.assertEqual(self.scraper.extract_domain("http://sub.example.com"), "sub.example.com")
        self.assertIsNone(self.scraper.extract_domain(None))

    def test_extract_categories(self):
        html = '<article class="post category-music category-news"></article>'
        soup = BeautifulSoup(html, 'html.parser')
        article = soup.find('article')
        categories = self.scraper.extract_categories(article)
        self.assertIn("Music", categories)
        self.assertIn("News", categories)

    def test_parse_page(self):
        html = """
        <html>
            <body>
                <article class="post">
                    <h2 class="entry-title"><a href="https://example.com/post1">Test Post</a></h2>
                    <time class="entry-date" datetime="2023-01-01">January 1, 2023</time>
                    <div class="entry-content">
                        <a href="https://external.com">External Link</a>
                    </div>
                    <span class="author vcard"><a class="fn">Test Author</a></span>
                </article>
            </body>
        </html>
        """
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        posts = loop.run_until_complete(self.scraper.parse_page(html))

        self.assertEqual(len(posts), 1)
        post = posts[0]
        self.assertEqual(post['title'], "Test Post")
        self.assertEqual(post['date'], "January 1, 2023")
        self.assertEqual(post['author'], "Test Author")
        self.assertEqual(post['external_link'], "https://external.com")
        self.assertEqual(post['domain'], "external.com")
        self.assertEqual(post['post_url'], "https://example.com/post1")

if __name__ == '__main__':
    unittest.main()
