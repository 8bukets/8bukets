from .base import BaseAgent
from typing import Any, Dict
from collections import Counter
import re

class IntelligenceAgent(BaseAgent):
    def __init__(self):
        super().__init__("IntelligenceAgent")

    async def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        data = context.get("scraped_data", [])
        if not data:
            return {"intelligence": {}}

        self.log("Extracting intelligence (keywords and trends)...")

        # Simple keyword extraction from titles
        words = []
        ignore_words = {'the', 'a', 'an', 'in', 'on', 'at', 'for', 'to', 'of', 'and', 'or', 'with', 'by', 'is', 'are', 'https', 'com', 'www', 'advertisement'}

        for p in data:
            title = p.get('title', '').lower()
            # Remove punctuation
            title = re.sub(r'[^\w\s]', '', title)
            for word in title.split():
                if len(word) > 3 and word not in ignore_words:
                    words.append(word)

        keyword_counts = Counter(words).most_common(10)

        # Author trends
        authors = [p.get('author') for p in data if p.get('author')]
        top_authors = Counter(authors).most_common(3)

        return {
            "intelligence": {
                "top_keywords": keyword_counts,
                "top_authors": top_authors
            }
        }
