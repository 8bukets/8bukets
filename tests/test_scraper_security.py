import unittest
from scraper import OracleNewsScraper

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        self.scraper = OracleNewsScraper(
            output_json="test.json",
            output_csv="test.csv",
            output_txt="test.txt"
        )

    def test_validate_url_valid(self):
        """Test that valid oracle.com URLs are accepted."""
        if hasattr(self.scraper, 'validate_url'):
            self.assertTrue(self.scraper.validate_url("https://www.oracle.com/news/announcement/test"))
            self.assertTrue(self.scraper.validate_url("http://oracle.com/something"))
        else:
            self.fail("validate_url method not implemented")

    def test_validate_url_invalid_domain(self):
        """Test that non-oracle.com URLs are rejected."""
        if hasattr(self.scraper, 'validate_url'):
            self.assertFalse(self.scraper.validate_url("https://evil.com/news"))
            self.assertFalse(self.scraper.validate_url("https://google.com"))
        else:
            self.fail("validate_url method not implemented")

    def test_validate_url_invalid_scheme(self):
        """Test that non-http/https schemes are rejected."""
        if hasattr(self.scraper, 'validate_url'):
            self.assertFalse(self.scraper.validate_url("ftp://oracle.com/file"))
            self.assertFalse(self.scraper.validate_url("file:///etc/passwd"))
            self.assertFalse(self.scraper.validate_url("javascript:alert(1)"))
        else:
            self.fail("validate_url method not implemented")

if __name__ == '__main__':
    unittest.main()
