import unittest
from bs4 import BeautifulSoup
from scraper import BlogScraper
import os

class TestBlogScraperSecurity(unittest.TestCase):
    def setUp(self):
        # We don't need real DB or JSON for this test
        self.db_name = "test_security.db"
        self.json_name = "test_security.json"
        self.scraper = BlogScraper("http://mock.url", self.json_name, self.db_name)

    def tearDown(self):
        if os.path.exists(self.db_name):
            os.remove(self.db_name)
        if os.path.exists(self.json_name):
            os.remove(self.json_name)

    def test_parse_article_xss_urls(self):
        # Malicious HTML
        malicious_html = """
        <html>
            <body>
                <article>
                    <header class="entry-header">
                        <h2 class="entry-title"><a href="javascript:alert('XSS')">Malicious Title</a></h2>
                    </header>
                    <div class="entry-content">
                        <a href="javascript:steal_cookie()">Click Me</a>
                    </div>
                </article>
            </body>
        </html>
        """
        soup = BeautifulSoup(malicious_html, 'html.parser')
        article = soup.find('article')
        item = self.scraper.parse_article(article)

        # Expectation: malicious URLs are filtered out (None)
        self.assertIsNone(item['post_url'], "Javascript URL in post_url should be None")
        self.assertIsNone(item['external_link'], "Javascript URL in external_link should be None")

    def test_parse_article_valid_urls(self):
        valid_html = """
        <html>
            <body>
                <article>
                    <header class="entry-header">
                        <h2 class="entry-title"><a href="https://example.com/good">Good Title</a></h2>
                    </header>
                    <div class="entry-content">
                        <a href="http://external.com/good">External</a>
                    </div>
                </article>
            </body>
        </html>
        """
        soup = BeautifulSoup(valid_html, 'html.parser')
        article = soup.find('article')
        item = self.scraper.parse_article(article)

        self.assertEqual(item['post_url'], "https://example.com/good")
        self.assertEqual(item['external_link'], "http://external.com/good")

if __name__ == '__main__':
    unittest.main()
