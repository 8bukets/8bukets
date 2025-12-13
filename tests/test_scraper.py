import unittest
from bs4 import BeautifulSoup
from scrape_informatic import is_external_link, parse_post_html, Post

class TestScraper(unittest.TestCase):

    def test_is_external_link(self):
        base = "https://example.com"
        self.assertTrue(is_external_link("https://google.com", base))
        self.assertTrue(is_external_link("http://other.com/foo", base))
        self.assertFalse(is_external_link("https://example.com/page/2", base))
        self.assertFalse(is_external_link("/local/path", base))
        self.assertFalse(is_external_link(None, base))
        self.assertFalse(is_external_link("", base))

    def test_parse_post_html(self):
        html = """
        <article class="post">
            <header class="entry-header">
                <h2 class="entry-title"><a href="https://example.com/post1">Test Title</a></h2>
                <div class="entry-meta">
                    <time class="entry-date" datetime="2023-01-01T12:00:00+00:00">January 1, 2023</time>
                </div>
            </header>
            <div class="entry-content">
                <p>This is some content with a <a href="https://google.com">link</a>.</p>
            </div>
            <span class="cat-links"><a href="/cat/tech">Tech</a></span>
        </article>
        """
        soup = BeautifulSoup(html, 'html.parser')
        article = soup.find('article')
        post = parse_post_html(article, "https://example.com")

        self.assertIsInstance(post, Post)
        self.assertEqual(post.title, "Test Title")
        self.assertEqual(post.post_url, "https://example.com/post1")
        self.assertEqual(post.date, "2023-01-01T12:00:00+00:00")
        self.assertEqual(post.date_text, "January 1, 2023")
        self.assertEqual(post.categories, ["Tech"])
        self.assertEqual(post.external_links, ["https://google.com"])
        self.assertIn("This is some content with a [link](https://google.com).", post.content)
        self.assertIsNone(post.image_url)

    def test_parse_post_html_missing_fields(self):
        html = """
        <article class="post">
             <div class="entry-content">
                Just content.
            </div>
        </article>
        """
        soup = BeautifulSoup(html, 'html.parser')
        article = soup.find('article')
        post = parse_post_html(article, "https://example.com")

        self.assertIsNone(post.title)
        self.assertIsNone(post.post_url)
        self.assertIsNone(post.date)
        self.assertEqual(post.categories, [])
        self.assertIn("Just content.", post.content)

if __name__ == '__main__':
    unittest.main()
