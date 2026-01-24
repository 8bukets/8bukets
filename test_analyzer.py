import unittest
from agents.analyzer import AnalyzerAgent
from collections import Counter

class TestAnalyzerAgent(unittest.TestCase):
    def setUp(self):
        self.agent = AnalyzerAgent()

    def test_empty_input(self):
        data = {"blog_posts": [], "google_listings": []}
        result = self.agent.perform_task(data)
        self.assertEqual(result["total_posts"], 0)
        self.assertEqual(result["average_sentiment"], 0)
        self.assertEqual(result["top_keywords"], [])

    def test_normal_input(self):
        posts = [
            {
                "content": "Python is a great programming language. It is very versatile.",
                "categories": ["Tech"]
            },
            {
                "content": "Coding is fun. Python makes it easy.",
                "categories": ["Tech"]
            }
        ]
        data = {"blog_posts": posts, "google_listings": []}
        result = self.agent.perform_task(data)

        self.assertEqual(result["total_posts"], 2)
        self.assertGreater(result["average_sentiment"], 0)

        # Check keywords
        keywords = dict(result["top_keywords"])
        self.assertIn("python", keywords)
        self.assertIn("great", keywords)

    def test_mixed_input(self):
        posts = [
            {"content": "", "categories": ["Empty"]},
            {"content": "Content here.", "categories": ["Filled"]}
        ]
        data = {"blog_posts": posts, "google_listings": []}
        result = self.agent.perform_task(data)

        self.assertEqual(result["total_posts"], 2)
        # Should not crash

if __name__ == '__main__':
    unittest.main()
