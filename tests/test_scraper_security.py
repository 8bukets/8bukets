
import unittest
from scraper import MarkPositionScraperAsync

class TestScraperSecurity(unittest.TestCase):
    def test_sanitize_for_csv(self):
        scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")

        # Test vulnerable strings
        self.assertEqual(scraper.sanitize_for_csv("=cmd|'/C calc'!A0"), "'=cmd|'/C calc'!A0")
        self.assertEqual(scraper.sanitize_for_csv("+SUM(1+1)"), "'+SUM(1+1)")
        self.assertEqual(scraper.sanitize_for_csv("-10+20"), "'-10+20")
        self.assertEqual(scraper.sanitize_for_csv("@SUM(1+1)"), "'@SUM(1+1)")

        # Test safe strings
        self.assertEqual(scraper.sanitize_for_csv("Normal Text"), "Normal Text")
        self.assertEqual(scraper.sanitize_for_csv("http://example.com"), "http://example.com")
        self.assertEqual(scraper.sanitize_for_csv(""), "")
        self.assertEqual(scraper.sanitize_for_csv(None), "")

        # Test whitespaces handling
        self.assertEqual(scraper.sanitize_for_csv(" =1+1"), "' =1+1")
        self.assertEqual(scraper.sanitize_for_csv("\t-1"), "'\t-1")

if __name__ == '__main__':
    unittest.main()
