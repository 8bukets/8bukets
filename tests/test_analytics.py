import unittest
import json
import os
from analytics import get_domain, generate_report

class TestAnalytics(unittest.TestCase):
    def setUp(self):
        self.test_data = [
            {
                "title": "Post 1",
                "date": "2023-01-01",
                "datetime": "2023-01-01T10:00:00+00:00",
                "author": "Author A",
                "categories": ["Cat A", "Cat B"],
                "external_link": "https://www.example.com/page",
                "domain": "example.com"
            },
            {
                "title": "Post 2",
                "date": "2023-01-02",
                "datetime": "2023-01-02T10:00:00+00:00",
                "author": "Author B",
                "categories": ["Cat A"],
                "external_link": "https://sub.test.org/path",
                "domain": "sub.test.org"
            }
        ]
        self.output_file = "test_report.md"

    def tearDown(self):
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_get_domain(self):
        self.assertEqual(get_domain("https://www.google.com"), "google.com")
        self.assertEqual(get_domain("http://sub.domain.co.uk/path"), "sub.domain.co.uk")
        self.assertIsNone(get_domain(None))
        self.assertIsNone(get_domain("not a url"))

    def test_generate_report_creates_file(self):
        generate_report(self.test_data, self.output_file)
        self.assertTrue(os.path.exists(self.output_file))

        with open(self.output_file, 'r') as f:
            content = f.read()
            self.assertIn("# 📊 Wordpress Blog Analytics Report", content)
            self.assertIn("Author A", content)
            self.assertIn("Cat A", content)
            self.assertIn("example.com", content)

if __name__ == '__main__':
    unittest.main()
