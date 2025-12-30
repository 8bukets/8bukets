
import unittest
from bs4 import BeautifulSoup, SoupStrainer
from scraper import MarkPositionScraperAsync
import asyncio

class TestScraper(unittest.TestCase):
    def test_clean_text(self):
        scraper = MarkPositionScraperAsync("", "", "")
        self.assertEqual(scraper.clean_text("  hello   world  "), "hello world")
        self.assertEqual(scraper.clean_text("hello\xa0world"), "hello world")

    def test_extract_categories(self):
        scraper = MarkPositionScraperAsync("", "", "")
        html = '<article class="post category-tech category-news"></article>'
        soup = BeautifulSoup(html, 'html.parser')
        article = soup.find('article')
        categories = scraper.extract_categories(article)
        self.assertIn("Tech", categories)
        self.assertIn("News", categories)

    def test_parse_page_logic(self):
        # Using a sync wrapper for async method test or just extracting logic
        # For simplicity, we can test the parse logic by mocking the HTML
        html = """
        <html>
        <body>
            <article class="post">
                <header class="entry-header">
                    <h1 class="entry-title"><a href="http://example.com/post1">Title 1</a></h1>
                    <time class="entry-date" datetime="2023-01-01">Jan 1, 2023</time>
                </header>
                <div class="entry-content">
                    <p>Content</p>
                </div>
            </article>
        </body>
        </html>
        """
        scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")

        # Use asyncio.run for cleaner async execution
        results = asyncio.run(scraper.parse_page(html))

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['title'], "Title 1")
        self.assertEqual(results[0]['date'], "Jan 1, 2023")

if __name__ == '__main__':
    unittest.main()
