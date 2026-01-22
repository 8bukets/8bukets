import unittest
from unittest.mock import MagicMock, patch
import json
import os
import sqlite3
from scraper import BlogScraper

class TestBlogScraper(unittest.TestCase):
    def setUp(self):
        self.mock_html = """
        <html>
            <body>
                <article>
                    <header class="entry-header">
                        <h2 class="entry-title"><a href="http://example.com/post1">Test Title</a></h2>
                        <span class="cat-links"><a href="#">Category1</a></span>
                    </header>
                    <div class="entry-content">
                        <a href="https://external.com">Link</a>
                    </div>
                    <div class="entry-meta">
                        <span class="posted-on"><time datetime="2023-01-01">January 1, 2023</time></span>
                        <span class="byline"><span class="author"><a href="#">Author Name</a></span></span>
                    </div>
                </article>
            </body>
        </html>
        """
        self.db_name = "test_wishlist.db"
        self.json_name = "test_wishlist.json"
        self.scraper = BlogScraper("http://mock.url", self.json_name, self.db_name)

    def tearDown(self):
        self.scraper.close()
        if os.path.exists(self.db_name):
            os.remove(self.db_name)
        if os.path.exists(self.json_name):
            os.remove(self.json_name)

    def test_fetch_page(self):
        # We need to mock session.get on the instance
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = self.mock_html.encode('utf-8')

        with patch.object(self.scraper.session, 'get', return_value=mock_response) as mock_get:
            content = self.scraper.fetch_page("http://mock.url")
            self.assertIsNotNone(content)
            self.assertIn(b"Test Title", content)

    def test_parse_article(self):
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(self.mock_html, 'html.parser')
        article = soup.find('article')
        item = self.scraper.parse_article(article)

        self.assertEqual(item['title'], "Test Title")
        self.assertEqual(item['post_url'], "http://example.com/post1")
        self.assertEqual(item['external_link'], "https://external.com")
        self.assertEqual(item['date'], "January 1, 2023")
        self.assertEqual(item['datetime'], "2023-01-01")
        self.assertEqual(item['author'], "Author Name")
        self.assertEqual(item['categories'], ["Category1"])

    def test_database_insertion(self):
        item = {
            'title': 'DB Test',
            'post_url': 'http://example.com/unique-post-1',
            'external_link': 'https://dbtest.com',
            'date': '2023-01-01',
            'datetime': '2023-01-01',
            'author': 'Tester',
            'categories': ['Test']
        }

        # First insertion should succeed
        success = self.scraper.save_to_db(item)
        self.assertTrue(success)

        # Duplicate insertion (by post_url) should fail/ignore
        success = self.scraper.save_to_db(item)
        self.assertFalse(success)

        # Manually commit to verify with another connection
        self.scraper.conn.commit()

        # Verify data in DB
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM posts WHERE post_url=?", ('http://example.com/unique-post-1',))
            row = cursor.fetchone()
            self.assertIsNotNone(row)
            self.assertEqual(row[1], 'DB Test') # title

if __name__ == '__main__':
    unittest.main()
