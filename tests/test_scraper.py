import unittest
from urllib.parse import urlparse
import sys
import os

# Add root to path to import scrape_informatic
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scrape_informatic import is_external_link, BASE_URL

class TestScraper(unittest.TestCase):
    def test_is_external_link(self):
        base_url = "https://informaticmagazine.data.blog"
        base_netloc = urlparse(base_url).netloc

        # Internal links
        self.assertFalse(is_external_link("https://informaticmagazine.data.blog/some-post", base_netloc))
        self.assertFalse(is_external_link("/relative-path", base_netloc))
        self.assertFalse(is_external_link("#fragment", base_netloc))
        self.assertFalse(is_external_link("", base_netloc))
        self.assertFalse(is_external_link(None, base_netloc))

        # External links
        self.assertTrue(is_external_link("https://google.com", base_netloc))
        self.assertTrue(is_external_link("http://other.blog.com", base_netloc))
        self.assertTrue(is_external_link("https://informaticmagazine.data.blog.evil.com", base_netloc))

if __name__ == '__main__':
    unittest.main()
