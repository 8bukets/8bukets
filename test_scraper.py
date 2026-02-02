import unittest
from bs4 import BeautifulSoup
import scraper

# Mock HTML for testing
SAMPLE_HTML = """
<html>
<body>
    <article class="post category-tech">
        <header class="entry-header">
            <h1 class="entry-title"><a href="http://example.com/post1">Test Post Title</a></h1>
            <div class="entry-meta">
                <time class="entry-date" datetime="2023-01-01T12:00:00">January 1, 2023</time>
                <div class="author vcard"><span class="fn">Test Author</span></div>
            </div>
        </header>
        <div class="entry-content">
            <p>Some content</p>
            <a href="https://external.com">External Link</a>
        </div>
    </article>
    <article class="post">
        <h1 class="entry-title"><a href="http://example.com/post2">Second Post</a></h1>
    </article>
    <!-- Should NOT be matched -->
    <article class="poster">
        <h1 class="entry-title"><a href="http://example.com/bad">Poster Article</a></h1>
    </article>
</body>
</html>
"""

class TestScraper(unittest.TestCase):

    def test_clean_text(self):
        # These functions will be module level
        self.assertEqual(scraper.clean_text("  Hello   World  "), "Hello World")
        self.assertEqual(scraper.clean_text("Hello\xa0World"), "Hello World")

    def test_is_url(self):
        self.assertTrue(scraper.is_url("http://google.com"))
        self.assertTrue(scraper.is_url("https://google.com"))
        self.assertFalse(scraper.is_url("google.com"))

    def test_extract_domain(self):
        self.assertEqual(scraper.extract_domain("https://www.google.com/path"), "google.com")
        self.assertEqual(scraper.extract_domain("http://sub.example.com"), "sub.example.com")
        self.assertIsNone(scraper.extract_domain(None))

    def test_parse_html(self):
        # Test the main parsing logic
        results = scraper.parse_html(SAMPLE_HTML)
        # Should be 2, ignoring "poster"
        self.assertEqual(len(results), 2)

        post1 = results[0]
        self.assertEqual(post1['title'], "Test Post Title")
        self.assertEqual(post1['date'], "January 1, 2023")
        self.assertEqual(post1['datetime'], "2023-01-01T12:00:00")
        self.assertEqual(post1['author'], "Test Author")
        self.assertEqual(post1['external_link'], "https://external.com")
        self.assertEqual(post1['domain'], "external.com")
        self.assertIn("Tech", post1['categories'])

        post2 = results[1]
        self.assertEqual(post2['title'], "Second Post")

if __name__ == '__main__':
    unittest.main()
