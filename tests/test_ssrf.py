import unittest
from unittest.mock import patch
from scraper import BlogScraper

class TestScraperSSRF(unittest.TestCase):
    def setUp(self):
        self.scraper = BlogScraper("http://example.com")

    def test_validate_url_valid(self):
        # valid url should not raise exception
        url = "https://wishlist.design.blog"
        self.scraper.validate_url(url)

    def test_validate_url_invalid_scheme(self):
        # file scheme should be rejected
        url = "file:///etc/passwd"
        with self.assertRaises(ValueError):
            self.scraper.validate_url(url)

        # ftp scheme should be rejected
        url = "ftp://example.com"
        with self.assertRaises(ValueError):
            self.scraper.validate_url(url)

    def test_validate_url_localhost(self):
        # localhost should be rejected
        urls = [
            "http://localhost:8080",
            "http://127.0.0.1/admin",
            "http://[::1]/secret"
        ]
        for url in urls:
            with self.assertRaises(ValueError):
                self.scraper.validate_url(url)

if __name__ == '__main__':
    unittest.main()
