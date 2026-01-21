import unittest
from agents.security_utils import sanitize_for_markdown

class TestSecurityUtils(unittest.TestCase):
    def test_sanitize_for_markdown_basic(self):
        self.assertEqual(sanitize_for_markdown("Hello World"), "Hello World")
        self.assertEqual(sanitize_for_markdown(""), "")

    def test_sanitize_markdown_chars(self):
        # * _ ` { } [ ] ( ) # + - . ! < >
        dangerous = "*Bold* and [Link](http://example.com)"
        # Note: colon : is not escaped, forward slash / is not escaped
        expected = r"\*Bold\* and \[Link\]\(http://example\.com\)"
        self.assertEqual(sanitize_for_markdown(dangerous), expected)

    def test_sanitize_html(self):
        dangerous = "<script>alert('xss')</script>"
        # single quote ' is not escaped
        expected = r"\<script\>alert\('xss'\)\</script\>"
        self.assertEqual(sanitize_for_markdown(dangerous), expected)

    def test_sanitize_complex(self):
        dangerous = "Click [here](javascript:alert(1)) to win!"
        expected = r"Click \[here\]\(javascript:alert\(1\)\) to win\!"
        self.assertEqual(sanitize_for_markdown(dangerous), expected)

    def test_sanitize_pipes(self):
        # Pipes are used in tables
        dangerous = "| Column 1 | Column 2 |"
        expected = r"\| Column 1 \| Column 2 \|"
        self.assertEqual(sanitize_for_markdown(dangerous), expected)

    def test_double_escape_backslash(self):
        # Backslash itself should be escaped
        dangerous = r"C:\Windows\System32"
        expected = r"C:\\Windows\\System32"
        self.assertEqual(sanitize_for_markdown(dangerous), expected)

if __name__ == '__main__':
    unittest.main()
