import unittest
import sys
import os
import tempfile
import json

# Add parent directory to path to import analytics
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import analytics

class TestAnalyticsSecurity(unittest.TestCase):
    def test_markdown_injection(self):
        # Create a temporary file for input data
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
            json.dump([
                {
                    "title": "Malicious Post",
                    "date": "2023-10-28",
                    "author": "Hacker|Admin",
                    "categories": ["Hacking|Good", "[Link](javascript:alert(1))"],
                    "external_link": "http://evil.com|break|table",
                    "datetime": "2023-10-28T10:00:00"
                }
            ], f)
            input_file = f.name

        # Create a temporary file for output report
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.md') as f:
            output_file = f.name

        try:
            # Run the report generation
            data = analytics.load_data(input_file)
            analytics.generate_report(data, output_file)

            # Read the output
            with open(output_file, 'r') as f:
                content = f.read()

            # Check for escaped characters
            # We expect evil.com\|break\|table
            self.assertIn(r"evil.com\|break\|table", content, "Pipe in domain should be escaped")

            # We expect Hacking\|Good
            self.assertIn(r"Hacking\|Good", content, "Pipe in category should be escaped")

            # We expect brackets to be escaped
            self.assertIn(r"\[Link\](javascript:alert(1))", content, "Brackets in category should be escaped")

            # We expect Hacker\|Admin
            self.assertIn(r"Hacker\|Admin", content, "Pipe in author should be escaped")

        finally:
            if os.path.exists(input_file):
                os.remove(input_file)
            if os.path.exists(output_file):
                os.remove(output_file)

if __name__ == '__main__':
    unittest.main()
