import unittest
import json
import os
import subprocess
import sys

class TestAnalyticsSecurity(unittest.TestCase):
    def setUp(self):
        self.input_file = 'test_links_sec.json'
        self.output_file = 'REPORT_SEC.md'

        # Malicious data
        self.data = [
            {
                "title": "Bad Post",
                "date": "2023-01-01",
                "datetime": "2023-01-01T00:00:00",
                "author": "<b>Hacker</b>",
                "categories": ["Malicious | Category"],
                "external_link": "http://evil.com/safe",
                "post_url": "http://example.com"
            }
        ]

        with open(self.input_file, 'w') as f:
            json.dump(self.data, f)

    def tearDown(self):
        if os.path.exists(self.input_file):
            os.remove(self.input_file)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_markdown_injection(self):
        # Run analytics.py
        result = subprocess.run(
            [sys.executable, 'analytics.py', '--input', self.input_file, '--output', self.output_file],
            capture_output=True,
            text=True
        )
        self.assertEqual(result.returncode, 0, "analytics.py failed to run")

        # Read the report
        with open(self.output_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for HTML injection in Author
        self.assertIn('&lt;b&gt;Hacker&lt;/b&gt;', content, "HTML in author name was not escaped!")

        # Check for Table Injection in Category
        # We expect 'Malicious \| Category'
        self.assertIn(r'Malicious \| Category', content, "Pipe in category was not escaped!")

if __name__ == '__main__':
    unittest.main()
