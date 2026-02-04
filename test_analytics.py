import unittest
from analytics import sanitize_markdown

class TestAnalytics(unittest.TestCase):
    def test_sanitize_markdown(self):
        self.assertEqual(sanitize_markdown("Hello World"), "Hello World")
        self.assertEqual(sanitize_markdown("Hello|World"), "Hello&#124;World")
        self.assertEqual(sanitize_markdown("<b>Bold</b>"), "&lt;b&gt;Bold&lt;/b&gt;")
        self.assertEqual(sanitize_markdown(None), "")
        self.assertEqual(sanitize_markdown(123), "123")
        self.assertEqual(sanitize_markdown("Line\nBreak"), "Line Break")

if __name__ == '__main__':
    unittest.main()
