import unittest
import asyncio
from scraper import MarkPositionScraperAsync

SAMPLE_HTML = """
<!DOCTYPE html>
<html>
<body>
    <div id="content">
        <article class="post category-tech">
            <h1 class="entry-title"><a href="http://example.com/1">Title 1</a></h1>
            <time class="entry-date" datetime="2023-01-01">Jan 1</time>
            <div class="author vcard"><span class="fn">Alice</span></div>
            <div class="entry-content">
                <p>Content</p>
            </div>
        </article>
        <article class="post category-life">
            <h1 class="entry-title"><a href="http://example.com/2">Title 2</a></h1>
            <time class="entry-date" datetime="2023-01-02">Jan 2</time>
            <div class="author vcard"><span class="fn">Bob</span></div>
            <div class="entry-content">
                <a href="https://external.com">Link</a>
            </div>
        </article>
        <div class="sidebar">
            <!-- Noise -->
        </div>
    </div>
</body>
</html>
"""

class TestScraperOptimization(unittest.TestCase):
    def setUp(self):
        self.scraper = MarkPositionScraperAsync("json", "csv", "txt")

    def test_parse_page_correctness(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        results = loop.run_until_complete(self.scraper.parse_page(SAMPLE_HTML))

        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]['title'], "Title 1")
        self.assertEqual(results[0]['author'], "Alice")
        self.assertIn("Tech", results[0]['categories'])

        self.assertEqual(results[1]['title'], "Title 2")
        self.assertEqual(results[1]['external_link'], "https://external.com")
        loop.close()

if __name__ == '__main__':
    unittest.main()
