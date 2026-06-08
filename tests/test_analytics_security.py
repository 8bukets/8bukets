import unittest
import json
import os
import sys
import tempfile
from analytics import escape_markdown, generate_report

class TestAnalyticsSecurity(unittest.TestCase):
    def test_escape_markdown(self):
        self.assertEqual(escape_markdown("Safe"), "Safe")
        self.assertEqual(escape_markdown("Pipe | Test"), "Pipe &#124; Test")
        self.assertEqual(escape_markdown("<script>"), "&lt;script&gt;")
        self.assertEqual(escape_markdown("Mixed | <tag>"), "Mixed &#124; &lt;tag&gt;")
        self.assertEqual(escape_markdown(None), "")

    def test_generate_report_sanitization(self):
        # Create a temporary output file
        with tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8') as tmp:
            output_file = tmp.name

        try:
            data = [
                {
                    "title": "Test",
                    "date": "2023-01-01",
                    "datetime": "2023-01-01T00:00:00",
                    "author": "Hacker <script>",
                    "categories": ["Malicious | Category"],
                    "external_link": "http://evil.com/foo",
                    "domain": "ignored",
                    "post_url": "http://example.com"
                }
            ]

            generate_report(data, output_file)

            with open(output_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Verify Author sanitization
            self.assertIn("Hacker &lt;script&gt;", content)
            self.assertNotIn("Hacker <script>", content)

            # Verify Category sanitization in table
            self.assertIn("| Malicious &#124; Category |", content)
            self.assertNotIn("| Malicious | Category |", content)

        finally:
            if os.path.exists(output_file):
                os.remove(output_file)

if __name__ == '__main__':
    unittest.main()
