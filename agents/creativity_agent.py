from .base_agent import BaseAgent
import random

class CreativityAgent(BaseAgent):
    def __init__(self):
        super().__init__("CreativityAgent")

    async def run(self, data: list, context: dict) -> dict:
        self.logger.info("Running Creativity Session...")

        insights = context.get("intelligence_insights", [])

        angles = [
            "The Hidden Truth About Ad Tech",
            "Why Your Strategy Needs a Reboot",
            "5 Trends Shaping the Future",
            "Monetization: Beyond the Basics"
        ]

        selected_angles = random.sample(angles, 2)
        if insights:
            selected_angles.append(f"Deep Dive: {insights[0]}")

        return {"creative_angles": selected_angles}
