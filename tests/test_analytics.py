import unittest
import sys
import os

# Add parent directory to path to import analytics
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from analytics import sanitize_markdown

class TestAnalyticsSecurity(unittest.TestCase):
    def test_sanitize_markdown_basic(self):
        self.assertEqual(sanitize_markdown("Hello"), "Hello")
        self.assertEqual(sanitize_markdown("123"), "123")
        self.assertEqual(sanitize_markdown(None), "")

    def test_sanitize_markdown_pipes(self):
        # Pipes should be escaped
        self.assertEqual(sanitize_markdown("Hello | World"), "Hello \| World")
        self.assertEqual(sanitize_markdown("|Start"), "\|Start")
        self.assertEqual(sanitize_markdown("End|"), "End\|")

    def test_sanitize_markdown_html(self):
        # HTML tags should be escaped
        self.assertEqual(sanitize_markdown("<script>"), "&lt;script&gt;")
        self.assertEqual(sanitize_markdown("<b>Bold</b>"), "&lt;b&gt;Bold&lt;/b&gt;")

    def test_sanitize_markdown_mixed(self):
        # Mixed malicious input
        input_str = "<script> | "
        expected = "&lt;script&gt; \| "
        self.assertEqual(sanitize_markdown(input_str), expected)

if __name__ == '__main__':
    unittest.main()
