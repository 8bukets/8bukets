import unittest
import json
import os
import tempfile
from analytics import generate_report

class TestAnalyticsSecurity(unittest.TestCase):
    def setUp(self):
        self.test_data = [
            {
                "external_link": "http://example.com",
                "categories": ["Category | With | Pipes", "Normal Category"],
                "datetime": "2023-01-01T12:00:00",
                "author": "Author | Malicious",
                "domain": "example.com"
            }
        ]
        self.tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".md")
        self.tmp_file.close()

    def tearDown(self):
        if os.path.exists(self.tmp_file.name):
            os.remove(self.tmp_file.name)

    def test_markdown_injection(self):
        """Test that pipes in data are escaped in the Markdown report."""
        generate_report(self.test_data, self.tmp_file.name)

        with open(self.tmp_file.name, 'r', encoding='utf-8') as f:
            content = f.read()

        # Verify that pipes are escaped in the category section
        # The category is "Category | With | Pipes"
        # In a markdown table, this should appear as "Category \| With \| Pipes"
        # If it is NOT escaped, it will be "Category | With | Pipes" which breaks the table

        # We expect the fix to have escaped pipes.
        # But this test is also used to verify the vulnerability if run before the fix (assertions would need to be adjusted or we check for failure).
        # To fail IF vulnerable, we check for the escaped version.

        # Check for escaped pipes in Category
        self.assertIn("Category \\| With \\| Pipes", content, "Pipes in categories should be escaped")

        # Check for escaped pipes in Domain if applicable (though domain parser usually handles this,
        # let's inject a malicious domain if possible, but get_domain parses it.
        # The author field is a better candidate for simple string injection.)

        # Check Author (note: authors are a list, not a table in current analytics.py, but let's check anyway)
        # Ah, looking at analytics.py:
        # md.append(f"- {author}: {count} posts")
        # So author is just a list item, not a table row. Pipes are fine there for structure,
        # but XSS might be a concern if viewed in HTML.
        # However, the table logic is definitely in Domain, Category, and Year sections.

        # Let's focus on Category table which is definitely vulnerable.
