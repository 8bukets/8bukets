import unittest
from scraper import OracleNewsScraper

class TestOracleNewsScraper(unittest.TestCase):
    def test_clean_text(self):
        scraper = OracleNewsScraper(output_json="", output_csv="", output_txt="")
        self.assertEqual(scraper.clean_text("  Hello   World  "), "Hello World")
        self.assertEqual(scraper.clean_text("Hello\xa0World"), "Hello World")

    def test_sanitize_for_csv(self):
        scraper = OracleNewsScraper(output_json="", output_csv="", output_txt="")
        self.assertEqual(scraper.sanitize_for_csv("=1+1"), "'=1+1")
        self.assertEqual(scraper.sanitize_for_csv("Normal text"), "Normal text")
        self.assertEqual(scraper.sanitize_for_csv("+Positive"), "'+Positive")
        self.assertEqual(scraper.sanitize_for_csv("-Negative"), "'-Negative")
        self.assertEqual(scraper.sanitize_for_csv("@Mention"), "'@Mention")
        self.assertEqual(scraper.sanitize_for_csv("%Percent"), "'%Percent")

    def test_is_allowed_url(self):
        scraper = OracleNewsScraper(output_json="", output_csv="", output_txt="")
        # Allowed
        self.assertTrue(scraper.is_allowed_url("https://www.oracle.com/news/something"))
        self.assertTrue(scraper.is_allowed_url("http://www.oracle.com/news"))

        # Disallowed Domains
        self.assertFalse(scraper.is_allowed_url("https://evil.com/news"))
        self.assertFalse(scraper.is_allowed_url("https://google.com"))

        # Disallowed Schemes
        self.assertFalse(scraper.is_allowed_url("ftp://www.oracle.com/news"))
        self.assertFalse(scraper.is_allowed_url("file:///etc/passwd"))

        # Subdomain mismatch (strict check in current impl)
        self.assertFalse(scraper.is_allowed_url("https://oracle.com/news"))

if __name__ == '__main__':
    unittest.main()
