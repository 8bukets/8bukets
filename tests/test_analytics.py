import unittest
import os
import json
from analytics import create_ascii_bar, generate_report

class TestAnalytics(unittest.TestCase):
    def test_create_ascii_bar_full(self):
        # 10/10 with length 10 -> 10 chars
        bar = create_ascii_bar(10, 10, length=10)
        self.assertEqual(bar, "██████████")

    def test_create_ascii_bar_half(self):
        # 5/10 with length 10 -> 5 chars
        bar = create_ascii_bar(5, 10, length=10)
        self.assertEqual(bar, "█████")

    def test_create_ascii_bar_zero_max(self):
        bar = create_ascii_bar(5, 0)
        self.assertEqual(bar, "")

    def test_create_ascii_bar_zero_count(self):
        bar = create_ascii_bar(0, 10)
        self.assertEqual(bar, "")

    def test_create_ascii_bar_custom_length(self):
        # 1/2 with length 4 -> 2 chars
        bar = create_ascii_bar(1, 2, length=4)
        self.assertEqual(bar, "██")

    def test_generate_report_integration(self):
        # Create a temporary input file
        input_data = [
            {"external_link": "https://a.com", "categories": ["Cat1"], "datetime": "2023-01-01T00:00:00"},
            {"external_link": "https://a.com", "categories": ["Cat1"], "datetime": "2023-01-01T00:00:00"},
            {"external_link": "https://b.com", "categories": ["Cat2"], "datetime": "2022-01-01T00:00:00"}
        ]
        input_file = "test_integration_input.json"
        output_file = "test_integration_report.md"

        with open(input_file, 'w') as f:
            json.dump(input_data, f)

        try:
            generate_report(input_data, output_file)

            self.assertTrue(os.path.exists(output_file))
            with open(output_file, 'r') as f:
                content = f.read()

            # Check for bar chart elements
            self.assertIn("| Distribution |", content)
            self.assertIn("██", content) # Should have bars
            self.assertIn("a.com", content)
            self.assertIn("b.com", content)

        finally:
            # Cleanup
            if os.path.exists(input_file):
                os.remove(input_file)
            if os.path.exists(output_file):
                os.remove(output_file)

if __name__ == '__main__':
    unittest.main()
