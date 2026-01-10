
import unittest
import asyncio
from bs4 import BeautifulSoup
from scraper import MarkPositionScraperAsync

class TestScraperOptimization(unittest.TestCase):
    def setUp(self):
        self.scraper = MarkPositionScraperAsync(
            output_json="test.json",
            output_csv="test.csv",
            output_txt="test.txt"
        )
        self.sample_html = """
        <html>
            <body>
                <header>Ignored Header</header>
                <div id="content">
                    <article class="post">
                        <header class="entry-header">
                            <h1 class="entry-title"><a href="http://example.com/post1">Test Post 1</a></h1>
                            <div class="entry-meta">
                                <span class="posted-on">
                                    <time class="entry-date published" datetime="2023-01-01T12:00:00+00:00">January 1, 2023</time>
                                </span>
                                <span class="byline">
                                    <span class="author vcard"><a class="url fn n" href="#">Test Author</a></span>
                                </span>
                            </div>
                        </header>
                        <div class="entry-content">
                            <p>Some content</p>
                            <a href="https://external.com">External Link</a>
                        </div>
                        <footer class="entry-footer">
                            <span class="cat-links">
                                <a href="#" rel="category tag">Uncategorized</a>
                            </span>
                        </footer>
                    </article>
                    <article class="post">
                        <h1 class="entry-title"><a href="http://example.com/post2">Test Post 2</a></h1>
                    </article>
                </div>
                <footer>Ignored Footer</footer>
            </body>
        </html>
        """

    def test_parse_logic(self):
        # The optimized parse_page is now synchronous (CPU-bound) to be run in executor
        results = self.scraper.parse_page(self.sample_html)

        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]['title'], "Test Post 1")
        self.assertEqual(results[0]['date'], "January 1, 2023")
        self.assertEqual(results[0]['author'], "Test Author")
        self.assertEqual(results[0]['external_link'], "https://external.com")

        self.assertEqual(results[1]['title'], "Test Post 2")

if __name__ == '__main__':
    unittest.main()
