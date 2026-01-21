import unittest
import os
import json
import analytics

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
        self.input_file = "test_links.json"
        self.output_file = "TEST_REPORT.md"

        with open(self.input_file, 'w') as f:
            json.dump(self.test_data, f)

    def tearDown(self):
        if os.path.exists(self.input_file):
            os.remove(self.input_file)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_report_content(self):
        # Run the generator
        analytics.generate_report(self.test_data, self.output_file)

        with open(self.output_file, 'r') as f:
            content = f.read()

        # Check for UX Enhancements

        # 1. Table of Contents existence
        self.assertIn("## Table of Contents", content)
        self.assertIn("- [General Statistics](#general-statistics)", content)

        # 2. Emojis in headers
        self.assertIn("## 📊 General Statistics", content)
        self.assertIn("## 🌐 Top 10 Referenced Domains", content)

        # 3. HTML Anchors
        self.assertIn('<a name="general-statistics"></a>', content)
        self.assertIn('<a name="top"></a>', content)

        # 4. Back to Top links
        self.assertIn("[Back to Top](#top)", content)

        # 5. Number formatting (simulated check, though small numbers won't show commas)
        # We can check if basic structure is maintained
        self.assertIn("| example.com | 1 |", content)

if __name__ == '__main__':
    unittest.main()
