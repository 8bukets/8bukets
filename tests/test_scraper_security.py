import unittest
from unittest.mock import MagicMock, mock_open, patch
import sys
import os

# Add parent directory to path to import scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import MarkPositionScraperAsync

class TestCSVInjection(unittest.TestCase):
    def test_csv_injection_vulnerability(self):
        # Setup
        scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")

        # Malicious payloads
        malicious_posts = [
            {
                'title': '=1+1',  # Formula injection
                'date': '2023-01-01',
                'author': 'Hacker',
                'categories': ['Security'],
                'external_link': 'http://example.com',
                'domain': 'example.com',
                'post_url': 'http://example.com/post'
            },
            {
                'title': 'Safe Title',
                'date': '@SUM(1,2)', # Another injection
                'author': '+cmd|/c calc!A0', # DDE injection
                'categories': ['-Malicious'],
                'external_link': 'http://example.com',
                'domain': 'example.com',
                'post_url': 'http://example.com/post'
            }
        ]

        # Mocks
        mock_json_f = MagicMock()
        mock_csv_writer = MagicMock()
        mock_txt_f = MagicMock()
        seen_links = set()

        # Execute
        scraper.save_batch(malicious_posts, mock_json_f, mock_csv_writer, mock_txt_f, seen_links, True)

        # Verify
        # Get calls to writerow
        calls = mock_csv_writer.writerow.call_args_list
        self.assertEqual(len(calls), 2)

        # Check first row (FIXED BEHAVIOR: expects sanitized input)
        row1 = calls[0][0][0] # args[0] is the list of fields
        self.assertEqual(row1[0], "'=1+1")

        # Check second row
        row2 = calls[1][0][0]
        self.assertEqual(row2[1], "'@SUM(1,2)")
        self.assertEqual(row2[2], "'+cmd|/c calc!A0")
        # Categories are joined by ", " so "-Malicious" remains "-Malicious"
        self.assertEqual(row2[3], "'-Malicious")

if __name__ == '__main__':
    unittest.main()
