from .base_agent import BaseAgent
from typing import Dict, List
import html

class ContentAgent(BaseAgent):
    def __init__(self):
        super().__init__("Content Agent")

    def process(self, data: List[Dict], insights: Dict) -> str:
        self.log("Generating content...")

        articles = "\n".join([f"- {html.escape(str(item.get('title') or ''))} ({html.escape(str(item.get('date', 'N/A')))})" for item in data])

        focus_areas = insights.get('focus_areas', [])
        # Ensure focus areas are strings and escape them
        safe_focus = [html.escape(str(f)) for f in focus_areas]
        focus = ", ".join(safe_focus)

        # Escape strategic insight as well
        strategic_insight = html.escape(str(insights.get('strategic_insight', '')))

        blog_post = f"""
# Oracle Database @ Google Cloud Update

## Latest Developments
{articles}

## Analysis
The market is currently in a {strategic_insight} state.
Key focus areas include: {focus}.

## Takeaway
Enterprises should prepare for multi-cloud data strategies leveraging these new availabilities.
"""
        return blog_post
