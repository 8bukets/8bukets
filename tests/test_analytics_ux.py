
import unittest
import os
import json
from unittest.mock import MagicMock
import sys

# Add root directory to path to import analytics
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from analytics import generate_bar, generate_report

class TestAnalyticsUX(unittest.TestCase):
    def test_generate_bar(self):
        # Test full bar
        self.assertEqual(generate_bar(100, 100, 10), '██████████')
        # Test empty bar
        self.assertEqual(generate_bar(0, 100, 10), '░░░░░░░░░░')
        # Test half bar
        self.assertEqual(generate_bar(50, 100, 10), '█████░░░░░')
        # Test zero max (division by zero prevention)
        self.assertEqual(generate_bar(10, 0, 10), '')

    def test_report_generation(self):
        # Create dummy data
        data = [
            {
                "external_link": "https://example.com/post1",
                "categories": ["Tech"],
                "datetime": "2023-01-01T10:00:00",
                "author": "Alice"
            },
            {
                "external_link": "https://example.com/post2",
                "categories": ["Tech"],
                "datetime": "2023-01-02T10:00:00",
                "author": "Bob"
            }
        ]

        output_file = "TEST_REPORT.md"
        generate_report(data, output_file)

        # Check if file created
        self.assertTrue(os.path.exists(output_file))

        with open(output_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for UX elements
        self.assertIn("📈 Markposition Analytics Report", content)
        self.assertIn("Executive Summary 📊", content)
        self.assertIn("| Distribution |", content) # Check for new column
        self.assertIn("█", content) # Check for ASCII bars

        # Cleanup
        if os.path.exists(output_file):
            os.remove(output_file)

if __name__ == '__main__':
    unittest.main()
