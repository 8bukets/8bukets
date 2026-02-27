from .base_agent import BaseAgent
from datetime import datetime

class ContentAgent(BaseAgent):
    execution_stage = 5
    def __init__(self):
        super().__init__("ContentAgent")

    async def run(self, data: list, context: dict) -> dict:
        self.logger.info("Generating Content...")

        angles = context.get("creative_angles", [])
        title = angles[0] if angles else "Daily Ad Tech Update"

        body = f"Title: {title}\n\n"
        body += f"Date: {datetime.now().strftime('%Y-%m-%d')}\n\n"
        body += "Introduction:\n"
        body += "In today's fast-paced digital landscape, understanding market position is crucial. "
        body += "Our latest analysis reveals significant shifts in the ecosystem.\n\n"

        body += "Key Takeaways:\n"
        for insight in context.get("intelligence_insights", []):
            body += f"- {insight}\n"

        return {"generated_content": body}
