import unittest
import os
import json
from unittest.mock import patch, mock_open
import analytics
from datetime import datetime

class TestAnalyticsUX(unittest.TestCase):
    def setUp(self):
        self.test_data = [
            {
                "external_link": "https://example.com/page1",
                "categories": ["Tech", "News"],
                "datetime": "2023-01-01T12:00:00",
                "author": "Alice"
            },
            {
                "external_link": "https://example.org/page2",
                "categories": ["Tech"],
                "datetime": "2023-02-01T12:00:00",
                "author": "Bob"
            }
        ]
        self.output_file = "TEST_REPORT.md"

    def tearDown(self):
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_report_content_ux(self):
        """Test that the generated report contains UX enhancements."""
        analytics.generate_report(self.test_data, self.output_file)

        with open(self.output_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for Emojis
        self.assertIn("# 📊 Wordpress Blog Analytics Report", content)
        self.assertIn("## 📈 General Statistics", content)
        self.assertIn("## 🔗 Top 10 Referenced Domains", content)
        self.assertIn("## 🏷️ Top 10 Categories", content)
        self.assertIn("## 📑 Full Data (Collapsible)", content)
        self.assertIn("## 📅 Posts by Year", content)
        self.assertIn("## ✍️ Authors", content)

        # Check for Collapsible Sections
        self.assertIn("<details>", content)
        self.assertIn("<summary><strong>View All Domains</strong></summary>", content)
        self.assertIn("<summary><strong>View All Categories</strong></summary>", content)
        self.assertIn("</details>", content)

        # Check Data Content
        self.assertIn("example.com", content)
        self.assertIn("Tech", content)

if __name__ == '__main__':
    unittest.main()
