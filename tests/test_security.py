import unittest
from scraper import MarkPositionScraperAsync

class TestSecurity(unittest.TestCase):
    def setUp(self):
        self.scraper = MarkPositionScraperAsync("dummy.json", "dummy.csv", "dummy.txt")

    def test_csv_injection_sanitization(self):
        # Test cases for CSV injection characters
        dangerous_inputs = [
            ("=SUM(A1:A2)", "'=SUM(A1:A2)"),
            ("+1+2", "'+1+2"),
            ("-1-2", "'-1-2"),
            ("@echo", "'@echo"),
            ("Safe string", "Safe string"),
            ("", ""),
            (None, None)
        ]

        for inp, expected in dangerous_inputs:
            with self.subTest(input=inp):
                result = self.scraper.sanitize_for_csv(inp)
                self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
