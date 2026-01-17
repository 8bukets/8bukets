from .base_agent import BaseAgent
from typing import Dict, List

class ContentAgent(BaseAgent):
    def __init__(self):
        super().__init__("Content Agent")

    def process(self, data: List[Dict], insights: Dict) -> str:
        self.log("Generating content...")

        articles = "\n".join([f"- {self.escape_markdown(item['title'])} ({item.get('date', 'N/A')})" for item in data])
        focus = ", ".join(insights.get('focus_areas', []))

        blog_post = f"""
# Oracle Database @ Google Cloud Update

## Latest Developments
{articles}

## Analysis
The market is currently in a {insights.get('strategic_insight')} state.
Key focus areas include: {focus}.

## Takeaway
Enterprises should prepare for multi-cloud data strategies leveraging these new availabilities.
"""
        return blog_post
