from .base_agent import BaseAgent, Blackboard

class CreativityAgent(BaseAgent):
    def __init__(self):
        super().__init__("CreativityAgent", dependencies=["intelligence_insights"], provides=["creative_concepts"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Running Creativity Session...")

        insights = blackboard.get("intelligence_insights", [])

        concepts = [
            "5 Trends Shaping the Future",
            "Why Your Strategy Needs a Reboot",
            "Monetization: Beyond the Basics"
        ]

        if any("advertising" in str(insight).lower() for insight in insights):
            concepts.append("Deep Dive: High concentration of advertising-related content.")

        return {"creative_concepts": concepts}
