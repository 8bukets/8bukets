import unittest
from unittest.mock import MagicMock, patch, mock_open
import scrape_informatic
import os

class TestScraperSecurity(unittest.TestCase):

    @patch('scrape_informatic.get_session')
    @patch('builtins.open', new_callable=mock_open)
    @patch('scrape_informatic.json.dump')
    def test_domain_restriction(self, mock_json_dump, mock_file_open, mock_get_session):
        """
        Test that the scraper does not follow links to external domains.
        """
        # Setup mock session
        mock_session = MagicMock()
        mock_get_session.return_value = mock_session

        # HTML with a link to evil.com
        html_content = """
        <html>
            <body>
                <div class="nav-previous">
                    <a href="http://evil.com/page2">Old Posts</a>
                </div>
            </body>
        </html>
        """

        # Configure mock response for the first call (valid)
        mock_response = MagicMock()
        mock_response.content = html_content.encode('utf-8')
        mock_response.status_code = 200

        # Mock response for evil.com (if it gets called)
        mock_evil_response = MagicMock()
        mock_evil_response.content = b"<html><body>Evil Content</body></html>"
        mock_evil_response.status_code = 200

        # Side effect: First call returns valid page, subsequent calls return evil page
        mock_session.get.side_effect = [mock_response, mock_evil_response]

        # Run scrape (limit 2 pages to trigger the loop if it follows the link)
        # Pass a dummy file name
        scrape_informatic.scrape("dummy_output.json", max_pages=2)

        # Verify calls
        called_urls = [args[0] for args, kwargs in mock_session.get.call_args_list]

        print(f"\nCalled URLs: {called_urls}")

        # It should always call the BASE_URL first
        self.assertIn("https://informaticmagazine.data.blog", called_urls)

        # It should NOT call evil.com
        self.assertNotIn("http://evil.com/page2", called_urls, "Security Vulnerability: Scraper followed link to external domain!")

    @patch('scrape_informatic.get_session')
    @patch('builtins.open', new_callable=mock_open)
    @patch('scrape_informatic.json.dump')
    def test_timeout_enforcement(self, mock_json_dump, mock_file_open, mock_get_session):
        """
        Test that the scraper uses a timeout for network requests.
        """
        mock_session = MagicMock()
        mock_get_session.return_value = mock_session

        mock_response = MagicMock()
        mock_response.content = b"<html></html>"
        mock_response.status_code = 200
        mock_session.get.return_value = mock_response

        scrape_informatic.scrape("dummy_output.json", max_pages=1)

        # Check that timeout was passed
        # We check the first call
        args, kwargs = mock_session.get.call_args
        self.assertIn('timeout', kwargs, "Security Vulnerability: Request made without timeout!")
        self.assertEqual(kwargs['timeout'], 10, "Timeout should be set to 10 seconds")

if __name__ == '__main__':
    unittest.main()
