import unittest
from security_utils import sanitize_for_markdown

class TestSecurityUtils(unittest.TestCase):
    def test_sanitize_basic(self):
        self.assertEqual(sanitize_for_markdown("Hello World"), "Hello World")

    def test_sanitize_links(self):
        malicious = "[Click Me](javascript:alert(1))"
        # We expect [ to be escaped, ] to be escaped, ( escaped, ) escaped.
        # [ -> \[
        # ] -> \]
        # ( -> \(
        # ) -> \)
        expected = "\\[Click Me\\]\\(javascript:alert\\(1\\)\\)"
        self.assertEqual(sanitize_for_markdown(malicious), expected)

    def test_sanitize_html(self):
        malicious = "<script>alert(1)</script>"
        # < -> &lt;
        # > -> &gt;
        expected = "&lt;script&gt;alert\\(1\\)&lt;/script&gt;"
        self.assertEqual(sanitize_for_markdown(malicious), expected)

    def test_sanitize_formatting(self):
        malicious = "**Bold** and *Italic* and `Code`"
        # * -> \*
        # ` -> \`
        expected = "\\*\\*Bold\\*\\* and \\*Italic\\* and \\`Code\\`"
        self.assertEqual(sanitize_for_markdown(malicious), expected)

    def test_none_input(self):
        self.assertEqual(sanitize_for_markdown(None), "")

    def test_numeric_input(self):
        self.assertEqual(sanitize_for_markdown(123), "123")

    def test_pipe_injection(self):
        malicious = "Malicious | Pipe"
        expected = "Malicious \\| Pipe"
        self.assertEqual(sanitize_for_markdown(malicious), expected)

    def test_backslash_injection(self):
        malicious = "Back\\slash"
        expected = "Back\\\\slash"
        self.assertEqual(sanitize_for_markdown(malicious), expected)

if __name__ == '__main__':
    unittest.main()
