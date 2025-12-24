import unittest
from scraper import MarkPositionScraperAsync

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        self.scraper = MarkPositionScraperAsync('dummy.json', 'dummy.csv', 'dummy.txt')

    def test_sanitize_csv_field_basic(self):
        self.assertEqual(self.scraper.sanitize_csv_field("Normal"), "Normal")
        self.assertEqual(self.scraper.sanitize_csv_field("123"), "123")

    def test_sanitize_csv_field_injection(self):
        self.assertEqual(self.scraper.sanitize_csv_field("=cmd"), "'=cmd")
        self.assertEqual(self.scraper.sanitize_csv_field("+1+1"), "'+1+1")
        self.assertEqual(self.scraper.sanitize_csv_field("-1+1"), "'-1+1")
        self.assertEqual(self.scraper.sanitize_csv_field("@SUM"), "'@SUM")

    def test_sanitize_csv_field_none(self):
        self.assertEqual(self.scraper.sanitize_csv_field(None), "")

    def test_sanitize_csv_field_non_string(self):
        self.assertEqual(self.scraper.sanitize_csv_field(123), "123")

if __name__ == '__main__':
    unittest.main()
