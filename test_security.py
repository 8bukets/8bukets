import unittest
import os
import csv
from scraper import MarkPositionScraperAsync

class TestCSVInjectionFix(unittest.TestCase):
    def setUp(self):
        self.output_json = 'test_fix.json'
        self.output_csv = 'test_fix.csv'
        self.output_txt = 'test_fix.txt'
        self.scraper = MarkPositionScraperAsync(self.output_json, self.output_csv, self.output_txt)

    def tearDown(self):
        for f in [self.output_json, self.output_csv, self.output_txt]:
            if os.path.exists(f):
                os.remove(f)

    def test_sanitize_for_csv(self):
        # Test cases: (input, expected)
        test_cases = [
            ('=1+1', "'=1+1"),
            ('+1+1', "'+1+1"),
            ('-1+1', "'-1+1"),
            ('@attacker', "'@attacker"),
            ('Normal Text', 'Normal Text'),
            ('', ''),
            (None, ''),
            ('1+1', '1+1'), # Does not start with dangerous char
            ('==', "'==")
        ]

        for inp, expected in test_cases:
            with self.subTest(input=inp):
                self.assertEqual(self.scraper.sanitize_for_csv(inp), expected)

    def test_save_data_sanitization(self):
        malicious_posts = [
            {
                'title': '=1+1',
                'date': '2023-01-01',
                'author': '@attacker',
                'categories': ['=cmd|/C calc!A0'],
                'external_link': 'http://example.com',
                'domain': 'example.com',
                'post_url': 'http://example.com/post'
            }
        ]

        self.scraper.save_data(malicious_posts)

        with open(self.output_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)

            # Row structure: Title, Date, Author, Categories, External Link, Domain, Post URL
            # Expecting sanitization
            self.assertEqual(row[0], "'=1+1")
            self.assertEqual(row[2], "'@attacker")
            self.assertEqual(row[3], "'=cmd|/C calc!A0")

if __name__ == '__main__':
    unittest.main()
