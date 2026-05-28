import unittest
import os
import tempfile
from analytics import create_ascii_bar, generate_report

class TestAnalyticsUX(unittest.TestCase):
    def test_create_ascii_bar(self):
        # Test full bar
        self.assertEqual(create_ascii_bar(10, 10, 10), "██████████")
        # Test empty bar
        self.assertEqual(create_ascii_bar(0, 10, 10), "░░░░░░░░░░")
        # Test half bar
        self.assertEqual(create_ascii_bar(5, 10, 10), "█████░░░░░")
        # Test default length (20)
        self.assertEqual(len(create_ascii_bar(5, 10)), 20)

    def test_generate_report_visuals(self):
        # Mock data
        data = [
            {"domain": "example.com", "categories": ["Tech"], "datetime": "2023-01-01T12:00:00", "author": "Alice", "external_link": "https://example.com/1"},
            {"domain": "example.com", "categories": ["Tech"], "datetime": "2023-01-02T12:00:00", "author": "Alice", "external_link": "https://example.com/2"},
            {"domain": "other.com", "categories": ["Life"], "datetime": "2022-01-01T12:00:00", "author": "Bob", "external_link": "https://other.com/1"},
        ]

        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as tmp:
            output_file = tmp.name

        try:
            generate_report(data, output_file)

            with open(output_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Check for bar chart characters
            self.assertIn("█", content)
            self.assertIn("Distribution", content)

        finally:
            if os.path.exists(output_file):
                os.remove(output_file)

if __name__ == "__main__":
    unittest.main()
