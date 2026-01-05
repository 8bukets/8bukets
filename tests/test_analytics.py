import unittest
from analytics import draw_bar_chart

class TestAnalytics(unittest.TestCase):
    def test_draw_bar_chart_full(self):
        self.assertEqual(draw_bar_chart(10, 10), "██████████ 100%")

    def test_draw_bar_chart_half(self):
        self.assertEqual(draw_bar_chart(5, 10), "█████░░░░░ 50%")

    def test_draw_bar_chart_zero(self):
        self.assertEqual(draw_bar_chart(0, 10), "░░░░░░░░░░ 0%")

    def test_draw_bar_chart_empty_total(self):
        self.assertEqual(draw_bar_chart(5, 0), "")

    def test_draw_bar_chart_custom_width(self):
        self.assertEqual(draw_bar_chart(5, 10, width=4), "██░░ 50%")

if __name__ == '__main__':
    unittest.main()
