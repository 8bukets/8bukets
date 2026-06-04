import os
import unittest
# Import generate_report.
# Note: analytics.py is in the root, so we can import it directly if running from root.
from analytics import generate_report

class TestAnalyticsUX(unittest.TestCase):
    def setUp(self):
        self.test_output = "TEST_REPORT.md"
        self.dummy_data = [
            {
                "title": "Test Post 1",
                "date": "2022-01-01",
                "datetime": "2022-01-01T12:00:00",
                "author": "Test Author",
                "categories": ["Category A"],
                "domain": "example.com"
            },
            {
                "title": "Test Post 2",
                "date": "2022-01-02",
                "datetime": "2022-01-02T12:00:00",
                "author": "Test Author",
                "categories": ["Category B"],
                "domain": "example.org"
            }
        ]

    def tearDown(self):
        if os.path.exists(self.test_output):
            os.remove(self.test_output)

    def test_report_ux_elements(self):
        generate_report(self.dummy_data, self.test_output)

        with open(self.test_output, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for Table of Contents
        self.assertIn("## Table of Contents", content, "Table of Contents is missing")

        # Check for Emojis in headers
        self.assertIn("## 📊 General Statistics", content, "Emoji missing in General Statistics")
        self.assertIn("## 🔗 Top 10 Referenced Domains", content, "Emoji missing in Domains")
        self.assertIn("## 📂 Top 10 Categories", content, "Emoji missing in Categories")
        self.assertIn("## 📅 Posts by Year", content, "Emoji missing in Posts by Year")
        self.assertIn("## ✍️ Authors", content, "Emoji missing in Authors")

        # Check for Back to Top links
        self.assertIn("[Back to Top](#table-of-contents)", content, "Back to Top link missing")

if __name__ == '__main__':
    unittest.main()
