import sys
import os
import unittest

# Add root directory to python path to import scrape_informatic
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scrape_informatic import is_safe_url
from urllib.parse import urljoin

class TestScraperSecurity(unittest.TestCase):

    def setUp(self):
        self.base_url = "https://informaticmagazine.data.blog"

    def test_safe_internal_url(self):
        url = "https://informaticmagazine.data.blog/page/2"
        self.assertTrue(is_safe_url(url, self.base_url))

    def test_safe_relative_resolution(self):
        current_url = "https://informaticmagazine.data.blog/page/1"
        href = "/page/2"
        resolved = urljoin(current_url, href)
        self.assertTrue(is_safe_url(resolved, self.base_url))

    def test_unsafe_external_domain(self):
        url = "https://malicious.com/hack"
        self.assertFalse(is_safe_url(url, self.base_url))

    def test_unsafe_subdomain(self):
        # Strict matching check - usually we want same netloc
        url = "https://evil.informaticmagazine.data.blog"
        self.assertFalse(is_safe_url(url, self.base_url))

    def test_unsafe_scheme(self):
        url = "ftp://informaticmagazine.data.blog/file"
        self.assertFalse(is_safe_url(url, self.base_url))

    def test_unsafe_javascript(self):
        url = "javascript:alert(1)"
        self.assertFalse(is_safe_url(url, self.base_url))

    def test_unsafe_data(self):
        url = "data:text/html,<script>alert(1)</script>"
        self.assertFalse(is_safe_url(url, self.base_url))

    def test_none_input(self):
        self.assertFalse(is_safe_url(None, self.base_url))

if __name__ == '__main__':
    unittest.main()
