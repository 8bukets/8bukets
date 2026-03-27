import unittest
import csv
import os
from scraper import MarkPositionScraperAsync

class TestCSVInjection(unittest.TestCase):
    def setUp(self):
        self.output_csv = "test_injection.csv"
        self.output_json = "test_injection.json"
        self.output_txt = "test_injection.txt"
        self.scraper = MarkPositionScraperAsync(self.output_json, self.output_csv, self.output_txt)

    def tearDown(self):
        for f in [self.output_csv, self.output_json, self.output_txt]:
            if os.path.exists(f):
                os.remove(f)

    def test_sanitize_for_csv(self):
        # Test basic characters
        self.assertEqual(self.scraper.sanitize_for_csv("Normal"), "Normal")
        self.assertEqual(self.scraper.sanitize_for_csv("123"), "123")

        # Test dangerous characters
        self.assertEqual(self.scraper.sanitize_for_csv("=sum(1+1)"), "'=sum(1+1)")
        self.assertEqual(self.scraper.sanitize_for_csv("+plus"), "'+plus")
        self.assertEqual(self.scraper.sanitize_for_csv("-minus"), "'-minus")
        self.assertEqual(self.scraper.sanitize_for_csv("@link"), "'@link")
        self.assertEqual(self.scraper.sanitize_for_csv("\ttab"), "'\ttab")

        # Test None and empty
        self.assertEqual(self.scraper.sanitize_for_csv(None), "")
        self.assertEqual(self.scraper.sanitize_for_csv(""), "")

    def test_save_batch_injection(self):
        malicious_title = "=cmd|' /C calc'!A0"
        posts = [
            {
                'title': malicious_title,
                'date': '2023-01-01',
                'author': 'Hacker',
                'categories': ['Security'],
                'external_link': 'http://example.com',
                'domain': 'example.com',
                'post_url': 'http://example.com/post'
            }
        ]

        with open(self.output_json, 'w', encoding='utf-8') as json_f, \
             open(self.output_csv, 'w', newline='', encoding='utf-8') as csv_f, \
             open(self.output_txt, 'w', encoding='utf-8') as txt_f:

            csv_writer = csv.writer(csv_f)
            self.scraper.save_batch(posts, json_f, csv_writer, txt_f, set(), True)

        with open(self.output_csv, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)
            injected_row = rows[0]
            title = injected_row[0]

            self.assertFalse(title.startswith('='))
            self.assertEqual(title, f"'{malicious_title}")

if __name__ == '__main__':
    unittest.main()
