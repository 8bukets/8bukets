import unittest
from scraper import BlogScraper

class TestSSRFProtection(unittest.TestCase):
    def test_safe_urls(self):
        safe_urls = [
            "https://google.com",
            "http://example.com",
            "https://www.wikipedia.org"
        ]
        for url in safe_urls:
            self.assertTrue(BlogScraper.is_safe_url(url), f"Should be safe: {url}")

    def test_unsafe_schemes(self):
        unsafe_urls = [
            "ftp://example.com",
            "file:///etc/passwd",
            "gopher://example.com",
            "javascript:alert(1)"
        ]
        for url in unsafe_urls:
            self.assertFalse(BlogScraper.is_safe_url(url), f"Should be unsafe scheme: {url}")

    def test_unsafe_hosts(self):
        unsafe_urls = [
            "http://localhost",
            "http://127.0.0.1",
            "http://0.0.0.0",
            "http://169.254.169.254", # AWS Metadata
            "http://10.0.0.1",       # Private range
            "http://192.168.1.1",    # Private range
            "http://[::1]"           # IPv6 Loopback
        ]
        for url in unsafe_urls:
            self.assertFalse(BlogScraper.is_safe_url(url), f"Should be unsafe host: {url}")

if __name__ == '__main__':
    unittest.main()
