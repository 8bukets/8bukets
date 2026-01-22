import unittest
import csv
import os
import asyncio
from scraper import MarkPositionScraperAsync

class MockScraper(MarkPositionScraperAsync):
    def __init__(self, output_csv):
        super().__init__("dummy_test.json", output_csv, "dummy_test.txt")

    async def scrape(self):
        pass

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        self.output_csv = "test_security_output.csv"

    def tearDown(self):
        if os.path.exists(self.output_csv):
            os.remove(self.output_csv)
        if os.path.exists("dummy_test.json"):
            os.remove("dummy_test.json")
        if os.path.exists("dummy_test.txt"):
            os.remove("dummy_test.txt")

    def test_csv_injection_sanitization(self):
        posts = [
            {
                'title': '=1+1',
                'date': '2023-01-01',
                'author': '@attacker',
                'categories': ['News'],
                'external_link': 'http://example.com',
                'domain': 'example.com',
                'post_url': 'http://site.com/post'
            },
            {
                'title': '+SUM(1,2)',
                'date': '2023-01-02',
                'author': '-someone',
                'categories': [],
                'external_link': '',
                'domain': '',
                'post_url': ''
            }
        ]

        scraper = MockScraper(self.output_csv)
        scraper.save_data(posts)

        with open(self.output_csv, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row1 = next(reader)
            row2 = next(reader)

        self.assertEqual(row1[0], "'=1+1")
        self.assertEqual(row1[2], "'@attacker")
        self.assertEqual(row2[0], "'+SUM(1,2)")
        self.assertEqual(row2[2], "'-someone")

if __name__ == '__main__':
    unittest.main()
