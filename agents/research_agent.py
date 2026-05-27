from collections import Counter
import re
from .base_agent import BaseAgent

class ResearchAgent(BaseAgent):
    def __init__(self):
        super().__init__("Research Agent")

    def run(self):
        self.log("Starting research...")
        if not self.data:
            return

        # Extract topics from titles
        all_text = " ".join([p.get('title', '') for p in self.data])
        # Simple keyword extraction (ignore common stop words - simplified list)
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'it'}
        words = re.findall(r'\w+', all_text.lower())
        filtered_words = [w for w in words if w not in stop_words and len(w) > 3]

        common_topics = Counter(filtered_words).most_common(20)

        self.results = {
            "trending_keywords": common_topics,
            "sample_titles": [p.get('title') for p in self.data[:5]]
        }
        self.log("Research complete.")
