from .base_agent import BaseAgent
from typing import Dict, List, Any

class ContentAgent(BaseAgent):
    def __init__(self):
        super().__init__("Content Agent")

    def process(self, data: List[Dict], insights: Dict, memory: Dict[str, Any] = None) -> str:
        self.log("Generating content...")

        articles = "\n".join([f"- {item['title']} ({item.get('date', 'N/A')})" for item in data])
        focus = ", ".join(insights.get('focus_areas', []))

        oracle_ai_section = ""
        if memory and 'oracle_ai_knowledge' in memory:
            oracle_ai_knowledge = memory['oracle_ai_knowledge']
            sections = oracle_ai_knowledge.get('sections', [])
            ai_points = [sec['content'] for sec in sections if 'AI' in sec.get('content', '')]

            if ai_points:
                ai_summary = "\n".join([f"- {point}" for point in ai_points[:5]])
                oracle_ai_section = f"""
## Oracle AI Intelligence
{ai_summary}
"""

        blog_post = f"""
# Oracle Database @ Google Cloud Update

## Latest Developments
{articles}

## Analysis
The market is currently in a {insights.get('strategic_insight')} state.
Key focus areas include: {focus}.
{oracle_ai_section}
## Takeaway
Enterprises should prepare for multi-cloud data strategies leveraging these new availabilities.
"""
        return blog_post
