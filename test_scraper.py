import unittest
from scrape_gadgets import GadgetScraper
from models import Post

SAMPLE_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
</head>
<body class="home blog">
<div id="page" class="site">
	<div id="content" class="site-content">
		<main id="main" class="site-main" role="main">
            <article id="post-1" class="post type-post status-publish format-standard has-post-thumbnail hentry category-tech tag-gadget">
                <div class="featured-image">
                    <img src="https://example.com/image.jpg?w=840" />
                </div>
                <header class="entry-header">
                    <span class="cat-links"><a href="https://example.com/category/tech">Tech</a></span>
                    <span class="tags-links"><a href="https://example.com/tag/gadget">Gadget</a></span>
                    <h2 class="entry-title"><a href="https://infogadgettech.wordpress.com/2022/10/12/example-post/">Example Post</a></h2>
                    <div class="entry-meta">
                        <span class="posted-on"><time class="entry-date published" datetime="2022-10-12">October 12, 2022</time></span>
                        <span class="byline"> by <span class="author vcard"><a class="url fn n" href="#">John Doe</a></span></span>
                    </div>
                </header>
                <div class="entry-content">
                    <p><a href="https://external-link.com">https://external-link.com</a></p>
                </div>
            </article>
            <div class="nav-previous"><a href="https://infogadgettech.wordpress.com/page/2/">Older posts</a></div>
		</main>
	</div>
</div>
</body>
</html>
"""

class TestGadgetScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = GadgetScraper("http://mock-url.com", 1)

    def test_parse_date(self):
        self.assertEqual(self.scraper.parse_date("October 12, 2022"), "2022-10-12")
        self.assertEqual(self.scraper.parse_date("January 1, 2023"), "2023-01-01")
        # Test invalid date behavior
        self.assertEqual(self.scraper.parse_date("Invalid Date"), "Invalid Date")

    def test_extract_posts_from_html(self):
        posts, next_url = self.scraper.extract_posts_from_html(SAMPLE_HTML)

        self.assertEqual(len(posts), 1)
        post = posts[0]

        self.assertIsInstance(post, Post)
        self.assertEqual(post.title, "Example Post")
        self.assertEqual(post.date, "2022-10-12")
        self.assertEqual(post.author, "John Doe")
        self.assertEqual(post.external_link, "https://external-link.com")
        self.assertEqual(post.categories, ["Tech"])
        self.assertEqual(post.tags, ["Gadget"])
        self.assertEqual(post.image_url, "https://example.com/image.jpg")
        self.assertEqual(post.original_url, "https://infogadgettech.wordpress.com/2022/10/12/example-post/")

        self.assertEqual(next_url, "https://infogadgettech.wordpress.com/page/2/")

if __name__ == '__main__':
    unittest.main()
