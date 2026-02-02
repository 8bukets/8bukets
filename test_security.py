import unittest
import json
import os
import analytics

class TestSecurity(unittest.TestCase):
    def setUp(self):
        self.test_json = 'security_test_data.json'
        self.test_report = 'SECURITY_REPORT.md'

        # Malicious data
        self.data = [
            {
                "title": "Safe Post",
                "date": "2023-01-01",
                "datetime": "2023-01-01T12:00:00",
                "author": "Safe Author",
                "categories": ["Safe Cat"],
                "external_link": "https://safe.com",
            },
            {
                "title": "Unsafe Post",
                "date": "2023-01-02",
                "datetime": "2023-01-02T12:00:00",
                "author": "<b>Hacker</b>",
                "categories": ["Cat|Injection", "<script>alert(1)</script>"],
                "external_link": "https://evil.com|pipe",
            }
        ]

        with open(self.test_json, 'w') as f:
            json.dump(self.data, f)

    def tearDown(self):
        if os.path.exists(self.test_json):
            os.remove(self.test_json)
        if os.path.exists(self.test_report):
            os.remove(self.test_report)

    def test_markdown_injection(self):
        # Generate report
        analytics.generate_report(self.data, self.test_report)

        # Read report
        with open(self.test_report, 'r') as f:
            content = f.read()

        print("\n--- Generated Report Content (Snippet) ---\n")
        print(content)
        print("\n------------------------------------------\n")

        # Assertions
        # 1. Pipes in categories should be escaped
        self.assertNotIn('Cat|Injection', content, "Pipe char in category was not escaped (Table Injection Vulnerability)")
        self.assertIn('Cat&#124;Injection', content, "Pipe char in category was not correctly escaped")

        # 2. Scripts in categories should be escaped
        self.assertNotIn('<script>', content, "HTML script tag in category was not escaped (XSS Vulnerability)")
        self.assertIn('&lt;script&gt;', content, "HTML script tag in category was not correctly escaped")

        # 3. Pipes in domains should be escaped
        self.assertNotIn('evil.com|pipe', content, "Pipe char in domain was not escaped (Table Injection Vulnerability)")
        self.assertIn('evil.com&#124;pipe', content, "Pipe char in domain was not correctly escaped")

        # 4. HTML in authors should be escaped
        self.assertNotIn('<b>Hacker</b>', content, "HTML tag in author was not escaped")
        self.assertIn('&lt;b&gt;Hacker&lt;/b&gt;', content, "HTML tag in author was not correctly escaped")

if __name__ == '__main__':
    unittest.main()
