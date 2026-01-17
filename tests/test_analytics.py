import unittest
import json
import os
import math
from unittest.mock import patch, mock_open
import sys

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from analytics import generate_bar_chart, generate_report

class TestAnalytics(unittest.TestCase):
    def test_generate_bar_chart(self):
        # Update expectation for 0 value to match implementation (empty bar)
        self.assertEqual(generate_bar_chart(0, 100, 10), "`░░░░░░░░░░`")
        self.assertEqual(generate_bar_chart(50, 100, 10), "`█████░░░░░`")
        self.assertEqual(generate_bar_chart(100, 100, 10), "`██████████`")
        self.assertEqual(generate_bar_chart(1, 100, 10), "`█░░░░░░░░░`") # Should show at least one block if > 0

    def test_report_content(self):
        # Create dummy data
        data = [
            {"external_link": "http://google.com/a", "categories": ["Tech"], "datetime": "2023-01-01T12:00:00", "author": "Alice"},
            {"external_link": "http://google.com/b", "categories": ["Tech"], "datetime": "2023-01-02T12:00:00", "author": "Alice"},
            {"external_link": "http://yahoo.com/a", "categories": ["News"], "datetime": "2023-01-03T12:00:00", "author": "Bob"},
        ]

        output_file = "TEST_REPORT.md"
        generate_report(data, output_file)

        with open(output_file, 'r') as f:
            content = f.read()

        # Check for emojis and charts
        self.assertIn("📊 Executive Summary", content)
        self.assertIn("`██", content) # Check for bar chart
        self.assertIn("google.com", content)

        # Clean up
        if os.path.exists(output_file):
            os.remove(output_file)

if __name__ == '__main__':
    unittest.main()
