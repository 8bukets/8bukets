import unittest
import sys
import io
from analytics import Colors, create_bar_chart

class TestAnalyticsUX(unittest.TestCase):
    def test_colors_exist(self):
        self.assertTrue(hasattr(Colors, 'HEADER'))
        self.assertTrue(hasattr(Colors, 'BLUE'))
        self.assertTrue(hasattr(Colors, 'ENDC'))

    def test_create_bar_chart(self):
        # We need to simulate tty for colors to appear, or just check content
        # If tty is false (likely in test env), colors are empty strings

        # Test full bar
        chart = create_bar_chart("Test", 10, 10, width=10)
        self.assertIn("Test", chart)
        self.assertIn("██████████", chart)

        # Test half bar
        chart = create_bar_chart("Test", 5, 10, width=10)
        self.assertIn("█████░░░░░", chart)

        # Test zero bar
        chart = create_bar_chart("Test", 0, 10, width=10)
        self.assertIn("░░░░░░░░░░", chart)

    def test_create_bar_chart_zero_division(self):
        # Should not crash
        chart = create_bar_chart("Test", 0, 0, width=10)
        self.assertIn("Test", chart)

if __name__ == '__main__':
    unittest.main()
