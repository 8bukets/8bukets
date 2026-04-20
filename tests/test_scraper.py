
import unittest
from bs4 import BeautifulSoup, SoupStrainer
from scraper import MarkPositionScraperAsync
import asyncio

class TestScraperParsing(unittest.TestCase):
    def setUp(self):
        self.scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")
        self.sample_html = """
        <html>
            <body>
                <header>Ignored</header>
                <article class="post">
                    <h1 class="entry-title"><a href="http://example.com/post1">Title 1</a></h1>
                    <time class="entry-date" datetime="2023-01-01">Jan 1, 2023</time>
                    <div class="entry-content">
                        <a href="http://external.com/1">External Link 1</a>
                    </div>
                </article>
                <article class="post">
                    <h1 class="entry-title"><a href="http://example.com/post2">Title 2</a></h1>
                </article>
                <footer>Ignored</footer>
            </body>
        </html>
        """

    def test_parse_page(self):
        # We need to run the async method
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        results = loop.run_until_complete(self.scraper.parse_page(self.sample_html))
        loop.close()

        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]['title'], "Title 1")
        self.assertEqual(results[0]['external_link'], "http://external.com/1")
        self.assertEqual(results[1]['title'], "Title 2")

    def test_soup_strainer_logic(self):
        # Test that strainer + lxml (if available) finds the articles
        try:
            strainer = SoupStrainer('article')
            soup = BeautifulSoup(self.sample_html, 'lxml', parse_only=strainer)
            articles = soup.find_all('article', class_='post')
            self.assertEqual(len(articles), 2)
        except Exception as e:
            # If lxml not installed, this test might fail or be skipped in some environments
            # But in this env we know lxml is installed
            self.fail(f"lxml parsing failed: {e}")

if __name__ == '__main__':
    unittest.main()
