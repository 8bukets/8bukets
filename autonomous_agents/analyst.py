from .base import BaseAgent
from collections import Counter

class AnalystAgent(BaseAgent):
    def __init__(self):
        super().__init__("Analyst")

    def run(self, context):
        data = context.get('scraped_data', [])
        if not data:
            self.log_activity("No data to analyze.")
            return

        self.log_activity(f"Analyzing {len(data)} items...")

        # Simple analysis: Count words in titles
        words = []
        for post in data:
            words.extend(post['title'].lower().split())

        common_words = Counter(words).most_common(3)
        context['analysis_report'] = {
            "total_posts": len(data),
            "top_keywords": common_words
        }
        self.learn(f"Top keywords identified: {common_words}")
