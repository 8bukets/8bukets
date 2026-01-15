import unittest
import sys
import os

# Add parent directory to path so we can import scrape_informatic
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scrape_informatic import is_external_link

# Import the function we are about to add (or check if it exists)
try:
    from scrape_informatic import is_safe_pagination_url
except ImportError:
    is_safe_pagination_url = None

class TestSecurityUtils(unittest.TestCase):
    BASE_URL = "https://informaticmagazine.data.blog"

    def test_is_external_link(self):
        # Should be True for different domain
        self.assertTrue(is_external_link("http://google.com", self.BASE_URL))
        self.assertTrue(is_external_link("https://evil.com/page", self.BASE_URL))

        # Should be False for same domain
        self.assertFalse(is_external_link("https://informaticmagazine.data.blog/page/2", self.BASE_URL))
        self.assertFalse(is_external_link("https://informaticmagazine.data.blog", self.BASE_URL))

        # Should be False for relative link
        self.assertFalse(is_external_link("/page/2", self.BASE_URL))
        self.assertFalse(is_external_link("page/2", self.BASE_URL))

    def test_is_safe_pagination_url(self):
        if is_safe_pagination_url is None:
            print("\nis_safe_pagination_url is missing (Expected)")
            self.fail("is_safe_pagination_url not implemented yet")
            return

        # Valid internal scenarios
        self.assertTrue(is_safe_pagination_url("https://informaticmagazine.data.blog/page/2", self.BASE_URL), "Absolute same domain should be safe")
        self.assertTrue(is_safe_pagination_url("/page/2", self.BASE_URL), "Relative path should be safe")
        self.assertTrue(is_safe_pagination_url("?page=2", self.BASE_URL), "Query only should be safe")

        # Invalid external scenarios (SSRF risk)
        self.assertFalse(is_safe_pagination_url("http://evil.com", self.BASE_URL), "External http should be unsafe")
        self.assertFalse(is_safe_pagination_url("https://google.com", self.BASE_URL), "External https should be unsafe")
        self.assertFalse(is_safe_pagination_url("//evil.com", self.BASE_URL), "Protocol relative URL to external should be unsafe")

        # Malicious schemes
        self.assertFalse(is_safe_pagination_url("javascript:alert(1)", self.BASE_URL), "Javascript scheme should be unsafe")
        self.assertFalse(is_safe_pagination_url("file:///etc/passwd", self.BASE_URL), "File scheme should be unsafe")
        self.assertFalse(is_safe_pagination_url("data:text/html,<body>", self.BASE_URL), "Data scheme should be unsafe")

        # Mixed case schemes
        self.assertFalse(is_safe_pagination_url("JaVaScRiPt:alert(1)", self.BASE_URL), "Mixed case javascript scheme should be unsafe")

if __name__ == '__main__':
    unittest.main()
