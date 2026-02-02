import unittest
from unittest.mock import MagicMock
import sys
import os

# Add parent directory to path to import scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import MarkPositionScraperAsync

class TestSecurity(unittest.TestCase):
    def test_csv_injection_sanitization(self):
        """Test that fields starting with =, +, -, @ are sanitized with a leading single quote."""
        scraper = MarkPositionScraperAsync('json', 'csv', 'txt')

        # Mock file objects
        mock_csv_writer = MagicMock()
        mock_json_f = MagicMock()
        mock_txt_f = MagicMock()
        seen_links = set()

        # Malicious input
        malicious_posts = [
            {
                'title': '=SUM(1+1)',
                'date': '+2023-01-01',
                'author': '-Author',
                'categories': ['@Category'],
                'external_link': 'http://example.com',
                'domain': 'example.com',
                'post_url': 'http://example.com/post'
            }
        ]

        scraper.save_batch(malicious_posts, mock_json_f, mock_csv_writer, mock_txt_f, seen_links, True)

        # Check what was written to CSV
        args, _ = mock_csv_writer.writerow.call_args
        row = args[0]

        # Expected: all dangerous fields should be prepended with '
        self.assertEqual(row[0], "'=SUM(1+1)", "Title should be sanitized")
        self.assertEqual(row[1], "'+2023-01-01", "Date should be sanitized")
        self.assertEqual(row[2], "'-Author", "Author should be sanitized")
        # Categories are joined by comma, check if the string starts with '
        self.assertEqual(row[3], "'@Category", "Categories should be sanitized")

if __name__ == '__main__':
    unittest.main()
