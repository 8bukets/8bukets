import unittest
import json
import os
import sys
import tempfile
from unittest.mock import patch

# Add parent directory to path to import analytics
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import analytics

class TestAnalyticsSecurity(unittest.TestCase):
    def setUp(self):
        # Create a temporary file for output
        self.output_file = "test_report.md"

    def tearDown(self):
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_markdown_table_injection(self):
        """Test that pipes in data do not break Markdown table structure."""

        # Malicious data containing pipes
        data = [
            {
                "title": "Malicious Post",
                "categories": ["Category | Injection", "Normal"],
                "external_link": "https://example.com/page",
                "author": "Hacker",
                "datetime": "2023-01-01T12:00:00"
            }
        ]

        # Generate report
        analytics.generate_report(data, self.output_file)

        # Read the report
        with open(self.output_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for escaped pipes in the table
        found = False
        for line in content.splitlines():
            if "Injection" in line:
                found = True
                self.assertNotIn("Category | Injection", line, "Pipe was not escaped in Markdown table!")
                self.assertIn(r"Category \| Injection", line, "Escaped pipe not found!")

        self.assertTrue(found, "Injected category not found in report.")

    def test_newline_injection(self):
        """Test that newlines in data do not break Markdown table rows."""

        # Malicious data containing newlines
        data = [
            {
                "title": "Newline Post",
                "categories": ["Category\nSplit", "Normal"],
                "external_link": "https://example.com/page2",
                "author": "Hacker",
                "datetime": "2023-01-02T12:00:00"
            }
        ]

        # Generate report
        analytics.generate_report(data, self.output_file)

        # Read the report
        with open(self.output_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check that the newline was replaced
        # We search for the row containing "Category Split" (space instead of newline)
        found = False
        for line in content.splitlines():
            if "Category Split" in line:
                found = True
                self.assertNotIn("Category\nSplit", line, "Newline was not replaced!")

        self.assertTrue(found, "Sanitized newline category not found in report.")

if __name__ == '__main__':
    unittest.main()
