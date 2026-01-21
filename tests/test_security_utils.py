import unittest
from agents.security_utils import sanitize_for_markdown, sanitize_url

class TestSecurityUtils(unittest.TestCase):

    def test_sanitize_markdown_basic(self):
        self.assertEqual(sanitize_for_markdown("Hello World"), "Hello World")

    def test_sanitize_markdown_special_chars(self):
        # Testing various special characters
        unsafe = "*bold* _italic_ [link](url) | table |"
        expected = r"\*bold\* \_italic\_ \[link\]\(url\) \| table \|"
        self.assertEqual(sanitize_for_markdown(unsafe), expected)

    def test_sanitize_markdown_headers(self):
        unsafe = "# Header"
        expected = r"\# Header"
        self.assertEqual(sanitize_for_markdown(unsafe), expected)

    def test_sanitize_markdown_html(self):
        unsafe = "<script>alert(1)</script>"
        expected = r"\<script\>alert\(1\)\</script\>"
        self.assertEqual(sanitize_for_markdown(unsafe), expected)

    def test_sanitize_markdown_none(self):
        self.assertEqual(sanitize_for_markdown(None), "")

    def test_sanitize_markdown_int(self):
        self.assertEqual(sanitize_for_markdown(123), "123")

    def test_sanitize_url_basic(self):
        self.assertEqual(sanitize_url("https://example.com"), "https://example.com")

    def test_sanitize_url_parens(self):
        unsafe = "https://example.com/foo(bar)"
        expected = "https://example.com/foo(bar%29" # We assume ( is fine, ) breaks it
        self.assertEqual(sanitize_url(unsafe), expected)

    def test_sanitize_url_spaces(self):
        unsafe = "https://example.com/foo bar"
        expected = "https://example.com/foo%20bar"
        self.assertEqual(sanitize_url(unsafe), expected)

    def test_sanitize_url_control_chars(self):
        unsafe = "https://example.com\n"
        expected = "https://example.com"
        self.assertEqual(sanitize_url(unsafe), expected)

if __name__ == '__main__':
    unittest.main()
