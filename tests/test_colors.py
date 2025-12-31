import unittest
from utils.colors import Colors

class TestColors(unittest.TestCase):
    def test_strip_ansi(self):
        text = "\033[94mHello\033[0m"
        clean = Colors.strip_ansi(text)
        self.assertEqual(clean, "Hello")

    def test_get_visible_length_simple(self):
        self.assertEqual(Colors.get_visible_length("Hello"), 5)

    def test_get_visible_length_ansi(self):
        text = "\033[94mHello\033[0m"
        self.assertEqual(Colors.get_visible_length(text), 5)

    def test_get_visible_length_emoji(self):
        # 🚀 is visually 2 chars.
        # Python len("🚀") is 1.
        # Our heuristic adds 1.
        self.assertEqual(Colors.get_visible_length("🚀"), 2)

        # ⏱️ is visually 2 chars.
        # Python len("⏱️") is 2.
        # Our heuristic adds 0.
        self.assertEqual(Colors.get_visible_length("⏱️"), 2)

        # Combined
        # "🚀 Hello" -> 2 + 1 + 5 = 8
        self.assertEqual(Colors.get_visible_length("🚀 Hello"), 8)

if __name__ == '__main__':
    unittest.main()
