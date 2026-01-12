
import unittest
from unittest.mock import MagicMock
import asyncio
from scraper import MarkPositionScraperAsync
from bs4 import BeautifulSoup

class TestScraperOptimization(unittest.IsolatedAsyncioTestCase):
    async def test_parse_page_optimization(self):
        # Sample HTML with articles and junk
        html = """
        <html>
        <body>
            <div id="junk">
                <p>Some junk</p>
            </div>
            <article class="post category-tech">
                <h1 class="entry-title"><a href="link1">Title 1</a></h1>
            </article>
            <article class="post category-news">
                <h1 class="entry-title"><a href="link2">Title 2</a></h1>
            </article>
        </body>
        </html>
        """

        scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")

        # Test if it correctly parses articles
        posts = await scraper.parse_page(html)
        self.assertEqual(len(posts), 2)
        self.assertEqual(posts[0]['title'], "Title 1")
        self.assertEqual(posts[1]['title'], "Title 2")

    async def test_fallback(self):
        # Sample HTML where structure is slightly different (e.g. maybe class is different or something)
        # But wait, the fallback is for when strainer returns nothing but full soup finds something.
        # This can happen if SoupStrainer regex fails but full parser finds it?
        # Or if the structure is such that strainer misses it.
        # However, if strainer searches for 'article' with class 'post', and full soup searches for 'article' with class 'post',
        # they should theoretically behave the same unless `parse_only` messes up the tree.

        # Let's test the case where there are NO articles, should return empty list
        html = "<html><body>No articles here</body></html>"
        scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")
        posts = await scraper.parse_page(html)
        self.assertEqual(len(posts), 0)

if __name__ == '__main__':
    unittest.main()
