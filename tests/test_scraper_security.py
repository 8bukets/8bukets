import unittest
from scraper import BlogScraper
import os

class TestBlogScraperSecurity(unittest.TestCase):
    def setUp(self):
        # Malicious HTML with javascript: links
        self.mock_html = """
        <html>
            <body>
                <article>
                    <header class="entry-header">
                        <h2 class="entry-title"><a href="javascript:alert(1)">Malicious Title</a></h2>
                    </header>
                    <div class="entry-content">
                        <a href="javascript:steal_cookies()">Malicious Link</a>
                        <a href="data:text/html,<script>alert(1)</script>">Data Link</a>
                    </div>
                </article>
            </body>
        </html>
        """
        self.db_name = "test_security.db"
        self.json_name = "test_security.json"
        self.scraper = BlogScraper("http://mock.url", self.json_name, self.db_name)

    def tearDown(self):
        if os.path.exists(self.db_name):
            os.remove(self.db_name)
        if os.path.exists(self.json_name):
            os.remove(self.json_name)

    def test_parse_article_xss_prevention(self):
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(self.mock_html, 'html.parser')
        article = soup.find('article')
        item = self.scraper.parse_article(article)

        # We expect the malicious links to be filtered (None or empty)
        # But currently they are extracted as is.
        # This test asserts that they ARE filtered, so it should fail initially.

        # Check post_url
        self.assertNotEqual(item['post_url'], "javascript:alert(1)", "XSS vector in post_url detected")
        self.assertIsNone(item['post_url'], "post_url should be None for non-http schemes")

        # Check external_link
        self.assertNotEqual(item['external_link'], "javascript:steal_cookies()", "XSS vector in external_link detected")
        self.assertIsNone(item['external_link'], "external_link should be None for non-http schemes")

if __name__ == '__main__':
    unittest.main()
