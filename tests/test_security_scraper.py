import unittest
from bs4 import BeautifulSoup
from scraper import BlogScraper
import os

class TestSecurityScraper(unittest.TestCase):
    def setUp(self):
        self.mock_html_xss = """
        <html>
            <body>
                <article>
                    <header class="entry-header">
                        <h2 class="entry-title"><a href="javascript:alert(1)">Malicious Title</a></h2>
                    </header>
                    <div class="entry-content">
                        <a href="javascript:steal_cookies()">Click me</a>
                    </div>
                </article>
            </body>
        </html>
        """
        # Use a temporary DB and JSON file
        self.db_name = "test_security_wishlist.db"
        self.json_name = "test_security_wishlist.json"
        self.scraper = BlogScraper("http://mock.url", self.json_name, self.db_name)

    def tearDown(self):
        if os.path.exists(self.json_name):
            os.remove(self.json_name)
        if os.path.exists(self.db_name):
            os.remove(self.db_name)

    def test_xss_link_extraction(self):
        soup = BeautifulSoup(self.mock_html_xss, 'html.parser')
        article = soup.find('article')
        item = self.scraper.parse_article(article)

        # Verification: links should be None because they are javascript: scheme
        self.assertIsNone(item['post_url'], "Should reject javascript: post_url")
        self.assertIsNone(item['external_link'], "Should reject javascript: external_link")

    def test_valid_link_extraction(self):
        html = """
        <html>
            <body>
                <article>
                    <header class="entry-header">
                        <h2 class="entry-title"><a href="https://valid.com">Valid Title</a></h2>
                    </header>
                </article>
            </body>
        </html>
        """
        soup = BeautifulSoup(html, 'html.parser')
        article = soup.find('article')
        item = self.scraper.parse_article(article)
        self.assertEqual(item['post_url'], "https://valid.com")

if __name__ == '__main__':
    unittest.main()
