import unittest
import json
import os
import sys
from datetime import datetime

# Ensure we can import analytics
sys.path.append(os.getcwd())
import analytics

class TestAnalytics(unittest.TestCase):
    def setUp(self):
        self.test_data = [
            {
                "title": "Post 1",
                "date": "2023-01-01",
                "author": "Alice",
                "categories": ["Tech", "News"],
                "external_link": "https://example.com/1",
                "domain": "example.com"
            },
            {
                "title": "Post 2",
                "date": "2023-06-01",
                "author": "Bob",
                "categories": ["Tech"],
                "external_link": "https://other.com/2",
                "domain": "other.com"
            },
            {
                "title": "Post 3",
                "date": "2024-01-01",
                "author": "Alice",
                "categories": ["News"],
                "external_link": "https://example.com/3",
                "domain": "example.com"
            }
        ]
        self.output_file = "TEST_REPORT.md"

    def tearDown(self):
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_report_content(self):
        analytics.generate_report(self.test_data, self.output_file)

        with open(self.output_file, 'r') as f:
            content = f.read()

        # Check General Stats
        self.assertIn("Total Posts:** 3", content)
        self.assertIn("Unique Domains Linked:** 2", content)

        # Check Top Domains
        self.assertIn("| example.com | 2 |", content)
        self.assertIn("| other.com | 1 |", content)

        # Check Categories
        self.assertIn("| Tech | 2 |", content)
        self.assertIn("| News | 2 |", content)

        # Check Authors
        self.assertIn("- Alice: 2 posts", content)
        self.assertIn("- Bob: 1 posts", content)

    def test_date_parsing_correctness(self):
        # This test asserts correct date parsing behavior
        analytics.generate_report(self.test_data, self.output_file)
        with open(self.output_file, 'r') as f:
            content = f.read()

        self.assertIn("2023-01-01 to 2024-01-01", content)
        self.assertIn("| 2023 | 2 |", content)
        self.assertIn("| 2024 | 1 |", content)

if __name__ == '__main__':
    unittest.main()
