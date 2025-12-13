import unittest
from unittest.mock import MagicMock, patch
from scraper import MalubeachScraper

class TestMalubeachScraper(unittest.TestCase):

    def setUp(self):
        self.scraper = MalubeachScraper()

    def test_is_external_link(self):
        self.assertTrue(self.scraper.is_external_link('https://google.com'))
        self.assertTrue(self.scraper.is_external_link('http://example.com/page'))
        self.assertFalse(self.scraper.is_external_link('https://malubeach.wordpress.com/2021/01/01/post'))
        self.assertFalse(self.scraper.is_external_link('/relative/path'))
        self.assertFalse(self.scraper.is_external_link('#anchor'))

    def test_parse_page(self):
        html_content = """
        <html>
            <body>
                <article>
                    <h2 class="entry-title">Test Post</h2>
                    <time class="entry-date published">January 1, 2023</time>
                    <div class="entry-content">
                        <p>Some text</p>
                        <a href="https://external.com">External Link</a>
                        <a href="https://malubeach.wordpress.com/internal">Internal Link</a>
                    </div>
                </article>
                <div class="nav-previous">
                    <a href="https://malubeach.wordpress.com/page/2/">Older posts</a>
                </div>
            </body>
        </html>
        """
        data, next_url = self.scraper.parse_page(html_content)

        # Check extracted data
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['title'], 'Test Post')
        self.assertEqual(data[0]['date'], 'January 1, 2023')
        self.assertEqual(data[0]['link'], 'https://external.com')

        # Check next URL
        self.assertEqual(next_url, 'https://malubeach.wordpress.com/page/2/')

    def test_parse_page_no_external_links(self):
        html_content = """
        <html>
            <body>
                <article>
                    <h2 class="entry-title">Test Post</h2>
                    <time class="entry-date published">January 1, 2023</time>
                    <div class="entry-content">
                        <p>Just text</p>
                        <a href="https://malubeach.wordpress.com/internal">Internal Link</a>
                    </div>
                </article>
            </body>
        </html>
        """
        data, next_url = self.scraper.parse_page(html_content)
        self.assertEqual(len(data), 0)
        self.assertIsNone(next_url)

    def test_parse_page_multiple_external_links(self):
        html_content = """
        <html>
            <body>
                <article>
                    <h2 class="entry-title">Test Post</h2>
                    <time class="entry-date published">January 1, 2023</time>
                    <div class="entry-content">
                        <a href="https://link1.com">Link 1</a>
                        <a href="https://link2.com">Link 2</a>
                    </div>
                </article>
            </body>
        </html>
        """
        data, next_url = self.scraper.parse_page(html_content)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['link'], 'https://link1.com')
        self.assertEqual(data[1]['link'], 'https://link2.com')

    @patch('requests.Session.get')
    def test_fetch_page_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "<html></html>"
        mock_get.return_value = mock_response

        content = self.scraper.fetch_page('http://test.com')
        self.assertEqual(content, "<html></html>")

    @patch('requests.Session.get')
    def test_fetch_page_failure(self, mock_get):
        mock_get.side_effect = Exception("Connection Error")

        content = self.scraper.fetch_page('http://test.com')
        self.assertIsNone(content)

if __name__ == '__main__':
    unittest.main()
