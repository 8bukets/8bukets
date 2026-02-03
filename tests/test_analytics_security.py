import unittest
import os
import sys
import json

# Add parent directory to path so we can import analytics
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import analytics

class TestAnalyticsSecurity(unittest.TestCase):
    def setUp(self):
        self.test_output = "REPORT_TEST_SEC.md"
        self.malicious_data = [
            {
                "title": "Malicious Post",
                "date": "2023-01-01",
                "author": "Evil|Author",
                "categories": ["Cat|egory", "<script>alert(1)</script>"],
                "external_link": "https://malicious.com/post",
                "domain": "malicious.com",
                "post_url": "https://malicious.com/post"
            }
        ]

    def tearDown(self):
        if os.path.exists(self.test_output):
            os.remove(self.test_output)

    def test_markdown_injection(self):
        # Generate report
        analytics.generate_report(self.malicious_data, self.test_output)

        # Read report
        with open(self.test_output, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for escaped characters
        # Pipe should be escaped
        # We expect sanitization to happen, so raw malicious strings should NOT be present in a way that breaks markdown

        # Check Author
        self.assertIn("Evil&#124;Author", content, "Pipe in author should be escaped")

        # Check Category
        self.assertIn("Cat&#124;egory", content, "Pipe in category should be escaped")

        # Check HTML Injection
        self.assertIn("&lt;script&gt;", content, "HTML tags should be escaped")
        self.assertNotIn("<script>", content, "Raw HTML script tag found!")

if __name__ == '__main__':
    unittest.main()
