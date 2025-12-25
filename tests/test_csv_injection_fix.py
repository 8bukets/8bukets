import unittest
import csv
import io
import os
import sys
from unittest.mock import MagicMock

# Add root directory to path to import scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scraper import MarkPositionScraperAsync

class TestCSVInjection(unittest.TestCase):
    def test_csv_injection_fix(self):
        """
        Test that payloads starting with =, +, -, @ are now sanitized with a leading quote.
        """
        scraper = MarkPositionScraperAsync("mock.json", "mock.csv", "mock.txt")

        # Malicious payloads
        payloads = [
            {'title': '=cmd|/C calc!A0', 'author': 'hacker', 'date': '2023-01-01'},
            {'title': '+cmd|/C calc!A0', 'author': 'hacker', 'date': '2023-01-01'},
            {'title': '-cmd|/C calc!A0', 'author': 'hacker', 'date': '2023-01-01'},
            {'title': '@cmd|/C calc!A0', 'author': 'hacker', 'date': '2023-01-01'},
        ]

        # Mock file objects
        mock_json_f = MagicMock()
        mock_csv_f = io.StringIO()
        mock_txt_f = MagicMock()

        csv_writer = csv.writer(mock_csv_f)
        seen_links = set()

        scraper.save_batch(payloads, mock_json_f, csv_writer, mock_txt_f, seen_links, True)

        output = mock_csv_f.getvalue()

        # The output should now contain sanitized payloads
        # Note: CSV writer might quote the field if it contains special chars like commas, but here we just check for the content.
        # But actually, if we prepend ', the CSV writer might just write it as is or quote it.
        # Let's check for the presence of the sanitized string.

        self.assertIn("'=cmd|/C calc!A0", output)
        self.assertIn("'+cmd|/C calc!A0", output)
        self.assertIn("'-cmd|/C calc!A0", output)
        self.assertIn("'@cmd|/C calc!A0", output)

if __name__ == '__main__':
    unittest.main()
