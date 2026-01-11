import unittest
from unittest.mock import MagicMock, patch
from agents.researcher import ResearcherAgent

class TestResearcherAgent(unittest.TestCase):
    def setUp(self):
        self.agent = ResearcherAgent()

    @patch('scrape_informatic.scrape')
    @patch('google_search_scraper.perform_google_search')
    def test_perform_task(self, mock_google, mock_scrape):
        # Setup mocks
        mock_scrape.return_value = [{'title': 'Test Post', 'content': 'Test Content'}]
        mock_google.return_value = [{'title': 'Google Result', 'url': 'http://google.com'}]

        # Test input data
        data = {'limit': 1}

        # Execute
        result = self.agent.perform_task(data)

        # Assertions
        mock_scrape.assert_called_once_with(max_pages=1)
        mock_google.assert_called_once()

        self.assertIn('blog_posts', result)
        self.assertIn('google_listings', result)
        self.assertEqual(len(result['blog_posts']), 1)
        self.assertEqual(len(result['google_listings']), 1)
        self.assertEqual(result['blog_posts'][0]['title'], 'Test Post')

if __name__ == '__main__':
    unittest.main()
