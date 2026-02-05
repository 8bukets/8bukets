import unittest
from unittest.mock import MagicMock, patch
import scrape_informatic
from bs4 import BeautifulSoup
import logging

# Disable logging during test
logging.disable(logging.CRITICAL)

class TestScraperSecurity(unittest.TestCase):
    @patch('scrape_informatic.requests.Session')
    def test_pagination_ssrf(self, mock_session_cls):
        # Setup mock
        mock_session = mock_session_cls.return_value

        # Page 1 response: Contains a malicious next page link
        html_content = """
        <html>
            <body>
                <article class="post">
                    <h2 class="entry-title"><a href="http://example.com/post1">Post 1</a></h2>
                </article>
                <div class="nav-previous">
                    <a href="http://localhost:8080/admin">Next Page</a>
                </div>
            </body>
        </html>
        """
        response_1 = MagicMock()
        response_1.content = html_content.encode('utf-8')
        response_1.status_code = 200

        # Page 2 response (Malicious): Should NOT be fetched
        response_2 = MagicMock()
        response_2.content = b"Secret Admin Page"
        response_2.status_code = 200

        # Side effect for get:
        # First call: BASE_URL -> returns html_content
        # Second call: http://localhost:8080/admin -> returns response_2
        def side_effect(url, **kwargs):
            if "informaticmagazine.data.blog" in url:
                return response_1
            elif "localhost" in url:
                return response_2
            return MagicMock(status_code=404)

        mock_session.get.side_effect = side_effect

        # Run scrape
        # We do not catch exceptions here to ensure any runtime errors (e.g. NameError) fail the test.
        scrape_informatic.scrape("test_output.json", max_pages=2)

        # Verify
        # Check if fetch for malicious URL happened
        calls = [call.args[0] for call in mock_session.get.call_args_list]

        malicious_called = any("localhost:8080/admin" in str(c) for c in calls)

        if malicious_called:
            print("VULNERABILITY CONFIRMED: Scraper fetched external/internal URL.")
        else:
            print("SECURE: Scraper did not fetch external/internal URL.")

        self.assertFalse(malicious_called, "The scraper should NOT fetch external/internal URLs from pagination.")

if __name__ == '__main__':
    unittest.main()
