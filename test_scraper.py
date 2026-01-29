import unittest
from scraper import MarkPositionScraperAsync

class TestScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = MarkPositionScraperAsync('test.json', 'test.csv', 'test.txt')

    def test_sanitize_for_csv(self):
        # Test dangerous characters
        self.assertEqual(self.scraper.sanitize_for_csv('=cmd'), "'=cmd")
        self.assertEqual(self.scraper.sanitize_for_csv('+SUM'), "'+SUM")
        self.assertEqual(self.scraper.sanitize_for_csv('-10'), "'-10")
        self.assertEqual(self.scraper.sanitize_for_csv('@echo'), "'@echo")

        # Test safe characters
        self.assertEqual(self.scraper.sanitize_for_csv('Safe title'), "Safe title")
        self.assertEqual(self.scraper.sanitize_for_csv('123'), "123")

        # Test non-string inputs
        self.assertEqual(self.scraper.sanitize_for_csv(None), "")
        self.assertEqual(self.scraper.sanitize_for_csv(123), "123")

if __name__ == '__main__':
    unittest.main()
