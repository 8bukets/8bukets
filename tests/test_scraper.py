import unittest
from scrape_informatic import is_external_link, BASE_URL

class TestScraper(unittest.TestCase):

    def test_is_external_link(self):
        self.assertTrue(is_external_link("https://google.com", BASE_URL))
        self.assertFalse(is_external_link("https://informaticmagazine.data.blog/some-post", BASE_URL))
        self.assertFalse(is_external_link("/some-post", BASE_URL))
        self.assertFalse(is_external_link(None, BASE_URL))

if __name__ == '__main__':
    unittest.main()
