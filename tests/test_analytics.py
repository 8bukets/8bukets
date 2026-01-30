import unittest
import sys
import os

# Add parent directory to path so we can import analytics
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# We will need to mock generate_markdown_content if it doesn't exist yet,
# but for TDD we assume it will exist.
# However, to avoid import errors preventing me from running other things,
# I will import it inside the test or just fail if not present.
# Actually, I'll just assume I'll add it.

try:
    from analytics import generate_markdown_content
except ImportError:
    generate_markdown_content = None

class TestAnalytics(unittest.TestCase):
    def test_report_structure(self):
        if generate_markdown_content is None:
            self.fail("generate_markdown_content not found in analytics.py")

        data = [
            {
                "title": "Test Post",
                "datetime": "2025-01-01T12:00:00",
                "author": "Test Author",
                "categories": ["Test Cat"],
                "external_link": "https://example.com"
            }
        ]

        md = generate_markdown_content(data)

        # Check for TOC
        self.assertIn("## Table of Contents", md)
        self.assertIn("<a name='table-of-contents'></a>", md)

        # Check for Anchors (checking one example)
        # Note: The exact slug implementation might vary, so I'll check for the anchor tag presence
        self.assertIn("<a name=", md)

        # Check for Back to Top
        self.assertIn("[Back to Top](#table-of-contents)", md)

        # Check for Emojis
        self.assertIn("📊 General Statistics", md)

if __name__ == '__main__':
    unittest.main()
