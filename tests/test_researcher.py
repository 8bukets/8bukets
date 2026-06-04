import unittest
from unittest.mock import patch, MagicMock
import os
import json
from agents.researcher import ResearcherAgent

class TestResearcherAgent(unittest.TestCase):
    def setUp(self):
        self.agent = ResearcherAgent()

    @patch('subprocess.run')
    @patch('os.path.exists')
    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    def test_perform_task_success(self, mock_open, mock_exists, mock_subprocess):
        # Setup mocks
        mock_exists.return_value = True

        # Mock file content for json.load
        mock_file_content = json.dumps([{"title": "Test Post"}])
        mock_open.return_value.__enter__.return_value.read.return_value = mock_file_content

        # Run task
        result = self.agent.perform_task({'limit': 1})

        # Assertions
        self.assertEqual(mock_subprocess.call_count, 2)
        self.assertIn('blog_posts', result)
        self.assertIn('google_listings', result)

    @patch('subprocess.run')
    def test_perform_task_failure_handling(self, mock_subprocess):
        # Simulate subprocess failure
        mock_subprocess.side_effect = Exception("Subprocess failed")

        result = self.agent.perform_task({'limit': 1})

        self.assertEqual(result['blog_posts'], [])
        self.assertEqual(result['google_listings'], [])

if __name__ == '__main__':
    unittest.main()
