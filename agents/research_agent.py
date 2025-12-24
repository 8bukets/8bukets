import re
from collections import Counter
from .base_agent import BaseAgent

class ResearchAgent(BaseAgent):
    def __init__(self):
        super().__init__("Research Agent")
        self.stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'}

    def run(self, data: list) -> dict:
        """
        Extracts key topics/entities from titles to simulate 'research'.
        """
        if not data:
            return {}

        words = []
        for post in data:
            title = post.get('title')
            if title:
                # Simple tokenization
                tokens = re.findall(r'\b\w+\b', title.lower())
                filtered = [w for w in tokens if w not in self.stop_words and len(w) > 3]
                words.extend(filtered)

        topic_counts = Counter(words).most_common(20)

        return {
            "trending_keywords": [t[0] for t in topic_counts],
            "research_notes": f"Identified {len(topic_counts)} trending topics based on frequency analysis."
        }
