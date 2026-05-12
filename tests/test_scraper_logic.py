import unittest
import asyncio
from scraper import MarkPositionScraperAsync

SAMPLE_HTML = """
<!DOCTYPE html>
<html>
<body>
    <article class="post category-tech category-news">
        <h1 class="entry-title"><a href="http://example.com/post1">Test Post Title</a></h1>
        <time class="entry-date" datetime="2023-10-27T10:00:00+00:00">October 27, 2023</time>
        <div class="author vcard"><span class="fn">John Doe</span></div>
        <div class="entry-content">
            <p>Some content <a href="https://external.com/link">External Link</a></p>
        </div>
    </article>
</body>
</html>
"""

class TestScraperLogic(unittest.TestCase):
    def test_parse_page(self):
        scraper = MarkPositionScraperAsync("json", "csv", "txt")

        results = None

        if hasattr(scraper, '_parse_page_sync'):
             results = scraper._parse_page_sync(SAMPLE_HTML)
        elif hasattr(scraper, 'parse_page'):
             # Helper to run async method
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            if asyncio.iscoroutinefunction(scraper.parse_page):
                results = loop.run_until_complete(scraper.parse_page(SAMPLE_HTML))
            else:
                 results = scraper.parse_page(SAMPLE_HTML)
            loop.close()

        self.assertIsNotNone(results, "Parsing method not found or returned None")
        self.assertEqual(len(results), 1)
        post = results[0]
        self.assertEqual(post['title'], "Test Post Title")
        self.assertEqual(post['author'], "John Doe")
        self.assertEqual(post['date'], "October 27, 2023")
        self.assertIn("Tech", post['categories'])
        self.assertIn("News", post['categories'])
        self.assertEqual(post['external_link'], "https://external.com/link")
        self.assertEqual(post['domain'], "external.com")

if __name__ == '__main__':
    unittest.main()
