import unittest
from unittest.mock import patch
from scraper import BlogScraper

class TestScraperSecurity(unittest.TestCase):
    def test_ssrf_file_scheme(self):
        """Test that the scraper blocks file:// URLs."""
        scraper = BlogScraper("http://example.com")

        # Simulate a URL that might be exploited to read local files
        malicious_url = "file:///etc/passwd"

        # We'll patch requests.get to see if it gets called with the malicious URL
        with patch('requests.get') as mock_get:
            scraper.fetch_page(malicious_url)

            # Use assertions to ensure the test fails if the vulnerability exists
            self.assertFalse(mock_get.called, "requests.get should NOT be called for file:// URLs")

if __name__ == '__main__':
    unittest.main()
