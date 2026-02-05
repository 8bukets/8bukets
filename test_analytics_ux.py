import unittest
import sys
import os

# Add current directory to path so we can import analytics
sys.path.append(os.getcwd())

try:
    from analytics import create_ascii_bar
except ImportError:
    # Function not implemented yet
    create_ascii_bar = None

class TestAnalyticsUX(unittest.TestCase):
    def test_create_ascii_bar_basic(self):
        if not create_ascii_bar:
            self.skipTest("create_ascii_bar not implemented yet")

        # 50% of 20 chars = 10 chars
        bar = create_ascii_bar(50, 100, 20)
        self.assertEqual(bar, "██████████          ")
        self.assertEqual(len(bar), 20)

    def test_create_ascii_bar_full(self):
        if not create_ascii_bar:
            self.skipTest("create_ascii_bar not implemented yet")

        bar = create_ascii_bar(100, 100, 10)
        self.assertEqual(bar, "██████████")

    def test_create_ascii_bar_empty(self):
        if not create_ascii_bar:
            self.skipTest("create_ascii_bar not implemented yet")

        bar = create_ascii_bar(0, 100, 10)
        self.assertEqual(bar, "          ")

    def test_create_ascii_bar_rounding(self):
        if not create_ascii_bar:
            self.skipTest("create_ascii_bar not implemented yet")

        # 33/100 * 10 = 3.3 -> 3
        bar = create_ascii_bar(33, 100, 10)
        self.assertEqual(bar, "███       ")

    def test_create_ascii_bar_zero_total(self):
        if not create_ascii_bar:
            self.skipTest("create_ascii_bar not implemented yet")

        # Should handle division by zero or empty list case gracefully
        bar = create_ascii_bar(10, 0, 10)
        self.assertEqual(bar, "          ")

if __name__ == '__main__':
    unittest.main()
