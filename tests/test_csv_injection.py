import unittest
import csv
import os
import json
from unittest.mock import MagicMock, AsyncMock, patch
import asyncio
import sys

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scraper import OracleNewsScraper

class TestCSVInjection(unittest.TestCase):
    def setUp(self):
        self.output_json = 'test_output.json'
        self.output_csv = 'test_output.csv'
        self.output_txt = 'test_output.txt'
        self.scraper = OracleNewsScraper(self.output_json, self.output_csv, self.output_txt)

    def tearDown(self):
        for f in [self.output_json, self.output_csv, self.output_txt]:
            if os.path.exists(f):
                os.remove(f)

    def test_save_data_csv_injection(self):
        """Test if CSV injection is prevented."""
        # Malicious data
        posts = [{
            'title': '=1+1',
            'date': '@SUM(1,1)',
            'author': '+cmd',
            'categories': ['News'],
            'external_link': '-bad',
            'domain': 'example.com',
            'post_url': 'http://example.com'
        }]

        self.scraper.save_data(posts)

        # Check CSV content
        with open(self.output_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)

            # In a secure system, the malicious characters are escaped
            self.assertEqual(row[0], "'=1+1")
            self.assertEqual(row[1], "'@SUM(1,1)")
            self.assertEqual(row[2], "'+cmd")
            self.assertEqual(row[4], "'-bad")

if __name__ == '__main__':
    unittest.main()
