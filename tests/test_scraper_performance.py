import unittest
from scraper import MarkPositionScraperAsync
from bs4 import BeautifulSoup
import asyncio

class TestScraperParsing(unittest.TestCase):
    def setUp(self):
        self.scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")
        self.html = """
        <article class="post category-tech">
            <h1 class="entry-title"><a href="http://example.com/post">Post Title</a></h1>
            <time class="entry-date" datetime="2023-01-01">January 1, 2023</time>
            <div class="author vcard"><span class="fn">Author Name</span></div>
            <div class="entry-content">
                <p>Some content here...</p>
                <a href="https://external.com">External Link</a>
            </div>
        </article>
        """

    def test_parse_page(self):
        # parse_page is now synchronous
        results = self.scraper.parse_page(self.html)
        self.assertEqual(len(results), 1)
        post = results[0]
        self.assertEqual(post['title'], "Post Title")
        self.assertEqual(post['date'], "January 1, 2023")
        self.assertEqual(post['author'], "Author Name")
        self.assertEqual(post['external_link'], "https://external.com")
        self.assertIn("Tech", post['categories'])

    def test_parse_page_no_articles(self):
        results = self.scraper.parse_page("<html><body></body></html>")
        self.assertEqual(results, [])

    def test_parse_page_missing_fields(self):
        html_missing = """
        <article class="post">
            <h1 class="entry-title">No Link</h1>
        </article>
        """
        results = self.scraper.parse_page(html_missing)
        self.assertEqual(len(results), 1)
        post = results[0]
        self.assertEqual(post['title'], "") # No A tag
        self.assertIsNone(post['author'])
        self.assertIsNone(post['external_link'])

if __name__ == '__main__':
    unittest.main()
