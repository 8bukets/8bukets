import unittest
import json
import os
from analytics import generate_report, get_domain
from datetime import datetime

class TestDomainExtraction(unittest.TestCase):
    def test_standard_urls(self):
        self.assertEqual(get_domain("https://www.example.com/path"), "example.com")
        self.assertEqual(get_domain("http://example.com"), "example.com")
        self.assertEqual(get_domain("https://sub.domain.co.uk/"), "sub.domain.co.uk")

    def test_ports(self):
        self.assertEqual(get_domain("http://example.com:8080/path"), "example.com")
        self.assertEqual(get_domain("https://localhost:3000"), "localhost")

    def test_auth(self):
        self.assertEqual(get_domain("https://user:pass@example.com/path"), "example.com")
        self.assertEqual(get_domain("https://user@example.com/path"), "example.com")

    def test_no_scheme(self):
        self.assertEqual(get_domain("www.example.com/path"), "example.com")
        self.assertEqual(get_domain("example.com"), "example.com")

    def test_protocol_relative(self):
        self.assertEqual(get_domain("//example.com/path"), "example.com")

    def test_empty_none(self):
        self.assertIsNone(get_domain(None))
        self.assertIsNone(get_domain(""))

class TestAnalyticsReport(unittest.TestCase):
    def setUp(self):
        self.test_data = [
            {
                "external_link": "https://example.com/post1",
                "categories": ["Tech", "News"],
                "datetime": "2023-01-01T10:00:00",
                "author": "Alice"
            },
            {
                "external_link": "https://example.com/post2",
                "categories": ["Tech"],
                "datetime": "2023-01-02T10:00:00",
                "author": "Bob"
            },
            {
                "external_link": "https://other.com/post3",
                "categories": ["News"],
                "datetime": "2023-02-01T10:00:00",
                "author": "Alice"
            },
            {
                "external_link": None,
                "categories": [],
                "datetime": None,
                "author": None
            }
        ]
        self.output_file = "TEST_REPORT_FINAL.md"

    def tearDown(self):
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_report_content(self):
        generate_report(self.test_data, self.output_file)

        with open(self.output_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check total posts
        self.assertIn("Total Posts:** 4", content)

        # Check domains
        self.assertIn("| example.com | 2 |", content)
        self.assertIn("| other.com | 1 |", content)

        # Check categories
        self.assertIn("| Tech | 2 |", content)
        self.assertIn("| News | 2 |", content)

        # Check authors
        self.assertIn("- Alice: 2 posts", content)
        self.assertIn("- Bob: 1 posts", content)

        # Check years (all 2023)
        self.assertIn("| 2023 | 3 |", content)

if __name__ == '__main__':
    unittest.main()
