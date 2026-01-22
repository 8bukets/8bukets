import unittest
import os
import json
import tempfile
import sys

# Add root directory to sys.path to import analytics
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import analytics

class TestSecurity(unittest.TestCase):
    def setUp(self):
        self.test_data = [
            {
                "title": "Malicious Post",
                "date": "2024-01-01",
                "datetime": "2024-01-01T12:00:00",
                "author": "Hacker | Evil <script>",
                "categories": ["Normal", "Malicious | Category"],
                "external_link": "http://example.com",
                "domain": "example.com",
                "post_url": "http://markposition.wordpress.com/post1"
            }
        ]
        # Use mkstemp for secure temporary file creation
        self.output_fd, self.output_file = tempfile.mkstemp()
        os.close(self.output_fd)

    def tearDown(self):
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_markdown_injection(self):
        # Run the report generation
        analytics.generate_report(self.test_data, self.output_file)

        # Read the result
        with open(self.output_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check that pipes are escaped
        self.assertIn("Malicious \\| Category", content, "Category name containing pipe was not escaped")
        # Check that HTML is escaped
        self.assertIn("&lt;script&gt;", content, "HTML tags in author name were not escaped")

if __name__ == '__main__':
    unittest.main()
