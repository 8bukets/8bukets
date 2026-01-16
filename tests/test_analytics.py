import unittest
from analytics import escape_markdown

class TestAnalytics(unittest.TestCase):
    def test_escape_markdown(self):
        self.assertEqual(escape_markdown("Normal Text"), "Normal Text")
        self.assertEqual(escape_markdown("Text|With|Pipes"), "Text\\|With\\|Pipes")
        self.assertEqual(escape_markdown("<script>alert(1)</script>"), "&lt;script&gt;alert(1)&lt;/script&gt;")
        self.assertEqual(escape_markdown("Line\nBreak"), "Line Break")
        self.assertEqual(escape_markdown(123), "123")
        self.assertEqual(escape_markdown(None), "None")

if __name__ == '__main__':
    unittest.main()
