import unittest
import os
import csv
from scraper import OracleNewsScraper

class TestCSVInjection(unittest.TestCase):
    def setUp(self):
        self.json_file = 'test_security_links.json'
        self.csv_file = 'test_security_links.csv'
        self.txt_file = 'test_security_unique_links.txt'
        self.scraper = OracleNewsScraper(self.json_file, self.csv_file, self.txt_file)

    def tearDown(self):
        if os.path.exists(self.json_file):
            os.remove(self.json_file)
        if os.path.exists(self.csv_file):
            os.remove(self.csv_file)
        if os.path.exists(self.txt_file):
            os.remove(self.txt_file)

    def test_csv_sanitization(self):
        """Verify that CSV fields starting with specific chars are sanitized."""
        dangerous_inputs = [
            ("=cmd|' /C calc'!A0", "'=cmd|' /C calc'!A0"),
            ("+1+2", "'+1+2"),
            ("-1+2", "'-1+2"),
            ("@SUM(A1:A2)", "'@SUM(A1:A2)"),
            ("Normal Title", "Normal Title"),
            ("", ""),
            (None, None) # sanitize_for_csv handles None appropriately if passed through clean_text logic, but here it is passed directly.
                         # Actually get() returns '' by default in scraper, so we test strings mainly.
        ]

        # Test the method directly
        for input_str, expected in dangerous_inputs:
            if input_str is None: continue
            self.assertEqual(self.scraper.sanitize_for_csv(input_str), expected)

    def test_end_to_end_csv_output(self):
        """Verify that the CSV output file actually contains sanitized data."""
        posts = [{
            'title': "=Dangerous Title",
            'date': 'Oct 15, 2025',
            'author': '@Hacker',
            'categories': ['+News', '-Update'],
            'external_link': 'http://evil.com',
            'domain': 'evil.com',
            'post_url': 'http://evil.com'
        }]

        self.scraper.save_data(posts)

        with open(self.csv_file, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader)
            row = next(reader)

            # Check Title
            self.assertEqual(row[0], "'=Dangerous Title")
            # Check Author
            self.assertEqual(row[2], "'@Hacker")
            # Check Categories (joined)
            # categories are joined by ", " then sanitized. "+News, -Update" -> "'+News, -Update"
            self.assertEqual(row[3], "'+News, -Update")

if __name__ == '__main__':
    unittest.main()
