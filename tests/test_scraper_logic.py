import unittest
from bs4 import BeautifulSoup
# We will import these from scraper once refactored
# For now, we assume the refactor will expose them
from scraper import clean_text, is_url, extract_categories, extract_domain, parse_html_content

SAMPLE_HTML = """
<!DOCTYPE html>
<html>
<body>
    <article class="post category-tech category-news">
        <header class="entry-header">
            <h1 class="entry-title"><a href="https://example.com/post1">Test Post Title</a></h1>
            <div class="entry-meta">
                <span class="posted-on">
                    <time class="entry-date published" datetime="2023-10-27T10:00:00+00:00">October 27, 2023</time>
                </span>
                <span class="byline">
                    <span class="author vcard"><a class="url fn n" href="#">Test Author</a></span>
                </span>
            </div>
        </header>
        <div class="entry-content">
            <p>Some content with a <a href="https://external.com">link</a>.</p>
        </div>
    </article>
</body>
</html>
"""

class TestScraperParsing(unittest.TestCase):
    def test_clean_text(self):
        self.assertEqual(clean_text("  Hello   World  "), "Hello World")
        self.assertEqual(clean_text("Hello\xa0World"), "Hello World")
        self.assertEqual(clean_text(None), "")

    def test_is_url(self):
        self.assertTrue(is_url("https://google.com"))
        self.assertFalse(is_url("Not a URL"))

    def test_extract_categories(self):
        soup = BeautifulSoup('<article class="post category-foo-bar category-baz"></article>', 'html.parser')
        article = soup.find('article')
        cats = extract_categories(article)
        self.assertEqual(sorted(cats), sorted(["Foo Bar", "Baz"]))

    def test_extract_domain(self):
        self.assertEqual(extract_domain("https://www.google.com/search"), "google.com")
        self.assertIsNone(extract_domain(None))

    def test_parse_html_content(self):
        results = parse_html_content(SAMPLE_HTML)
        self.assertEqual(len(results), 1)
        post = results[0]
        self.assertEqual(post['title'], "Test Post Title")
        self.assertEqual(post['author'], "Test Author")
        self.assertEqual(post['date'], "October 27, 2023")
        self.assertEqual(post['datetime'], "2023-10-27T10:00:00+00:00")
        self.assertEqual(sorted(post['categories']), sorted(["Tech", "News"]))
        self.assertEqual(post['external_link'], "https://external.com")
        self.assertEqual(post['domain'], "external.com")
        self.assertEqual(post['post_url'], "https://example.com/post1")

if __name__ == '__main__':
    unittest.main()
