
import unittest
from scraper import OracleNewsScraper

class TestScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = OracleNewsScraper("dummy.json", "dummy.csv", "dummy.txt")
        self.html_content = """
        <html><body>
        <div>Some content</div>
        <!-- Random comment -->
        <!--
        <div class="rc92v0">
            <section>
                <ul>
                    <li class="rc92w3">
                        <div class="rc92-dt">Oct 15, 2025</div>
                        <h5><a href="/news/link1">Title 1</a></h5>
                    </li>
                </ul>
            </section>
        </div>
        -->
        </body></html>
        """

    def test_parse_page(self):
        posts = self.scraper.parse_page(self.html_content)
        self.assertEqual(len(posts), 1)
        self.assertEqual(posts[0]['title'], "Title 1")
        self.assertEqual(posts[0]['date'], "Oct 15, 2025")

    def test_parse_page_no_comment(self):
        html = "<html><body>No comments here</body></html>"
        posts = self.scraper.parse_page(html)
        self.assertEqual(len(posts), 0)

if __name__ == '__main__':
    unittest.main()
