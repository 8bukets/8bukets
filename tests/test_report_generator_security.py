import unittest
import json
import os
import sys
from unittest.mock import patch, mock_open

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from analytics import generate_report

class TestReportGeneratorSecurity(unittest.TestCase):
    def setUp(self):
        self.malicious_data = [
            {
                "title": "Malicious Post",
                "date": "2023-10-01",
                "datetime": "2023-10-01T12:00:00",
                "author": "<script>alert('XSS')</script>",
                "categories": ["Cat | 1", "Normal"],
                "external_link": "https://example.com/malicious",
                "domain": "example.com",
                "post_url": "https://markposition.wordpress.com/post1"
            },
            {
                "title": "Safe Post",
                "date": "2023-10-02",
                "datetime": "2023-10-02T12:00:00",
                "author": "Alice",
                "categories": ["Tech"],
                "external_link": "https://google.com",
                "domain": "google.com",
                "post_url": "https://markposition.wordpress.com/post2"
            }
        ]
        self.output_file = "TEST_REPORT.md"

    def tearDown(self):
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_markdown_injection_and_xss(self):
        """
        Test that pipe characters and HTML tags are escaped.
        """
        generate_report(self.malicious_data, self.output_file)

        with open(self.output_file, 'r', encoding='utf-8') as f:
            content = f.read()

        print("\n--- Generated Report Content ---")
        print(content)
        print("--------------------------------")

        # 1. Check for Broken Table Structure
        lines = content.split('\n')
        table_started = False
        broken_row_found = False

        for line in lines:
            if "| Domain | Count |" in line or "| Category | Count |" in line or "| Year | Count |" in line:
                table_started = True
                continue

            if table_started:
                if not line.strip().startswith('|'):
                    if line.strip() == "": continue
                    table_started = False
                else:
                    if ":---" in line: continue
                    pipe_count = line.count('|')
                    if pipe_count > 3:
                        broken_row_found = True
                        print(f"Broken row detected: {line}")

        self.assertFalse(broken_row_found, "Markdown table structure is broken by injected pipes!")

        # 2. Check for XSS
        # The author "<script>alert('XSS')</script>" should be escaped to "&lt;script&gt;alert(&#x27;XSS&#x27;)&lt;/script&gt;"
        self.assertNotIn("<script>", content, "XSS vector found in report (unclosed script tag)!")
        self.assertIn("&lt;script&gt;", content, "Script tag was not correctly escaped!")

if __name__ == '__main__':
    unittest.main()
