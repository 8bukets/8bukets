import unittest
from scraper import MarkPositionScraperAsync

class TestScraperSecurity(unittest.TestCase):
    """Security tests for the scraper."""
    def test_sanitize_for_csv(self):
        """Test that CSV injection characters are escaped."""
        scraper = MarkPositionScraperAsync("dummy.json", "dummy.csv", "dummy.txt")

        # Test cases vulnerable to CSV injection
        self.assertEqual(scraper.sanitize_for_csv("=SUM(1+1)"), "'=SUM(1+1)")
        self.assertEqual(scraper.sanitize_for_csv("+SUM(1+1)"), "'+SUM(1+1)")
        self.assertEqual(scraper.sanitize_for_csv("-SUM(1+1)"), "'-SUM(1+1)")
        self.assertEqual(scraper.sanitize_for_csv("@SUM(1+1)"), "'@SUM(1+1)")

        # Test safe cases
        self.assertEqual(scraper.sanitize_for_csv("Safe Title"), "Safe Title")
        self.assertEqual(scraper.sanitize_for_csv(""), "")
        self.assertEqual(scraper.sanitize_for_csv(None), "")
        self.assertEqual(scraper.sanitize_for_csv("123"), "123")

if __name__ == '__main__':
    unittest.main()
