import unittest
import asyncio
from unittest.mock import MagicMock, patch
from bs4 import BeautifulSoup, SoupStrainer
from scraper import MarkPositionScraperAsync

class TestScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = MarkPositionScraperAsync(
            output_json="test.json",
            output_csv="test.csv",
            output_txt="test.txt"
        )
        self.sample_html = """
        <html>
            <body>
                <header>Header content</header>
                <article class="post">
                    <h1 class="entry-title"><a href="http://example.com/1">Post 1</a></h1>
                    <time class="entry-date" datetime="2023-01-01">Jan 1, 2023</time>
                </article>
                <article class="post">
                    <h1 class="entry-title"><a href="http://example.com/2">Post 2</a></h1>
                    <time class="entry-date" datetime="2023-01-02">Jan 2, 2023</time>
                </article>
                <footer>Footer content</footer>
            </body>
        </html>
        """

    def test_clean_text(self):
        self.assertEqual(self.scraper.clean_text("  Hello   World  "), "Hello World")
        self.assertEqual(self.scraper.clean_text("Hello\xa0World"), "Hello World")

    def test_sanitize_for_csv(self):
        self.assertEqual(self.scraper.sanitize_for_csv("Normal text"), "Normal text")
        self.assertEqual(self.scraper.sanitize_for_csv("=Formula"), "'=Formula")
        self.assertEqual(self.scraper.sanitize_for_csv("+Formula"), "'+Formula")
        self.assertEqual(self.scraper.sanitize_for_csv("-Formula"), "'-Formula")
        self.assertEqual(self.scraper.sanitize_for_csv("@Formula"), "'@Formula")

    def test_parse_page(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(self.scraper.parse_page(self.sample_html))
        loop.close()

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['title'], "Post 1")
        self.assertEqual(result[1]['title'], "Post 2")

    def test_parse_page_empty(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(self.scraper.parse_page("<html></html>"))
        loop.close()
        self.assertEqual(len(result), 0)

    def test_soup_strainer_logic(self):
        # This test verifies that using SoupStrainer correctly preserves the elements we need
        strainer = SoupStrainer('article')
        soup = BeautifulSoup(self.sample_html, 'html.parser', parse_only=strainer)
        articles = soup.find_all('article', class_='post')
        self.assertEqual(len(articles), 2)

        # Verify content inside article matches
        title1 = articles[0].select_one('h1.entry-title a').get_text()
        self.assertEqual(title1, "Post 1")

if __name__ == '__main__':
    unittest.main()
