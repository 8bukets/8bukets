import unittest
from analytics import draw_bar

class TestAnalytics(unittest.TestCase):
    def test_draw_bar_empty(self):
        self.assertEqual(draw_bar(0, 0, width=10), "░" * 10)

    def test_draw_bar_full(self):
        self.assertEqual(draw_bar(100, 100, width=10), "█" * 10)

    def test_draw_bar_half(self):
        self.assertEqual(draw_bar(50, 100, width=10), "█" * 5 + "░" * 5)

    def test_draw_bar_zero_max(self):
        self.assertEqual(draw_bar(10, 0, width=10), "░" * 10)

if __name__ == '__main__':
    unittest.main()
