import unittest
import os
import json
from datetime import datetime
from analytics import generate_report

class TestAnalyticsUX(unittest.TestCase):
    def setUp(self):
        self.test_data = [
            {
                "domain": "example.com",
                "categories": ["Tech", "News"],
                "datetime": "2023-01-01T10:00:00",
                "author": "Alice"
            },
            {
                "domain": "example.com",
                "categories": ["Tech"],
                "datetime": "2023-01-02T10:00:00",
                "author": "Bob"
            },
            {
                "domain": "google.com",
                "categories": ["Search"],
                "datetime": "2023-02-01T10:00:00",
                "author": "Alice"
            }
        ]
        self.output_file = "TEST_REPORT.md"

    def tearDown(self):
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_report_content(self):
        generate_report(self.test_data, self.output_file)

        with open(self.output_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for Executive Summary elements
        self.assertIn("## 📊 Executive Summary", content)
        self.assertIn("| Metric | Value |", content)
        self.assertIn("Total Posts", content)

        # Check for Collapsible sections
        self.assertIn("<details>", content)
        self.assertIn("<summary>", content)

        # Check for Visual bars (simple check for the block character)
        self.assertIn("█", content)

        # Check for other emojis
        self.assertIn("🌐", content) # Domains
        self.assertIn("🏷️", content) # Categories
        self.assertIn("📅", content) # Years
        self.assertIn("✍️", content) # Authors

if __name__ == "__main__":
    unittest.main()
