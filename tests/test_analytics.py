import unittest
import sys
import os
from datetime import datetime

# Add root directory to path so we can import analytics
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import analytics

class TestAnalyticsUX(unittest.TestCase):
    def setUp(self):
        self.sample_data = [
            {
                "title": "Test Post",
                "date": "2023-01-01",
                "datetime": "2023-01-01T12:00:00+00:00",
                "author": "Tester",
                "categories": ["TestCat"],
                "external_link": "https://example.com/foo",
                "domain": "example.com"
            },
            {
                "title": "Another Post",
                "date": "2023-01-02",
                "datetime": "2023-01-02T12:00:00+00:00",
                "author": "Tester",
                "categories": ["TestCat"],
                "external_link": "https://google.com/bar",
                "domain": "google.com"
            }
        ]

    def test_markdown_structure(self):
        # This function doesn't exist yet, but will be added
        if not hasattr(analytics, 'generate_markdown_content'):
            self.fail("generate_markdown_content not implemented yet")

        md = analytics.generate_markdown_content(self.sample_data)

        # 1. Check for Table of Contents
        self.assertIn("# Table of Contents", md)
        self.assertIn("<a name='table-of-contents'></a>", md)

        # Check that TOC links exist
        self.assertIn("[General Statistics 📊](#stats)", md)

        # 2. Check for Emojis in Headers and Explicit Anchors
        self.assertIn("<a name='stats'></a>", md)
        self.assertIn("## General Statistics 📊", md)

        self.assertIn("<a name='domains'></a>", md)
        self.assertIn("## Top 10 Referenced Domains 🔗", md)

        # 3. Check for Back to Top links
        self.assertIn("[Back to Top](#table-of-contents)", md)

if __name__ == '__main__':
    unittest.main()
