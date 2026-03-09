from .base_agent import BaseAgent
from datetime import datetime

class ContentAgent(BaseAgent):
    execution_stage = 5
    def __init__(self):
        super().__init__("ContentAgent")

    async def run(self, data: list, context: dict) -> dict:
        self.logger.info("Generating Content for WordPress...")

        angles = context.get("creative_angles", [])
        title = angles[0] if angles else "Daily Ad Tech Update"

        # 1. Plain text format (legacy/reporting)
        body_text = f"Title: {title}\n\n"
        body_text += f"Date: {datetime.now().strftime('%Y-%m-%d')}\n\n"
        body_text += "Introduction:\n"
        body_text += "In today's fast-paced digital landscape, understanding market position is crucial. "
        body_text += "Our latest analysis reveals significant shifts in the ecosystem.\n\n"

        body_text += "Key Takeaways:\n"
        for insight in context.get("intelligence_insights", []):
            body_text += f"- {insight}\n"

        # 2. HTML format (WordPress integration)
        body_html = f"<h1>{title}</h1>"
        body_html += f"<p><em>Date: {datetime.now().strftime('%Y-%m-%d')}</em></p>"
        body_html += "<section><h2>Introduction</h2>"
        body_html += "<p>In today's fast-paced digital landscape, understanding market position is crucial. "
        body_html += "Our latest analysis reveals significant shifts in the ecosystem.</p></section>"

        body_html += "<section><h2>Key Takeaways</h2><ul>"
        for insight in context.get("intelligence_insights", []):
            body_html += f"<li>{insight}</li>"
        body_html += "</ul></section>"

        # Add RAG Insight
        if context.get("llm_reasoning"):
             body_html += f"<section><h2>AI Insights</h2><blockquote>{context.get('llm_reasoning')}</blockquote></section>"

        return {
            "generated_content": body_text,
            "generated_content_html": body_html,
            "top_pattern": title
        }
