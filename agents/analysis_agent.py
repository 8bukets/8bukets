from .base_agent import BaseAgent
from collections import Counter
from typing import List, Dict
import re

WORD_PATTERN = re.compile(r'\w+')

class AnalysisAgent(BaseAgent):
    def __init__(self):
        super().__init__("Analysis Agent")

    def process(self, data: List[Dict]) -> Dict:
        self.log("Analyzing data...")
        dates = []

        # Generator to yield words from titles
        def word_generator():
            for item in data:
                title = item.get('title', '')
                if item.get('date'):
                    dates.append(item['date'])
                if title:
                    yield from WORD_PATTERN.findall(title.lower())

        # Consumes generator directly into Counter
        common_words = Counter(word_generator()).most_common(10)

        return {
            "total_articles": len(data),
            "common_keywords": common_words,
            "date_range": [min(dates), max(dates)] if dates else []
        }
