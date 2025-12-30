
import unittest
from unittest.mock import MagicMock, patch
import sys
import os

# Add root directory to sys.path to import scrape_informatic
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import scrape_informatic
from scrape_informatic import scrape, parse_post_html

class TestScrapeInformatic(unittest.TestCase):

    def setUp(self):
        self.mock_html = """
        <html>
            <body>
                <main id="main" class="site-main">
                    <article>
                        <header class="entry-header">
                            <h2 class="entry-title"><a href="http://example.com/post1">Post 1</a></h2>
                        </header>
                        <div class="entry-content">
                            <p>Content 1</p>
                        </div>
                    </article>
                    <div class="nav-previous"><a href="http://example.com/page2">Next Page</a></div>
                </main>
            </body>
        </html>
        """

    @patch('scrape_informatic.get_session')
    @patch('scrape_informatic.time.sleep') # Skip sleep
    @patch('builtins.open', new_callable=unittest.mock.mock_open) # Mock file opening
    def test_scrape_pagination(self, mock_file, mock_sleep, mock_get_session):
        mock_session = MagicMock()
        mock_response_page1 = MagicMock()
        mock_response_page1.content = self.mock_html.encode('utf-8')
        mock_response_page1.status_code = 200

        mock_response_page2 = MagicMock()
        mock_response_page2.content = "<html><body><main></main></body></html>".encode('utf-8') # No articles, no pagination
        mock_response_page2.status_code = 200

        mock_session.get.side_effect = [mock_response_page1, mock_response_page2]
        mock_get_session.return_value = mock_session

        scrape("test_output.json", max_pages=2)

        # Check calls
        self.assertEqual(mock_session.get.call_count, 2)
        # Verify timeout was passed
        mock_session.get.assert_any_call("https://informaticmagazine.data.blog", timeout=10)
        mock_session.get.assert_any_call("http://example.com/page2", timeout=10)

        # Verify file write was attempted
        mock_file.assert_called_with("test_output.json", 'w', encoding='utf-8')

if __name__ == '__main__':
    unittest.main()
