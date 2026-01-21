import unittest
import os
import json
from analytics import sanitize_markdown, generate_report

class TestSecurity(unittest.TestCase):
    def test_sanitize_markdown(self):
        """Test that Markdown special characters and HTML are sanitized."""
        self.assertEqual(sanitize_markdown("Normal Text"), "Normal Text")
        self.assertEqual(sanitize_markdown("<b>Bold</b>"), "&lt;b&gt;Bold&lt;/b&gt;")
        self.assertEqual(sanitize_markdown("Pipe | Character"), r"Pipe \| Character")
        self.assertEqual(sanitize_markdown("<script>alert(1)</script>"), "&lt;script&gt;alert(1)&lt;/script&gt;")

    def test_report_generation_injection(self):
        """Test report generation with malicious input."""
        test_data = [
            {
                "title": "Test",
                "categories": ["Cloud | Injection", "<script>alert(1)</script>"],
                "author": "Hacker | Admin",
                "datetime": "2023-01-01T12:00:00"
            }
        ]
        output_file = "TEST_SECURITY_REPORT.md"
        try:
            generate_report(test_data, output_file)

            with open(output_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Verify sanitization in output
            self.assertIn(r"Cloud \| Injection", content)
            self.assertIn("&lt;script&gt;alert(1)&lt;/script&gt;", content)
            self.assertIn(r"Hacker \| Admin", content)
        finally:
            if os.path.exists(output_file):
                os.remove(output_file)

if __name__ == '__main__':
    unittest.main()
