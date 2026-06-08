import unittest
import os
import sys
from analytics import generate_report

# Ensure we can import from root
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestAnalytics(unittest.TestCase):
    def setUp(self):
        self.test_data = [
            {
                "datetime": "2023-01-01T12:00:00",
                "external_link": "https://example.com",
                "categories": ["TestCategory"],
                "author": "Test Author"
            }
        ]
        self.output_file = "test_report.md"

    def tearDown(self):
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_report_ux_elements(self):
        generate_report(self.test_data, self.output_file)

        with open(self.output_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for Table of Contents
        self.assertIn("## 📑 Table of Contents", content)
        self.assertIn("<a name='table-of-contents'></a>", content)

        # Check for Anchors
        self.assertIn("<a name='general-statistics'></a>", content)
        self.assertIn("<a name='top-referenced-domains'></a>", content)

        # Check for Emojis in headers
        self.assertIn("## 📊 General Statistics", content)
        self.assertIn("## 🔗 Top 10 Referenced Domains", content)
        self.assertIn("## 🏷️ Top 10 Categories", content)
        self.assertIn("## 📅 Posts by Year", content)
        self.assertIn("## ✍️ Authors", content)

        # Check for Back to Top links
        self.assertIn("[Back to Top](#table-of-contents)", content)

if __name__ == '__main__':
    unittest.main()
