from .base_agent import BaseAgent

class MonetizationAgent(BaseAgent):
    def __init__(self):
        super().__init__("MonetizationAgent")

    async def run(self, data: list, context: dict) -> dict:
        self.logger.info("Running Monetization Analysis...")

        keywords = ["affiliate", "program", "earn", "money", "monetize", "revenue"]
        opportunities = []

        for post in data:
            title = post.get('title', '').lower()
            if any(k in title for k in keywords):
                opportunities.append(post.get('title'))

        # Limit to top 5
        return {"monetization_opportunities": opportunities[:5]}
