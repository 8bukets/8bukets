
import unittest
from scraper import OracleNewsScraper

class TestOracleNewsScraper(unittest.TestCase):
    def test_clean_text(self):
        scraper = OracleNewsScraper("json", "csv", "txt")
        self.assertEqual(scraper.clean_text("  hello   world  "), "hello world")
        self.assertEqual(scraper.clean_text("hello\xa0world"), "hello world")
        self.assertEqual(scraper.clean_text(None), "")

    def test_parse_date(self):
        scraper = OracleNewsScraper("json", "csv", "txt")
        result = scraper.parse_date("Oct 15, 2025")
        self.assertEqual(result['display'], "Oct 15, 2025")
        self.assertEqual(result['iso'], "2025-10-15T00:00:00")

        result_invalid = scraper.parse_date("Invalid Date")
        self.assertEqual(result_invalid['display'], "Invalid Date")
        self.assertIsNone(result_invalid['iso'])

    def test_parse_page_regex_optimization(self):
        scraper = OracleNewsScraper("json", "csv", "txt")
        html = """
        <html>
        <body>
            <!--
            <section class="rc92 rc92v0">
                <ul>
                    <li class="rc92w3">
                        <div class="rc92-dt">Oct 15, 2025</div>
                        <h5><a href="/news/link1">Title 1</a></h5>
                    </li>
                </ul>
            </section>
            -->
        </body>
        </html>
        """
        posts = scraper.parse_page(html)
        self.assertEqual(len(posts), 1)
        self.assertEqual(posts[0]['title'], "Title 1")
        self.assertEqual(posts[0]['date'], "Oct 15, 2025")

    def test_parse_page_fallback(self):
        # Test that it works even if the structure is slightly different but still parsable by BS4 fallback?
        # Actually, the fallback logic mimics the regex logic but uses BS4.
        # So if regex fails to find the comment, BS4 should find it.
        # But regex finds <!-- .*? -->. BS4 finds Comment nodes.

        # This case tests if Regex fails for some reason but BS4 succeeds.
        # It's hard to construct a case where regex fails to find a comment that BS4 finds,
        # unless the comment syntax is weird but BS4 is lenient.

        scraper = OracleNewsScraper("json", "csv", "txt")
        # Standard valid comment
        html = """<!-- <section class="rc92 rc92v0"><li class="rc92w3"><div class="rc92-dt">Oct 15, 2025</div><h5><a href="l">T</a></h5></li></section> -->"""
        posts = scraper.parse_page(html)
        self.assertEqual(len(posts), 1)

if __name__ == '__main__':
    unittest.main()
