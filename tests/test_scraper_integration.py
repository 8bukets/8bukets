import unittest
import os
import sqlite3
import json
from unittest.mock import MagicMock, patch
from scraper import BlogScraper

SAMPLE_HTML = """
<html>
<body>
    <article>
        <header class="entry-header">
            <h2 class="entry-title"><a href="http://example.com/post1">Post 1</a></h2>
            <span class="cat-links"><a href="#">Category 1</a></span>
        </header>
        <div class="entry-content">
            <a href="http://external.com/1">External Link</a>
        </div>
        <div class="entry-meta">
            <span class="posted-on">
                <time datetime="2023-10-27T10:00:00+00:00">October 27, 2023</time>
            </span>
            <span class="byline">
                <span class="author"><a href="#">Bolt</a></span>
            </span>
        </div>
    </article>
    <div class="nav-previous">
        <!-- No next page -->
    </div>
</body>
</html>
"""

class TestScraperLogic(unittest.TestCase):
    def setUp(self):
        self.db_name = "test_wishlist.db"
        self.json_name = "test_wishlist.json"
        if os.path.exists(self.db_name):
            os.remove(self.db_name)
        if os.path.exists(self.json_name):
            os.remove(self.json_name)

    def tearDown(self):
        if os.path.exists(self.db_name):
            os.remove(self.db_name)
        if os.path.exists(self.json_name):
            os.remove(self.json_name)

    def test_scraper_flow(self):
        # Mock fetch_page to return our sample HTML once, then None
        scraper = BlogScraper("http://mock.url", self.json_name, self.db_name)

        # We need to mock fetch_page.
        # Since fetch_page is a method, we can mock it on the instance or patch it.
        # Patching is cleaner.

        with patch.object(scraper, 'fetch_page', side_effect=[SAMPLE_HTML.encode('utf-8'), None]):
            scraper.run()

        # Verify DB
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT title, post_url, external_link FROM posts")
        row = cursor.fetchone()
        conn.close()

        self.assertIsNotNone(row)
        self.assertEqual(row[0], "Post 1")
        self.assertEqual(row[1], "http://example.com/post1")
        self.assertEqual(row[2], "http://external.com/1")

        # Verify JSON
        self.assertTrue(os.path.exists(self.json_name))
        with open(self.json_name, 'r') as f:
            data = json.load(f)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]['title'], "Post 1")

if __name__ == "__main__":
    unittest.main()
