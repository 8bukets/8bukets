import unittest
from bs4 import BeautifulSoup
from scraper import BlogScraper

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        self.scraper = BlogScraper("http://mock.url", "test_json.json", "test_db.db")

    def test_malicious_javascript_link(self):
        # Simulator a page with a javascript: link which is an XSS vector if not sanitized
        html = """
        <article>
            <header class="entry-header">
                <h2 class="entry-title"><a href="javascript:alert(1)">Malicious Title</a></h2>
            </header>
            <div class="entry-content">
                <a href="javascript:alert('XSS')">Click me</a>
            </div>
        </article>
        """
        soup = BeautifulSoup(html, 'html.parser')
        article = soup.find('article')
        item = self.scraper.parse_article(article)

        # After the fix, these should be None because they don't start with http/https
        self.assertIsNone(item['post_url'], "Malicious Javascript URL should be filtered out")
        self.assertIsNone(item['external_link'], "Malicious Javascript External Link should be filtered out")

    def test_valid_http_link(self):
        html = """
        <article>
            <header class="entry-header">
                <h2 class="entry-title"><a href="http://good.com">Good Title</a></h2>
            </header>
            <div class="entry-content">
                <a href="https://secure.com">Secure Link</a>
            </div>
        </article>
        """
        soup = BeautifulSoup(html, 'html.parser')
        article = soup.find('article')
        item = self.scraper.parse_article(article)

        self.assertEqual(item['post_url'], "http://good.com")
        self.assertEqual(item['external_link'], "https://secure.com")

if __name__ == '__main__':
    unittest.main()
