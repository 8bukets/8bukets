import unittest
from bs4 import BeautifulSoup
import sys
import os

# Add parent directory to path so we can import scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import scraper

class TestScraperLogic(unittest.TestCase):
    def test_clean_text(self):
        text = "  Hello   World \xa0 "
        self.assertEqual(scraper.clean_text(text), "Hello World")

    def test_is_url(self):
        self.assertTrue(scraper.is_url("https://example.com"))
        self.assertFalse(scraper.is_url("Just text"))

    def test_extract_domain(self):
        self.assertEqual(scraper.extract_domain("https://www.example.com/page"), "example.com")
        self.assertIsNone(scraper.extract_domain(None))

    def test_extract_categories(self):
        html = '<article class="post category-tech category-news"></article>'
        soup = BeautifulSoup(html, 'html.parser')
        article = soup.find('article')
        categories = scraper.extract_categories(article)
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
        posts = scraper.parse_html_content(html)
        self.assertEqual(len(posts), 1)
        post = posts[0]
        self.assertEqual(post['title'], "Test Post")
        self.assertEqual(post['date'], "January 1, 2023")
        self.assertEqual(post['external_link'], "https://external.com")

if __name__ == '__main__':
    unittest.main()
