
import unittest
from scraper import OracleNewsScraper
import os
import tempfile
import json
import csv

class TestOracleNewsScraper(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()
        self.json_file = os.path.join(self.test_dir.name, 'test.json')
        self.csv_file = os.path.join(self.test_dir.name, 'test.csv')
        self.txt_file = os.path.join(self.test_dir.name, 'test.txt')
        self.scraper = OracleNewsScraper(self.json_file, self.csv_file, self.txt_file)

        # Load sample HTML
        try:
            with open('oracle_news.html', 'r', encoding='utf-8') as f:
                self.html = f.read()
        except FileNotFoundError:
             self.fail("oracle_news.html not found for testing.")

    def tearDown(self):
        self.test_dir.cleanup()

    def test_clean_text(self):
        text = "  Hello   World \xa0 "
        cleaned = self.scraper.clean_text(text)
        self.assertEqual(cleaned, "Hello World")

    def test_parse_date(self):
        res = self.scraper.parse_date('Oct 15, 2025')
        self.assertEqual(res['iso'], '2025-10-15T00:00:00')
        self.assertEqual(res['display'], 'Oct 15, 2025')

        res_invalid = self.scraper.parse_date('Invalid Date')
        self.assertIsNone(res_invalid['iso'])
        self.assertEqual(res_invalid['display'], 'Invalid Date')

    def test_parse_page(self):
        posts = self.scraper.parse_page(self.html)
        self.assertIsInstance(posts, list)
        self.assertGreater(len(posts), 0, "Should find posts in oracle_news.html")

        first_post = posts[0]
        self.assertIn('title', first_post)
        self.assertIn('date', first_post)
        self.assertIn('external_link', first_post)

        # Check specific content if known, otherwise just structure
        # (Assuming the fetched HTML has standard structure)

    def test_save_data(self):
        posts = [{'title': 'Test Post', 'date': 'Jan 1, 2023', 'external_link': 'http://example.com'}]
        self.scraper.save_data(posts)

        self.assertTrue(os.path.exists(self.json_file))
        with open(self.json_file, 'r') as f:
            data = json.load(f)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]['title'], 'Test Post')

        self.assertTrue(os.path.exists(self.csv_file))
        self.assertTrue(os.path.exists(self.txt_file))

if __name__ == '__main__':
    unittest.main()
