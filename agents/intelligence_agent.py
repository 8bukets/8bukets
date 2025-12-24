from .base_agent import BaseAgent
from typing import List, Dict, Any
from collections import Counter
import re

class IntelligenceAgent(BaseAgent):
    def __init__(self):
        super().__init__("Intelligence Agent")

    async def process(self, data: List[Dict]) -> Dict[str, Any]:
        # Extract keywords from titles
        all_text = ""
        for p in data:
            title = p.get('title', '')
            if title:
                all_text += " " + title

        # Simple tokenization and stop word removal (very basic)
        words = re.findall(r'\w+', all_text.lower())
        stop_words = {'the', 'a', 'an', 'in', 'on', 'at', 'for', 'to', 'of', 'and', 'with', 'by', 'is', 'it', 'from', 'as', 'be', 'are', 'this', 'that', 'or', 'google', 'ads'}
        # Added 'google', 'ads' to see more specific trends if possible, or keep them to see dominance

        filtered_words = [w for w in words if w not in stop_words and len(w) > 3]

        common_words = Counter(filtered_words).most_common(5)

        results = {}
        results['Trending Keywords'] = ", ".join([f"{w} ({c})" for w, c in common_words])

        return results
