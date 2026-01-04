import unittest
import json
import os
import sys
from datetime import datetime
from collections import Counter

# Add parent directory to path so we can import analytics
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from analytics import generate_report, get_domain

class TestAnalytics(unittest.TestCase):
    def setUp(self):
        self.test_data = [
            {
                "title": "Post 1",
                "datetime": "2023-01-01T10:00:00",
                "author": "Alice",
                "categories": ["Tech", "News"],
                "external_link": "https://example.com/1"
            },
            {
                "title": "Post 2",
                "datetime": "2023-01-02T11:00:00",
                "author": "Bob",
                "categories": ["Tech"],
                "external_link": "https://example.com/2"
            },
            {
                "title": "Post 3",
                "datetime": "2023-02-01T12:00:00",
                "author": "Alice",
                "categories": ["Life"],
                "external_link": "https://blog.example.com/3"
            },
            {
                "title": "Post 4",
                "datetime": "invalid-date",
                "author": "Charlie",
                "categories": [],
                "external_link": None
            }
        ]
        self.output_file = "test_report.md"

    def tearDown(self):
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_get_domain(self):
        self.assertEqual(get_domain("https://example.com/foo"), "example.com")
        self.assertEqual(get_domain("https://www.example.com/foo"), "example.com")
        self.assertIsNone(get_domain(None))
        self.assertIsNone(get_domain(""))

    def test_generate_report(self):
        generate_report(self.test_data, self.output_file)

        self.assertTrue(os.path.exists(self.output_file))

        with open(self.output_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check General Statistics
        self.assertIn("**Total Posts:** 4", content)
        self.assertIn("**Unique Domains Linked:** 2", content) # example.com, blog.example.com

        # Check Domains
        self.assertIn("| example.com | 2 |", content)
        self.assertIn("| blog.example.com | 1 |", content)

        # Check Categories
        self.assertIn("| Tech | 2 |", content)
        self.assertIn("| News | 1 |", content)
        self.assertIn("| Life | 1 |", content)

        # Check Authors
        self.assertIn("- Alice: 2 posts", content)
        self.assertIn("- Bob: 1 posts", content)
        self.assertIn("- Charlie: 1 posts", content)

        # Check Years
        self.assertIn("| 2023 | 3 |", content)

if __name__ == '__main__':
    unittest.main()
