import unittest
from unittest.mock import MagicMock, patch
import json
import os
import sqlite3
import socket
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
        if os.path.exists(self.db_name):
            os.remove(self.db_name)
        if os.path.exists(self.json_name):
            os.remove(self.json_name)

    @patch('scraper.socket.getaddrinfo')
    @patch('requests.get')
    def test_fetch_page(self, mock_get, mock_getaddrinfo):
        # Mock DNS resolution to a public IP (e.g., 93.184.216.34)
        mock_getaddrinfo.return_value = [(socket.AF_INET, socket.SOCK_STREAM, 6, '', ('93.184.216.34', 80))]

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = self.mock_html.encode('utf-8')
        mock_get.return_value = mock_response

        content = self.scraper.fetch_page("http://mock.url")
        self.assertIsNotNone(content)
        self.assertIn(b"Test Title", content)

    @patch('scraper.socket.getaddrinfo')
    def test_fetch_page_ssrf(self, mock_getaddrinfo):
        # Mock DNS resolution to a private IP (e.g., 127.0.0.1)
        mock_getaddrinfo.return_value = [(socket.AF_INET, socket.SOCK_STREAM, 6, '', ('127.0.0.1', 80))]

        content = self.scraper.fetch_page("http://localhost")
        self.assertIsNone(content)

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

        # Verify data in DB
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM posts WHERE post_url=?", ('http://example.com/unique-post-1',))
            row = cursor.fetchone()
            self.assertIsNotNone(row)
            self.assertEqual(row[1], 'DB Test') # title

if __name__ == '__main__':
    unittest.main()
