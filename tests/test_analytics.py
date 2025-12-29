import unittest
from analytics import sanitize_markdown

class TestSanitization(unittest.TestCase):
    def test_basic_sanitization(self):
        self.assertEqual(sanitize_markdown("Normal Text"), "Normal Text")

    def test_pipe_escape(self):
        self.assertEqual(sanitize_markdown("Broken | Pipe"), r"Broken \| Pipe")

    def test_html_escape(self):
        self.assertEqual(sanitize_markdown("<script>alert(1)</script>"), "&lt;script&gt;alert(1)&lt;/script&gt;")

    def test_mixed(self):
        self.assertEqual(sanitize_markdown("Foo | <b>Bar</b>"), r"Foo \| &lt;b&gt;Bar&lt;/b&gt;")

if __name__ == '__main__':
    unittest.main()
