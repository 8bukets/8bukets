import unittest
import os
import tempfile
import json
from analytics import generate_report

class TestAnalyticsSecurity(unittest.TestCase):
    def setUp(self):
        self.test_file = 'TEST_REPORT_SEC.md'

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_xss_mitigation(self):
        # Malicious data
        data = [{
            "title": "Title",
            "datetime": "2023-01-01T12:00:00",
            "author": "<script>alert('XSS')</script>",
            "categories": ["<b>Bold</b>", "Cat|Pipe"],
            "external_link": "http://example.com",
            "domain": "example.com",
            "post_url": "http://example.com"
        }]

        generate_report(data, self.test_file)

        with open(self.test_file, 'r') as f:
            content = f.read()

        # Assertion: Vulnerability IS FIXED
        self.assertNotIn("<script>", content, "Raw script tag should not be present")
        self.assertIn("&lt;script&gt;", content, "Script tag should be HTML escaped")

        self.assertNotIn("<b>Bold</b>", content, "Raw HTML tag should not be present")
        self.assertIn("&lt;b&gt;Bold&lt;/b&gt;", content, "HTML tag should be escaped")

        # Pipe should be escaped: "Cat|Pipe" -> "Cat\|Pipe"
        # We look for the exact string in the file.
        self.assertIn(r"Cat\|Pipe", content, "Pipe should be escaped with backslash")

if __name__ == '__main__':
    unittest.main()
