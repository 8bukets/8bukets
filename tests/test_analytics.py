import unittest
import sys
import os

# Add parent directory to path to import analytics
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from analytics import sanitize_markdown

class TestAnalytics(unittest.TestCase):
    def test_sanitize_markdown_basic(self):
        self.assertEqual(sanitize_markdown("Hello World"), "Hello World")

    def test_sanitize_markdown_pipes(self):
        self.assertEqual(sanitize_markdown("Hello|World"), "Hello\|World")
        self.assertEqual(sanitize_markdown("|Start"), "\|Start")
        self.assertEqual(sanitize_markdown("End|"), "End\|")

    def test_sanitize_markdown_html(self):
        self.assertEqual(sanitize_markdown("<script>"), "&lt;script&gt;")
        self.assertEqual(sanitize_markdown("<b>Bold</b>"), "&lt;b&gt;Bold&lt;/b&gt;")

    def test_sanitize_markdown_backslashes(self):
        self.assertEqual(sanitize_markdown("Back\\slash"), "Back\\\\slash")
        self.assertEqual(sanitize_markdown("Pipe|And\\Backslash"), "Pipe\|And\\\\Backslash")
        self.assertEqual(sanitize_markdown("Ends\\"), "Ends\\\\")

    def test_sanitize_markdown_mixed(self):
        self.assertEqual(sanitize_markdown("Link| <a href='x'>"), "Link\| &lt;a href='x'&gt;")

    def test_sanitize_markdown_non_string(self):
        self.assertEqual(sanitize_markdown(123), "123")
        self.assertEqual(sanitize_markdown(None), "")

if __name__ == '__main__':
    unittest.main()
