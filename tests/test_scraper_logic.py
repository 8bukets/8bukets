import unittest
import asyncio
import sys
import os

# Ensure we can import scraper
sys.path.append(os.getcwd())

from scraper import MarkPositionScraperAsync

SAMPLE_HTML = """
<!DOCTYPE html>
<html>
<body>
    <article class="post category-tech category-news">
        <h1 class="entry-title"><a href="http://example.com/post-1">Test Post Title</a></h1>
        <time class="entry-date" datetime="2023-10-27T10:00:00+00:00">October 27, 2023</time>
        <div class="author vcard"><span class="fn">Test Author</span></div>
        <div class="entry-content">
            <p>Here is a link: <a href="https://external-domain.com/article">External Link</a></p>
        </div>
    </article>
    <article class="post">
        <h1 class="entry-title"><a href="http://example.com/post-2">Second Post</a></h1>
        <!-- Missing time and author -->
        <div class="entry-content">
            <p>No external link here.</p>
        </div>
    </article>
</body>
</html>
"""

class TestScraperLogic(unittest.TestCase):
    def setUp(self):
        self.scraper = MarkPositionScraperAsync(
            output_json="test.json",
            output_csv="test.csv",
            output_txt="test.txt"
        )

    def test_parse_page(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        try:
            results = loop.run_until_complete(self.scraper.parse_page(SAMPLE_HTML))

            self.assertEqual(len(results), 2)

            # Check first post
            post1 = results[0]
            self.assertEqual(post1['title'], "Test Post Title")
            self.assertEqual(post1['author'], "Test Author")
            self.assertEqual(post1['date'], "October 27, 2023")
            self.assertIn("Tech", post1['categories'])
            self.assertIn("News", post1['categories'])
            self.assertEqual(post1['external_link'], "https://external-domain.com/article")
            self.assertEqual(post1['domain'], "external-domain.com")

            # Check second post
            post2 = results[1]
            self.assertEqual(post2['title'], "Second Post")
            self.assertIsNone(post2['author'])
            self.assertIsNone(post2['external_link'])

        finally:
            loop.close()

if __name__ == '__main__':
    unittest.main()
