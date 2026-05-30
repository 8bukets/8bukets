from .base_agent import BaseAgent
from collections import Counter
from typing import List, Dict
import re

class AnalysisAgent(BaseAgent):
    def __init__(self):
        super().__init__("Analysis Agent")

    def process(self, data: List[Dict]) -> Dict:
        self.log("Analyzing data...")
        text_corpus = ""
        dates = []
        for item in data:
            text_corpus += item.get('title', '') + " "
            if item.get('date'):
                dates.append(item['date'])

        # Simple keyword frequency
        words = re.findall(r'\w+', text_corpus.lower())
        common_words = Counter(words).most_common(10)

        return {
            "total_articles": len(data),
            "common_keywords": common_words,
            "date_range": [min(dates), max(dates)] if dates else []
        }
