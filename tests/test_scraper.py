import unittest
import asyncio
from scraper import MarkPositionScraperAsync

SAMPLE_HTML = """
<!DOCTYPE html>
<html>
<body>
    <article class="post tag-tech category-news">
        <h1 class="entry-title"><a href="http://example.com/post1">Test Post Title</a></h1>
        <time class="entry-date" datetime="2023-10-27T10:00:00">October 27, 2023</time>
        <div class="author vcard"><span class="fn">John Doe</span></div>
        <div class="entry-content">
            <p>Some content</p>
            <a href="https://external.com">External Link</a>
        </div>
    </article>
</body>
</html>
"""

class TestScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")

    def test_clean_text(self):
        self.assertEqual(self.scraper.clean_text("  Hello   World  "), "Hello World")
        self.assertEqual(self.scraper.clean_text("Hello\xa0World"), "Hello World")

    def test_is_url(self):
        self.assertTrue(self.scraper.is_url("http://google.com"))
        self.assertFalse(self.scraper.is_url("Not a URL"))

    def test_extract_domain(self):
        self.assertEqual(self.scraper.extract_domain("https://www.google.com/path"), "google.com")
        self.assertIsNone(self.scraper.extract_domain(None))

    def test_parse_page(self):
        # parse_page is synchronous now
        posts = self.scraper.parse_page(SAMPLE_HTML)
        self.assertEqual(len(posts), 1)
        post = posts[0]
        self.assertEqual(post['title'], "Test Post Title")
        self.assertEqual(post['date'], "October 27, 2023")
        self.assertEqual(post['author'], "John Doe")
        self.assertIn("News", post['categories'])
        self.assertEqual(post['external_link'], "https://external.com")
        self.assertEqual(post['domain'], "external.com")
        self.assertEqual(post['post_url'], "http://example.com/post1")

if __name__ == '__main__':
    unittest.main()
