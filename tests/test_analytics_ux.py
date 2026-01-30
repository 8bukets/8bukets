import unittest
import os
import tempfile
import json
from analytics import generate_report

class TestAnalyticsUX(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()
        self.output_file = os.path.join(self.test_dir.name, 'TEST_REPORT.md')

        self.sample_data = [
            {
                "external_link": "https://example.com/post1",
                "categories": ["Tech"],
                "datetime": "2023-01-01T12:00:00",
                "author": "Alice"
            },
            {
                "external_link": "https://google.com/search",
                "categories": ["Search"],
                "datetime": "2023-01-02T12:00:00",
                "author": "Bob"
            }
        ]

    def tearDown(self):
        self.test_dir.cleanup()

    def test_report_ux_elements(self):
        generate_report(self.sample_data, self.output_file)

        with open(self.output_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for Table of Contents
        self.assertIn("Table of Contents", content)
        self.assertIn("<a name='table-of-contents'></a>", content)

        # Check for Emojis in headers
        self.assertIn("📈 General Statistics", content)
        self.assertIn("🌐 Top 10 Referenced Domains", content)

        # Check for Anchors
        self.assertIn("<a name='general-statistics'></a>", content)

        # Check for Back to Top links
        self.assertIn("[Back to Top](#table-of-contents)", content)

if __name__ == '__main__':
    unittest.main()
