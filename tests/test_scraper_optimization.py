
import unittest
from bs4 import BeautifulSoup, SoupStrainer
from scraper import MarkPositionScraperAsync
import asyncio

class TestScraperOptimization(unittest.TestCase):
    def setUp(self):
        self.html_content = """
        <html>
        <head><title>Test</title></head>
        <body>
            <div id="header">Header content</div>
            <article class="post">
                <h1 class="entry-title"><a href="http://example.com/1">Post 1</a></h1>
                <time class="entry-date" datetime="2023-01-01">Jan 1, 2023</time>
                <div class="entry-content">Content 1</div>
            </article>
            <div id="sidebar">Sidebar content</div>
            <article class="post">
                <h1 class="entry-title"><a href="http://example.com/2">Post 2</a></h1>
                <time class="entry-date" datetime="2023-01-02">Jan 2, 2023</time>
                <div class="entry-content">Content 2</div>
            </article>
            <div id="footer">Footer content</div>
        </body>
        </html>
        """
        self.scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")

    def test_strainer_logic(self):
        # Verify that SoupStrainer correctly identifies the tags we want
        strainer = SoupStrainer('article', class_='post')
        soup = BeautifulSoup(self.html_content, 'html.parser', parse_only=strainer)
        articles = soup.find_all('article', class_='post')
        self.assertEqual(len(articles), 2)

        # Verify that children are preserved (crucial for extraction)
        title = articles[0].select_one('h1.entry-title a')
        self.assertIsNotNone(title)
        self.assertEqual(title.get_text(), "Post 1")

    def test_parse_page_returns_correct_data(self):
        # This test ensures that if we modify parse_page, it still works
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        posts = loop.run_until_complete(self.scraper.parse_page(self.html_content))
        loop.close()

        self.assertEqual(len(posts), 2)
        self.assertEqual(posts[0]['title'], "Post 1")
        self.assertEqual(posts[1]['title'], "Post 2")

if __name__ == '__main__':
    unittest.main()
