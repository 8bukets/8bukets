from .base import BaseAgent
from typing import Any, Dict
import random

class CreativityAgent(BaseAgent):
    def __init__(self):
        super().__init__("CreativityAgent")

    async def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        intelligence = context.get("intelligence", {})
        top_keywords = [k[0] for k in intelligence.get("top_keywords", [])]

        if not top_keywords:
            return {"creativity": {"ideas": ["Write about current events.", "Review a popular tool."]}}

        self.log("Generating creative content ideas...")

        templates = [
            "The Ultimate Guide to {keyword}",
            "Why {keyword} is the Future of Marketing",
            "10 Tips for {keyword} Success",
            "How to Master {keyword} in 2024",
            "{keyword} vs. The Competition: What You Need to Know"
        ]

        ideas = []
        for _ in range(5):
            keyword = random.choice(top_keywords).capitalize()
            template = random.choice(templates)
            ideas.append(template.format(keyword=keyword))

        return {
            "creativity": {
                "generated_ideas": list(set(ideas))
            }
        }
