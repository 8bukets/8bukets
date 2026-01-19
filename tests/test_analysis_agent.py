import unittest
from agents.analysis_agent import AnalysisAgent

class TestAnalysisAgent(unittest.TestCase):
    def test_process(self):
        data = [
            {"title": "Python is great", "date": "2023-01-01"},
            {"title": "Python is fast", "date": "2023-01-02"},
            {"title": "Java is okay", "date": "2023-01-03"},
        ]
        agent = AnalysisAgent()
        result = agent.process(data)

        self.assertEqual(result["total_articles"], 3)

        # Check common keywords
        # "python": 2, "is": 3, "great": 1, "fast": 1, "java": 1, "okay": 1
        keywords = dict(result["common_keywords"])
        self.assertEqual(keywords.get("python"), 2)
        self.assertEqual(keywords.get("is"), 3)
        self.assertEqual(keywords.get("java"), 1)

        # Check date range
        self.assertEqual(result["date_range"], ["2023-01-01", "2023-01-03"])

    def test_empty_data(self):
        agent = AnalysisAgent()
        result = agent.process([])
        self.assertEqual(result["total_articles"], 0)
        self.assertEqual(result["common_keywords"], [])
        self.assertEqual(result["date_range"], [])

    def test_missing_dates(self):
        data = [
            {"title": "No date here"},
            {"title": "Another title", "date": "2023-01-01"}
        ]
        agent = AnalysisAgent()
        result = agent.process(data)
        self.assertEqual(result["total_articles"], 2)
        self.assertEqual(result["date_range"], ["2023-01-01", "2023-01-01"])

if __name__ == '__main__':
    unittest.main()
