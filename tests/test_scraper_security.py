import unittest
import sys
import os

# Add parent directory to path to import scrape_informatic
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestScraperSecurity(unittest.TestCase):
    def test_is_safe_url(self):
        try:
            from scrape_informatic import is_safe_url
        except ImportError:
            self.fail("Could not import is_safe_url from scrape_informatic")

        base_url = "https://informaticmagazine.data.blog"

        # Safe cases
        self.assertTrue(is_safe_url("https://informaticmagazine.data.blog/2023/01/01/post", base_url), "Should allow same domain")
        self.assertTrue(is_safe_url("https://informaticmagazine.data.blog/page/2", base_url), "Should allow same domain pagination")

        # Unsafe cases - Different domain
        self.assertFalse(is_safe_url("https://google.com", base_url), "Should block google.com")
        self.assertFalse(is_safe_url("http://malicious.com", base_url), "Should block malicious.com")

        # Unsafe cases - Subdomain mismatch (strict check)
        self.assertFalse(is_safe_url("https://other.data.blog", base_url), "Should block other subdomains")

        # Unsafe cases - Protocol
        self.assertFalse(is_safe_url("file:///etc/passwd", base_url), "Should block file protocol")
        self.assertFalse(is_safe_url("ftp://informaticmagazine.data.blog", base_url), "Should block ftp protocol")

        # Unsafe cases - Localhost/Private IP
        self.assertFalse(is_safe_url("http://localhost:8000", base_url), "Should block localhost")
        self.assertFalse(is_safe_url("http://127.0.0.1", base_url), "Should block 127.0.0.1")
        self.assertFalse(is_safe_url("http://169.254.169.254", base_url), "Should block metadata IP")

if __name__ == '__main__':
    unittest.main()
