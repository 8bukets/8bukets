import unittest
import sys
import os

# Add root to path so we can import agents
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.analyzer import AnalyzerAgent

class TestAnalyzerAgent(unittest.TestCase):
    def setUp(self):
        self.agent = AnalyzerAgent()

    def test_perform_task(self):
        data = {
            "blog_posts": [
                {
                    "content": "Python is an amazing programming language. It is great for data science.",
                    "categories": ["tech", "python"]
                },
                {
                    "content": "Coding is fun and challenging. Performance optimization is key.",
                    "categories": ["tech", "coding"]
                }
            ],
            "google_listings": []
        }

        result = self.agent.perform_task(data)

        self.assertEqual(result["total_posts"], 2)
        # Categories should be tech(2), python(1), coding(1)
        # Note: top_categories returns list of tuples [('tech', 2), ...]
        cats = dict(result["top_categories"])
        self.assertEqual(cats.get("tech"), 2)

        self.assertTrue(result["average_sentiment"] > 0) # Should be positive

        # Keywords check
        keywords = [k[0] for k in result["top_keywords"]]
        # "programming" > 4 chars
        self.assertTrue("programming" in keywords or "amazing" in keywords or "python" in keywords)

    def test_empty_input(self):
        data = {"blog_posts": []}
        result = self.agent.perform_task(data)
        self.assertEqual(result["total_posts"], 0)
        self.assertEqual(result["average_sentiment"], 0)

if __name__ == '__main__':
    unittest.main()
