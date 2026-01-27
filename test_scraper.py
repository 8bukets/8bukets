import unittest
from unittest.mock import patch
from scraper import OracleNewsScraper
import os

class TestOracleNewsScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = OracleNewsScraper("test_output.json", "test_output.csv", "test_output.txt")
        # Minimal HTML structure that mimics what scraper expects
        self.html = """
        <html>
        <body>
        <!--
        rc92v0
        <section>
          <ul>
            <li class="rc92w3">
              <div class="rc92-dt">Oct 15, 2025</div>
              <h5><a href="/news/test-article">Test Article Title</a></h5>
            </li>
          </ul>
        </section>
        -->
        </body>
        </html>
        """

    def test_parse_page(self):
        posts = self.scraper.parse_page(self.html)
        self.assertEqual(len(posts), 1, "Should extract exactly 1 post")

        post = posts[0]
        self.assertEqual(post['title'], "Test Article Title")
        self.assertEqual(post['date'], "Oct 15, 2025")
        self.assertEqual(post['external_link'], "https://www.oracle.com/news/test-article")

    def test_parse_page_fallback(self):
        # Mock re.finditer to return empty so we force fallback to BeautifulSoup
        with patch('re.finditer') as mock_finditer:
            mock_finditer.return_value = []

            # This should still work because BS4 fallback will find the comment
            comment = self.scraper._extract_news_comment(self.html)
            self.assertIsNotNone(comment)
            self.assertIn("rc92v0", comment)
            self.assertIn("<section", comment)

if __name__ == '__main__':
    unittest.main()
