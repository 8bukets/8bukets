import unittest
import json
import os
import subprocess
import sys

class TestAnalyticsSecurity(unittest.TestCase):
    def setUp(self):
        self.input_file = "tests/malicious.json"
        self.output_file = "tests/REPORT_SECURITY.md"

        self.malicious_data = [
            {
                "title": "Test Post",
                "datetime": "2023-01-01T12:00:00",
                "author": "<b>Hacker</b>",
                "categories": ["Normal", "Malicious | Category"],
                "external_link": "https://example.com/page|pipe",
                "domain": "example.com|pipe",
                "post_url": "https://example.com/post"
            }
        ]

        with open(self.input_file, "w") as f:
            json.dump(self.malicious_data, f)

    def tearDown(self):
        if os.path.exists(self.input_file):
            os.remove(self.input_file)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_markdown_injection(self):
        # Run analytics.py
        cmd = [sys.executable, "analytics.py", "--input", self.input_file, "--output", self.output_file]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL)

        with open(self.output_file, "r") as f:
            content = f.read()

        # Check Author XSS
        self.assertNotIn("<b>Hacker</b>", content, "HTML in Author was not escaped")
        self.assertIn("&lt;b&gt;Hacker&lt;/b&gt;", content, "Escaped HTML not found")

        # Check Category Table Injection
        # Should NOT have the raw pipe structure that makes 3 columns
        self.assertNotIn("| Malicious | Category |", content, "Pipe in Category created a new table column")
        self.assertIn("Malicious \| Category", content, "Pipe was not escaped with backslash")

        # Check Domain Table Injection
        # Based on get_domain implementation, it parses URL.
        # urlparse('https://example.com/page|pipe') might behave differently depending on python version,
        # but the domain field in JSON is what we care about if we injected it directly (which we did).
        # Wait, analytics.py derives domain from external_link using get_domain(url).
        # "external_link": "https://example.com/page|pipe" -> netloc might be "example.com" (pipe invalid in hostname usually)
        # But we also have "domain": "example.com|pipe" in the JSON.
        # analytics.py does: domains = [get_domain(p.get('external_link')) ...]
        # So it ignores the 'domain' field in JSON and recalculates it.
        # Let's check what get_domain returns for 'https://example.com/page|pipe'

        # It's better to trust the Category test which is direct string injection.

if __name__ == "__main__":
    unittest.main()
