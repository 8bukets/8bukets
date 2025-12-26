import unittest
from unittest.mock import MagicMock
import sys
import os

# Add root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import MarkPositionScraperAsync

class TestCSVSecurity(unittest.TestCase):
    def test_csv_injection_prevention(self):
        """
        Test that fields starting with =, @, +, - are sanitized by prepending a single quote
        to prevent CSV injection attacks (Formula Injection).
        """
        scraper = MarkPositionScraperAsync("json", "csv", "txt")

        # Malicious data
        malicious_posts = [{
            'title': '=cmd|"/C calc"!A0',
            'date': '@SUM(1+1)',
            'author': '+Dangerous',
            'categories': ['-Minus'],
            'external_link': 'http://example.com',
            'domain': 'example.com',
            'post_url': 'http://example.com/post'
        }]

        # Mocks
        mock_json = MagicMock()
        mock_csv = MagicMock()
        mock_txt = MagicMock()
        seen_links = set()

        scraper.save_batch(malicious_posts, mock_json, mock_csv, mock_txt, seen_links, True)

        # Get the arguments passed to csv_writer.writerow
        # call_args returns (args, kwargs), and args is a tuple.
        # save_batch calls writerow with a single list argument.
        args = mock_csv.writerow.call_args[0][0]

        # Verify Sanitization (Expectation: prepended single quote)

        # Title: =cmd... -> '=cmd...
        self.assertTrue(args[0].startswith("'="), f"Title vulnerable to CSV Injection: {args[0]}")

        # Date: @SUM... -> '@SUM...
        self.assertTrue(args[1].startswith("'@"), f"Date vulnerable to CSV Injection: {args[1]}")

        # Author: +Dangerous -> '+Dangerous
        self.assertTrue(args[2].startswith("'+"), f"Author vulnerable to CSV Injection: {args[2]}")

        # Categories: -Minus -> '-Minus
        # Note: scraper joins categories with ", ". The string will start with -
        self.assertTrue(args[3].startswith("'-"), f"Categories vulnerable to CSV Injection: {args[3]}")

if __name__ == '__main__':
    unittest.main()
