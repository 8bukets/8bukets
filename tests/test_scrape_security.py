import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from unittest.mock import MagicMock, patch
from scrape_informatic import scrape, BASE_URL
import logging

# Disable logging during tests to keep output clean
logging.disable(logging.CRITICAL)

class TestScraperSecurity(unittest.TestCase):
    @patch('scrape_informatic.get_session')
    def test_pagination_ssrf_prevention(self, mock_get_session):
        # Setup mock session and response
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_get_session.return_value = mock_session
        mock_session.get.return_value = mock_response

        # HTML with a malicious pagination link
        # The scraper looks for 'div.nav-previous > a'
        html_content = """
        <html>
            <body>
                <article>
                    <h2 class="entry-title"><a href="post1">Title</a></h2>
                    <div class="entry-content">Content</div>
                </article>
                <div class="nav-previous">
                    <a href="http://malicious-site.com/exploit">Older posts</a>
                </div>
            </body>
        </html>
        """
        mock_response.content = html_content.encode('utf-8')
        mock_response.status_code = 200

        # Run scrape for 2 pages.
        # If vulnerable, it will try to visit the malicious URL in the second iteration.
        scrape("test_output.json", max_pages=2)

        # Get all URLs visited
        visited_urls = [call[0][0] for call in mock_session.get.call_args_list]
        print(f"\nURLs visited: {visited_urls}")

        # Check if malicious URL was visited
        if "http://malicious-site.com/exploit" in visited_urls:
             self.fail("Security Vulnerability: Scraper visited a malicious external URL via pagination!")

        # It should at least visit the BASE_URL
        self.assertIn(BASE_URL, visited_urls)

if __name__ == '__main__':
    unittest.main()
