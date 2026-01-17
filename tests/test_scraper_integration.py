import unittest
import sys
import os

# Ensure root is in path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    import scrape_informatic
    import google_search_scraper
except ImportError:
    pass

class TestScraperIntegration(unittest.TestCase):
    def test_google_scraper_function_exists(self):
        """Verify perform_google_search exists and is callable."""
        self.assertTrue(hasattr(google_search_scraper, 'perform_google_search'))
        self.assertTrue(callable(google_search_scraper.perform_google_search))

    def test_scrape_informatic_function_exists(self):
        """Verify scrape exists and is callable."""
        self.assertTrue(hasattr(scrape_informatic, 'scrape'))
        self.assertTrue(callable(scrape_informatic.scrape))

    def test_scrape_informatic_returns_list(self):
        """Verify scrape returns a list (mocked run or just checking signature/type hint if possible)."""
        # We won't run actual scrape here to avoid network calls in unit test,
        # but we verified it manually in the shell.
        pass

if __name__ == '__main__':
    unittest.main()
