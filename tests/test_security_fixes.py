import unittest
from scraper import MarkPositionScraperAsync

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        self.scraper = MarkPositionScraperAsync("links.json", "links.csv", "unique_links.txt")

    def test_is_url_security(self):
        """Test strict URL validation."""
        valid_urls = [
            "http://example.com",
            "https://example.com",
            "https://sub.example.com/path?query=1",
            "https://example.com/foo-bar"
        ]
        invalid_urls = [
            "ftp://example.com",
            "javascript:alert(1)",
            "http://example.com<script>",
            "http://example.com/foo bar",
            "http://example.com/foo\"bar",
            "http://example.com/foo'bar",
            "http://example.com/foo`bar"
        ]

        for url in valid_urls:
            self.assertTrue(self.scraper.is_url(url), f"Should accept valid URL: {url}")

        for url in invalid_urls:
            self.assertFalse(self.scraper.is_url(url), f"Should reject invalid URL: {url}")

    def test_extract_domain_security(self):
        """Test secure domain extraction."""
        test_cases = [
            ("https://example.com", "example.com"),
            ("https://www.example.com", "example.com"),
            ("http://sub-domain.example.co.uk", "sub-domain.example.co.uk"),
            ("http://example.com:8080", "example.com:8080"), # Port should be allowed
            ("http://example.com<script>", None),
            ("http://example.com/foo<bar", "example.com"), # URLParse splits netloc correctly usually, but let's see
        ]

        # For "http://example.com/foo<bar", urlparse netloc is "example.com".
        # But if the injection is in the domain part:
        # "http://example.com<script>/foo" -> netloc "example.com<script>" -> Should be None

        for url, expected in test_cases:
            result = self.scraper.extract_domain(url)
            self.assertEqual(result, expected, f"Failed for {url}")

    def test_extract_domain_injection_attempts(self):
        injection_attempts = [
            "http://example.com<script>",
            "http://example.com|pipe",
            "http://example.com;ls",
            "http://example.com$(whoami)"
        ]
        for url in injection_attempts:
            self.assertIsNone(self.scraper.extract_domain(url), f"Should reject injection attempt: {url}")

if __name__ == '__main__':
    unittest.main()
