import unittest
import sys
import os

# Add parent directory to path so we can import analytics
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from analytics import generate_markdown_content

class TestAnalyticsSecurity(unittest.TestCase):
    def test_markdown_sanitization(self):
        # Malicious data
        data = [
            {
                "title": "Test Post",
                "date": "2023-01-01",
                "datetime": "2023-01-01T12:00:00",
                "author": "<script>alert('xss')</script>",
                "categories": ["Malicious | Category"],
                "external_link": "http://example.com",
                "post_url": "http://markposition.wordpress.com/post"
            }
        ]

        md_output = generate_markdown_content(data)

        # Check for Table Injection prevention in Categories
        # Expected: "Malicious \| Category"
        self.assertIn(r"Malicious \| Category", md_output)

        # Check Author XSS prevention
        # Expected: "&lt;script&gt;alert('xss')&lt;/script&gt;"
        self.assertIn("&lt;script&gt;alert('xss')&lt;/script&gt;", md_output)
        self.assertNotIn("<script>", md_output)

if __name__ == '__main__':
    unittest.main()
