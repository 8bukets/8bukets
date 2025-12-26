import asyncio
import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scraper import MarkPositionScraperAsync

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        self.scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")

    def test_javascript_link_exclusion(self):
        """Ensure javascript: links are not extracted as external links."""
        html = """
        <article class="post">
            <h1 class="entry-title"><a href="http://example.com/post">Safe Title</a></h1>
            <div class="entry-content">
                <a href="javascript:alert('XSS')">Click me</a>
            </div>
        </article>
        """

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        posts = loop.run_until_complete(self.scraper.parse_page(html))
        loop.close()

        self.assertEqual(len(posts), 1)
        # It should be None or ignored, definitely not javascript:
        self.assertNotEqual(posts[0].get('external_link'), "javascript:alert('XSS')")
        self.assertIsNone(posts[0].get('external_link'))

    def test_csv_injection_sanitization(self):
        """Ensure sanitize_for_csv escapes dangerous characters."""
        dangerous_inputs = ["=1+1", "+1+1", "-1+1", "@1+1", "%1+1"]
        for inp in dangerous_inputs:
            sanitized = self.scraper.sanitize_for_csv(inp)
            self.assertTrue(sanitized.startswith("'"), f"Failed to sanitize {inp}")
            self.assertEqual(sanitized, "'" + inp)

    def test_valid_http_link_extraction(self):
        """Ensure valid http/https links are extracted."""
        html = """
        <article class="post">
            <h1 class="entry-title"><a href="http://example.com/post">Safe Title</a></h1>
            <div class="entry-content">
                <a href="https://example.com/external">External Link</a>
            </div>
        </article>
        """
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        posts = loop.run_until_complete(self.scraper.parse_page(html))
        loop.close()

        self.assertEqual(posts[0].get('external_link'), "https://example.com/external")

    def test_post_url_sanitization(self):
        """Ensure post_url is also sanitized if it contains dangerous schemes."""
        html = """
        <article class="post">
            <h1 class="entry-title"><a href="javascript:alert(1)">Unsafe Title Link</a></h1>
        </article>
        """
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        posts = loop.run_until_complete(self.scraper.parse_page(html))
        loop.close()

        # Should be None or ignored
        self.assertNotEqual(posts[0].get('post_url'), "javascript:alert(1)")
        self.assertIsNone(posts[0].get('post_url'))

if __name__ == '__main__':
    unittest.main()
