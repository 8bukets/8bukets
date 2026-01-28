import unittest
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# valid import only after the function is added
try:
    from analytics import sanitize_markdown
except ImportError:
    # define a dummy function if it doesn't exist yet so we can run the test file (and fail)
    def sanitize_markdown(text):
        raise NotImplementedError("sanitize_markdown not implemented in analytics.py")

class TestSecurity(unittest.TestCase):
    def test_sanitize_markdown_html(self):
        input_text = "<script>alert(1)</script>"
        expected = "&lt;script&gt;alert(1)&lt;/script&gt;"
        self.assertEqual(sanitize_markdown(input_text), expected)

    def test_sanitize_markdown_table(self):
        input_text = "Bad | Table"
        expected = "Bad \\| Table"
        self.assertEqual(sanitize_markdown(input_text), expected)

    def test_sanitize_markdown_mixed(self):
        input_text = "<div class='row'>|Content|</div>"
        expected = "&lt;div class='row'&gt;\\|Content\\|&lt;/div&gt;"
        self.assertEqual(sanitize_markdown(input_text), expected)

    def test_sanitize_markdown_none(self):
        self.assertEqual(sanitize_markdown(None), "")

    def test_sanitize_markdown_int(self):
        self.assertEqual(sanitize_markdown(123), "123")

    def test_sanitize_markdown_ampersand(self):
        input_text = "Ben & Jerry's"
        expected = "Ben &amp; Jerry's"
        self.assertEqual(sanitize_markdown(input_text), expected)

if __name__ == '__main__':
    unittest.main()
