import unittest
import asyncio
from scraper import OracleNewsScraper

class TestScraperSecurity(unittest.TestCase):
    def test_malicious_url_filtering(self):
        scraper = OracleNewsScraper("dummy.json", "dummy.csv", "dummy.txt")

        # HTML with valid and malicious links
        # All must contain '/news/announcement/' and 'google-cloud' to pass the initial filters
        html = """
        <html>
            <body>
                <a href="/news/announcement/valid-article-google-cloud"><h3>Valid Article</h3></a>
                <a href="javascript:alert(1);/news/announcement/google-cloud"><h3>Malicious JS Link</h3></a>
                <a href="data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==/news/announcement/google-cloud"><h3>Malicious Data Link</h3></a>
            </body>
        </html>
        """

        # We need to run the async method
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        articles = loop.run_until_complete(scraper.parse_page(html))
        loop.close()

        # Check results
        urls = [a['external_link'] for a in articles]

        # Verify valid link is present
        self.assertTrue(any("valid-article" in url for url in urls), f"Valid article should be present. Found: {urls}")

        # Verify malicious links are ABSENT
        # Currently, without the fix, these WILL be present, causing this test to fail
        javascript_links = [url for url in urls if url.startswith('javascript:')]
        data_links = [url for url in urls if url.startswith('data:')]

        self.assertEqual(len(javascript_links), 0, f"Found javascript links: {javascript_links}")
        self.assertEqual(len(data_links), 0, f"Found data links: {data_links}")

if __name__ == '__main__':
    unittest.main()
