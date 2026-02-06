import unittest
import os
from analytics import create_ascii_bar, generate_report

class TestAnalyticsUX(unittest.TestCase):

    def test_create_ascii_bar_full(self):
        # 10/10 -> 100% -> "▓" * 15
        bar = create_ascii_bar(10, 10, width=15)
        self.assertEqual(bar, "▓" * 15)

    def test_create_ascii_bar_half(self):
        # 5/10 -> 50% -> 7 "▓" and 8 "░" (int(7.5) = 7)
        bar = create_ascii_bar(5, 10, width=15)
        self.assertEqual(bar, "▓" * 7 + "░" * 8)

    def test_create_ascii_bar_zero(self):
        bar = create_ascii_bar(0, 10, width=15)
        self.assertEqual(bar, "░" * 15)

    def test_create_ascii_bar_small_positive(self):
        # Should have at least one block if > 0
        bar = create_ascii_bar(1, 1000, width=15)
        self.assertEqual(bar, "▓" + "░" * 14)

    def test_create_ascii_bar_empty_total(self):
        bar = create_ascii_bar(5, 0, width=15)
        self.assertEqual(bar, "░" * 15)

    def test_generate_report_integration(self):
        test_data = [
            {
                "external_link": "https://example.com/foo",
                "categories": ["CatA"],
                "datetime": "2022-01-01T12:00:00",
                "author": "Author1"
            },
            {
                "external_link": "https://example.com/bar",
                "categories": ["CatA", "CatB"],
                "datetime": "2021-01-01T12:00:00",
                "author": "Author1"
            }
        ]
        output_file = "TEST_REPORT.md"
        generate_report(test_data, output_file)

        self.assertTrue(os.path.exists(output_file))

        with open(output_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for distribution column
        self.assertIn("| Distribution |", content)
        # Check for ASCII blocks
        self.assertIn("▓", content)
        # Check for example.com
        self.assertIn("example.com", content)

        # Cleanup
        os.remove(output_file)

if __name__ == '__main__':
    unittest.main()
