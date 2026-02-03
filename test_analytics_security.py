import unittest
import analytics

class TestAnalyticsSecurity(unittest.TestCase):
    def test_sanitize_markdown_html(self):
        input_text = "<script>alert('xss')</script>"
        expected = "&lt;script&gt;alert(&#x27;xss&#x27;)&lt;/script&gt;"
        self.assertEqual(analytics.sanitize_markdown(input_text), expected)

    def test_sanitize_markdown_pipe(self):
        input_text = "Category | With Pipe"
        expected = "Category &#124; With Pipe"
        self.assertEqual(analytics.sanitize_markdown(input_text), expected)

    def test_sanitize_markdown_mixed(self):
        input_text = "<b onmouseover=alert(1)>Bold | Pipe</b>"
        # Exact expected string depends on how html.escape works (python 3.2+ escapes single quotes by default if quote=True, which is default)
        # html.escape("<") -> "&lt;"
        # html.escape(">") -> "&gt;"
        # html.escape("'") -> "&#x27;"
        expected = "&lt;b onmouseover=alert(1)&gt;Bold &#124; Pipe&lt;/b&gt;"
        self.assertEqual(analytics.sanitize_markdown(input_text), expected)

    def test_sanitize_markdown_none(self):
        self.assertEqual(analytics.sanitize_markdown(None), "")

if __name__ == '__main__':
    unittest.main()
