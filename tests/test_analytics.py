import unittest
from analytics import escape_markdown

class TestAnalyticsSecurity(unittest.TestCase):
    def test_escape_markdown_basic(self):
        self.assertEqual(escape_markdown("Hello World"), "Hello World")

    def test_escape_markdown_pipes(self):
        self.assertEqual(escape_markdown("Hello | World"), "Hello \| World")
        self.assertEqual(escape_markdown("|Start"), "\|Start")
        self.assertEqual(escape_markdown("End|"), "End\|")

    def test_escape_markdown_html(self):
        self.assertEqual(escape_markdown("<script>"), "&lt;script&gt;")
        self.assertEqual(escape_markdown("<b>bold</b>"), "&lt;b&gt;bold&lt;/b&gt;")

    def test_escape_markdown_newlines(self):
        self.assertEqual(escape_markdown("Line\nBreak"), "Line Break")
        self.assertEqual(escape_markdown("Carriage\rReturn"), "Carriage Return")

    def test_escape_markdown_mixed(self):
        payload = "evil.com | 100 |\n<script>"
        expected = "evil.com \| 100 \| &lt;script&gt;"
        self.assertEqual(escape_markdown(payload), expected)

    def test_escape_markdown_none(self):
        self.assertEqual(escape_markdown(None), "")

if __name__ == '__main__':
    unittest.main()
