from .base_agent import BaseAgent
from typing import List, Dict, Any
import random

class ContentAgent(BaseAgent):
    def __init__(self):
        super().__init__("Content Agent")

    async def process(self, data: List[Dict]) -> Dict[str, Any]:
        if not data:
            return {"Daily Briefing": "No data available."}

        # Pick a random interesting article or just summarize
        # Let's count categories
        categories = []
        for p in data:
            if p.get('categories'):
                categories.extend(p['categories'])

        top_cat = "General"
        if categories:
            top_cat = max(set(categories), key=categories.count)

        total = len(data)

        briefing = (
            f"Today's analysis covers {total} new data points. "
            f"The leading topic is '{top_cat}'. "
            "Our autonomous systems are detecting shifts in digital advertising strategies. "
            "Stay tuned for deeper insights."
        )

        return {"Daily Briefing": briefing}
