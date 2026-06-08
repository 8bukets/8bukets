import unittest
import sys
import os
import asyncio
import json
from unittest.mock import MagicMock, AsyncMock, patch

# Add root directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scraper import MarkPositionScraperAsync

class TestScraperRegression(unittest.TestCase):
    def setUp(self):
        self.scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")
        self.html = """
        <html>
        <body>
            <article class="post">
                <header class="entry-header">
                    <h1 class="entry-title"><a href="https://markposition.wordpress.com/2023/01/01/post1/">Test Post 1</a></h1>
                </header>
                <div class="entry-content">
                    <p>Some content <a href="https://external.com/1">External Link 1</a></p>
                </div>
                <footer class="entry-meta">
                    <span class="cat-links">
                        <a href="#" rel="category tag">Uncategorized</a>
                    </span>
                    <time class="entry-date" datetime="2023-01-01T12:00:00+00:00">January 1, 2023</time>
                    <span class="author vcard"><a class="url fn n" href="#">Test Author</a></span>
                </footer>
            </article>
            <article class="post">
                 <h1 class="entry-title"><a href="https://markposition.wordpress.com/2023/01/02/post2/">Test Post 2</a></h1>
            </article>
            <article class="not-a-post">
                Should be ignored
            </article>
        </body>
        </html>
        """

    def test_parse_page(self):
        # Check if parse_page returns list directly (sync)
        results = self.scraper.parse_page(self.html)

        self.assertTrue(len(results) > 0, "Should find posts")
        self.assertEqual(len(results), 2, f"Expected 2 posts, got {len(results)}")

        first_post = results[0]
        self.assertEqual(first_post['title'], "Test Post 1")
        self.assertEqual(first_post['author'], "Test Author")
        self.assertEqual(first_post['external_link'], "https://external.com/1")

    def test_fetch_and_parse(self):
        # Mock session and semaphore
        mock_session = AsyncMock()
        mock_sem = asyncio.Semaphore(1)

        # Mock fetch_page to return our sample html
        # Since fetch_page is an instance method, we can patch it on the instance
        self.scraper.fetch_page = AsyncMock(return_value=self.html)

        # Run fetch_and_parse
        result = asyncio.run(self.scraper.fetch_and_parse(mock_session, 1, mock_sem))

        self.assertIsNotNone(result)
        self.assertEqual(len(result), 2)

        # Verify fetch_page was called
        self.scraper.fetch_page.assert_called_once()

if __name__ == '__main__':
    unittest.main()
