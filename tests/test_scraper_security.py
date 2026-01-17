import unittest
from unittest.mock import MagicMock, patch
import sys
import os

# Add root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scrape_informatic import scrape

class TestScraperSecurity(unittest.TestCase):
    @patch('scrape_informatic.get_session')
    def test_ssrf_protection(self, mock_get_session):
        # Setup the mock session
        mock_session = MagicMock()
        mock_get_session.return_value = mock_session

        # Mock responses
        # Response 1: Valid page with a malicious "next page" link
        response1 = MagicMock()
        response1.status_code = 200
        response1.content = b"""
        <html>
            <body>
                <article>
                    <h2 class="entry-title"><a href="https://example.com/p1">Post 1</a></h2>
                    <time class="entry-date" datetime="2023-01-01">Jan 1, 2023</time>
                    <div class="entry-content">Content</div>
                </article>
                <div class="nav-previous"><a href="http://localhost:8080/admin">Next</a></div>
            </body>
        </html>
        """

        # Response 2: The malicious page (should NOT be fetched if fixed)
        response2 = MagicMock()
        response2.status_code = 200
        response2.content = b"<html><body>Admin Page</body></html>"

        # Set side_effect for session.get
        # The loop might continue if we don't handle it, so let's provide enough responses or stop it.
        # If it calls the second one, it will get response2.
        # If it tries to go further, we can raise an error or return None.
        mock_session.get.side_effect = [response1, response2, Exception("Stop")]

        # Run scrape
        # We limit to 2 pages so it tries to fetch the next one
        try:
            scrape("test_output.json", max_pages=2)
        except Exception:
            pass

        # Check what was called
        calls = mock_session.get.call_args_list
        urls_fetched = [c[0][0] for c in calls]
        print(f"URLs fetched: {urls_fetched}")

        # Verify initial call is correct
        self.assertIn("https://informaticmagazine.data.blog", urls_fetched[0])

        # Verify subsequent calls do NOT include localhost
        # The test asserts that NO call was made to localhost
        for url in urls_fetched:
            if "localhost" in url or "127.0.0.1" in url:
                self.fail(f"SSRF Vulnerability detected! Scraper attempted to fetch: {url}")

    def tearDown(self):
        if os.path.exists("test_output.json"):
            os.remove("test_output.json")

if __name__ == '__main__':
    unittest.main()
