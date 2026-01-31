import unittest
from unittest.mock import MagicMock, patch
from scraper import BlogScraper
import os

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        self.base_url = "https://wishlist.design.blog"
        self.json_file = "test_sec.json"
        self.db_file = "test_sec.db"
        self.scraper = BlogScraper(self.base_url, self.json_file, self.db_file)

    def tearDown(self):
        if os.path.exists(self.json_file):
            os.remove(self.json_file)
        if os.path.exists(self.db_file):
            os.remove(self.db_file)

    def test_is_safe_url_implementation(self):
        """Test that is_safe_url correctly identifies safe and unsafe URLs."""
        if not hasattr(self.scraper, 'is_safe_url'):
             # If not implemented, we can't test it yet, but valid behavior is to fail or skip
             # failing is better to remind me to implement it.
             self.fail("is_safe_url not implemented")

        # Allowed domain
        self.assertTrue(self.scraper.is_safe_url("https://wishlist.design.blog/page/2"))
        self.assertTrue(self.scraper.is_safe_url("https://wishlist.design.blog/2023/01/01/post"))

        # Disallowed domains
        self.assertFalse(self.scraper.is_safe_url("https://evil.com/malware"))
        self.assertFalse(self.scraper.is_safe_url("http://google.com"))

        # Disallowed schemes
        self.assertFalse(self.scraper.is_safe_url("file:///etc/passwd"))
        self.assertFalse(self.scraper.is_safe_url("javascript:alert(1)"))
        self.assertFalse(self.scraper.is_safe_url("ftp://example.com"))

    @patch('scraper.requests.get')
    def test_run_stops_on_unsafe_link(self, mock_get):
        """Test that the scraper loop stops when encountering an unsafe link."""
        # 1. First response: Valid page with MALICIOUS next link
        mock_response_1 = MagicMock()
        mock_response_1.status_code = 200
        mock_response_1.content = b"""
        <html>
            <body>
                <div class="nav-previous"><a href="http://evil.com/exploit">Older posts</a></div>
                <article>
                    <header class="entry-header">
                        <h2 class="entry-title"><a href="http://wishlist.design.blog/post1">Post 1</a></h2>
                    </header>
                </article>
            </body>
        </html>
        """

        # 2. Second response: Empty (end of loop) - this would be returned if it fetches evil.com
        mock_response_2 = MagicMock()
        mock_response_2.status_code = 200
        mock_response_2.content = b"<html></html>"

        mock_get.side_effect = [mock_response_1, mock_response_2]

        # 3. Run scraper
        self.scraper.run()

        # 4. Verify behavior
        urls_called = [args[0] for args, kwargs in mock_get.call_args_list]

        # It SHOULD call base_url
        self.assertIn(self.base_url, urls_called)

        # It SHOULD NOT call evil.com
        self.assertNotIn("http://evil.com/exploit", urls_called)

        # Ensure it stopped (called only once)
        self.assertEqual(mock_get.call_count, 1)

    @patch('scraper.requests.get')
    def test_fetch_page_validates_url(self, mock_get):
        """Test that fetch_page itself validates the URL."""
        if not hasattr(self.scraper, 'is_safe_url'):
             return # Skip checking fetch_page integration if logic missing

        unsafe_url = "http://evil.com/exploit"
        content = self.scraper.fetch_page(unsafe_url)

        self.assertIsNone(content)
        mock_get.assert_not_called()

if __name__ == '__main__':
    unittest.main()
