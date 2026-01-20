import unittest
import subprocess
import sys
import os
import json

class TestAnalyticsSecurity(unittest.TestCase):
    def setUp(self):
        self.malicious_data = [
            {
                "title": "Normal Title",
                "date": "2023-10-27",
                "author": "<script>alert('XSS')</script>",
                "categories": ["<b>Bold Category</b>|Pipe"],
                "external_link": "http://example.com",
                "domain": "example.com",
                "post_url": "http://example.com/post1",
                "datetime": "2023-10-27T10:00:00"
            }
        ]
        self.input_file = 'test_malicious.json'
        self.output_file = 'test_report.md'

        with open(self.input_file, 'w') as f:
            json.dump(self.malicious_data, f)

    def tearDown(self):
        if os.path.exists(self.input_file):
            os.remove(self.input_file)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_xss_prevention(self):
        # Run analytics.py
        # Assuming analytics.py is in the parent directory or current directory depending on where test is run
        # We'll try to locate it relative to this file

        script_path = os.path.join(os.path.dirname(__file__), '..', 'analytics.py')
        if not os.path.exists(script_path):
             script_path = 'analytics.py'

        result = subprocess.run(
            [sys.executable, script_path, "--input", self.input_file, "--output", self.output_file],
            capture_output=True,
            text=True
        )

        self.assertEqual(result.returncode, 0, f"Script failed: {result.stderr}")

        with open(self.output_file, 'r') as f:
            content = f.read()

        # Check for escaped XSS
        self.assertIn("&lt;script&gt;alert(&#x27;XSS&#x27;)&lt;/script&gt;", content, "XSS script tag not escaped")

        # Check for escaped HTML
        self.assertIn("&lt;b&gt;Bold Category&lt;/b&gt;", content, "HTML tag not escaped")

        # Check for escaped pipe
        self.assertIn(r"\|Pipe", content, "Pipe not escaped")

if __name__ == '__main__':
    unittest.main()
