import unittest
from bs4 import BeautifulSoup
import sys
import os
import asyncio

# Add parent directory to path so we can from scraper import WordpressScraperAsync
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import WordpressScraperAsync

class TestScraperLogic(unittest.TestCase):
    def setUp(self):
        self.scraper = WordpressScraperAsync("http://example.com", "out.json", "out.csv", "out.txt")
    def test_clean_text(self):
        text = "  Hello   World \xa0 "
        self.assertEqual(self.scraper.clean_text(text), "Hello World")

    def test_is_url(self):
        self.assertTrue(self.scraper.is_url("https://example.com"))
        self.assertFalse(self.scraper.is_url("Just text"))

    def test_extract_domain(self):
        self.assertEqual(self.scraper.extract_domain("https://www.example.com/page"), "example.com")
        self.assertIsNone(self.scraper.extract_domain(None))

    def test_extract_categories(self):
        html = '<article class="post category-tech category-news"></article>'
        soup = BeautifulSoup(html, 'lxml')
        article = soup.find('article')
        categories = self.scraper.extract_categories(article)
        self.assertIn("Tech", categories)
        self.assertIn("News", categories)

    def test_parse_html_content(self):
        html = """
        <html>
            <body>
                <article class="post">
                    <h1 class="entry-title"><a href="http://example.com/post1">Test Post</a></h1>
                    <time class="entry-date" datetime="2023-01-01">January 1, 2023</time>
                    <div class="entry-content">
                        <a href="https://external.com">External Link</a>
                    </div>
                </article>
            </body>
        </html>
        """
        posts = asyncio.run(self.scraper.parse_page(html))
        self.assertEqual(len(posts), 1)
        post = posts[0]
        self.assertEqual(post['title'], "Test Post")
        self.assertEqual(post['date'], "January 1, 2023")
        self.assertEqual(post['external_link'], "https://external.com")

if __name__ == '__main__':
    unittest.main()
