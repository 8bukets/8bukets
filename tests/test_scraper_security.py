import unittest
import io
import csv
from scraper import MarkPositionScraperAsync

class TestScraperSecurity(unittest.TestCase):
    def test_csv_injection_sanitization(self):
        scraper = MarkPositionScraperAsync("dummy.json", "dummy.csv", "dummy.txt")

        # Test individual sanitization
        self.assertEqual(scraper.sanitize_for_csv("=1+1"), "'=1+1")
        self.assertEqual(scraper.sanitize_for_csv("+data"), "'+data")
        self.assertEqual(scraper.sanitize_for_csv("-data"), "'-data")
        self.assertEqual(scraper.sanitize_for_csv("@data"), "'@data")
        self.assertEqual(scraper.sanitize_for_csv("Safe Data"), "Safe Data")
        self.assertEqual(scraper.sanitize_for_csv(""), "")

    def test_save_batch_security(self):
        scraper = MarkPositionScraperAsync("dummy.json", "dummy.csv", "dummy.txt")

        # Mock objects
        csv_output = io.StringIO()
        csv_writer = csv.writer(csv_output)
        json_output = io.StringIO()
        txt_output = io.StringIO()

        malicious_posts = [
            {
                'title': '=cmd|/C calc.exe!A0',
                'date': '2023-01-01',
                'author': '@attacker',
                'categories': ['+badcat'],
                'external_link': '-http://example.com',
                'domain': 'example.com',
                'post_url': 'http://site.com/post'
            }
        ]

        scraper.save_batch(malicious_posts, json_output, csv_writer, txt_output, set(), True)

        output = csv_output.getvalue().strip()

        # Check that dangerous fields are quoted
        self.assertIn("'=cmd|/C calc.exe!A0", output)
        self.assertIn("'@attacker", output)
        self.assertIn("'+badcat", output)
        self.assertIn("'-http://example.com", output)

if __name__ == '__main__':
    unittest.main()
