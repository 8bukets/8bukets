import unittest
import json
import os
from analytics import get_domain, generate_report

class TestAnalytics(unittest.TestCase):
    def test_get_domain(self):
        self.assertEqual(get_domain('https://example.com/foo'), 'example.com')
        self.assertEqual(get_domain('http://www.test.org'), 'test.org')
        self.assertIsNone(get_domain(None))
        self.assertIsNone(get_domain(''))

    def test_generate_report_creates_file(self):
        # Create dummy data
        data = [
            {
                "title": "Test Post",
                "date": "July 20, 2023",
                "datetime": "2023-07-20T12:00:00+00:00",
                "author": "Test Author",
                "categories": ["Tech"],
                "external_link": "https://example.com/article",
                "domain": "example.com",
                "post_url": "https://markposition.wordpress.com/2023/07/20/test"
            }
        ]

        output_file = "TEST_REPORT.md"
        if os.path.exists(output_file):
            os.remove(output_file)

        generate_report(data, output_file)

        self.assertTrue(os.path.exists(output_file))

        # Cleanup
        if os.path.exists(output_file):
            os.remove(output_file)

if __name__ == '__main__':
    unittest.main()
