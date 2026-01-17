from .base_agent import BaseAgent
from typing import List, Dict, Any
from collections import Counter
import re

class IntelligenceAgent(BaseAgent):
    def __init__(self):
        super().__init__("Intelligence Agent")

    async def process(self, data: List[Dict], shared_context: Dict[str, Any], knowledge_base: Dict[str, Any]) -> Dict[str, Any]:
        # Extract keywords from titles
        titles = [p.get('title', '') for p in data if p.get('title')]
        all_text = " ".join(titles)

        # Simple tokenization and stop word removal (very basic)
        words = re.findall(r'\w+', all_text.lower())
        stop_words = {'the', 'a', 'an', 'in', 'on', 'at', 'for', 'to', 'of', 'and', 'with', 'by', 'is', 'it', 'from', 'as', 'be', 'are', 'this', 'that', 'or', 'google', 'ads'}

        filtered_words = [w for w in words if w not in stop_words and len(w) > 3]

        common_words = Counter(filtered_words).most_common(5)

        # SHARE CONTEXT: Write keywords for BidAgent
        shared_context['trending_keywords'] = common_words

        results = {}
        results['Trending Keywords'] = ", ".join([f"{w} ({c})" for w, c in common_words])

        return results
