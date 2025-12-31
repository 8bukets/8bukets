import unittest
from unittest.mock import patch, MagicMock
from bs4 import BeautifulSoup, SoupStrainer
import sys
import os

# Add root directory to path to import scrape_informatic
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scrape_informatic import scrape

class TestScraper(unittest.TestCase):
    @patch('scrape_informatic.requests.Session')
    def test_scrape_logic(self, mock_session_cls):
        # Mock HTML content
        html_content = """
        <html>
            <body>
                <div class="site-content">
                    <article class="post">
                        <header class="entry-header">
                            <h2 class="entry-title"><a href="http://example.com/post1">Post 1</a></h2>
                        </header>
                        <div class="entry-content">Content 1</div>
                        <time class="entry-date" datetime="2023-01-01">Jan 1, 2023</time>
                    </article>
                    <article class="post">
                        <header class="entry-header">
                            <h2 class="entry-title"><a href="http://example.com/post2">Post 2</a></h2>
                        </header>
                        <div class="entry-content">Content 2</div>
                        <time class="entry-date" datetime="2023-01-02">Jan 2, 2023</time>
                    </article>
                    <div class="nav-previous">
                        <a href="http://example.com/page/2">Older posts</a>
                    </div>
                </div>
            </body>
        </html>
        """

        # Mock second page (no pagination)
        html_content_page2 = """
        <html>
            <body>
                <article class="post">
                    <h2 class="entry-title"><a href="http://example.com/post3">Post 3</a></h2>
                </article>
            </body>
        </html>
        """

        # Mock response
        mock_response_page1 = MagicMock()
        mock_response_page1.content = html_content.encode('utf-8')
        mock_response_page1.status_code = 200

        mock_response_page2 = MagicMock()
        mock_response_page2.content = html_content_page2.encode('utf-8')
        mock_response_page2.status_code = 200

        # Mock session instance
        mock_session = mock_session_cls.return_value
        mock_session.get.side_effect = [mock_response_page1, mock_response_page2]

        # Run scrape with mocked session
        output_file = "tests/test_output.json"
        try:
            scrape(output_file, max_pages=2)

            # Verify calls
            self.assertEqual(mock_session.get.call_count, 2)

            # Verify file content
            import json
            with open(output_file, 'r') as f:
                data = json.load(f)
                self.assertEqual(len(data), 3) # 2 from page 1, 1 from page 2
                self.assertEqual(data[0]['title'], "Post 1")
                self.assertEqual(data[1]['title'], "Post 2")
                self.assertEqual(data[2]['title'], "Post 3")
        finally:
            if os.path.exists(output_file):
                os.remove(output_file)

if __name__ == '__main__':
    unittest.main()
