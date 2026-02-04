import unittest
import analytics
import os

class TestAnalyticsSecurity(unittest.TestCase):
    def setUp(self):
        self.output_file = "REPORT_TEST_SEC.md"
        self.data = [
            {
                "title": "Post 1",
                "date": "2023-01-01",
                "datetime": "2023-01-01T12:00:00",
                "author": "Malicious | Author",
                "categories": ["<b>Bold</b>", "Table | Breaker"],
                "external_link": "http://example.com",
                "domain": "example.com"
            },
            {
                "title": "Post 2",
                "date": "2023-01-02",
                "datetime": "2023-01-02T12:00:00",
                "author": "<script>alert('XSS')</script>",
                "categories": ["Normal"],
                "external_link": "http://evil.com",
                "domain": "evil.com"
            }
        ]

    def tearDown(self):
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_markdown_sanitization(self):
        analytics.generate_report(self.data, self.output_file)

        with open(self.output_file, 'r') as f:
            content = f.read()

        # Check Author Sanitization
        self.assertNotIn("Malicious | Author", content)
        self.assertIn("Malicious &#124; Author", content)

        self.assertNotIn("<script>", content)
        self.assertIn("&lt;script&gt;", content)

        # Check Category Sanitization
        self.assertNotIn("| Table | Breaker |", content) # This would be the broken table row
        self.assertIn("Table &#124; Breaker", content)
        self.assertIn("&lt;b&gt;Bold&lt;/b&gt;", content)

if __name__ == '__main__':
    unittest.main()
