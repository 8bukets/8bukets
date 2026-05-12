from .base_agent import BaseAgent, Blackboard

class ContentAgent(BaseAgent):
    def __init__(self):
        super().__init__("ContentAgent", dependencies=["creative_concepts", "intelligence_insights"], provides=["generated_content"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Generating Content...")

        concepts = blackboard.get("creative_concepts", [])
        insights = blackboard.get("intelligence_insights", [])

        title = concepts[0] if concepts else "Autonomous Insight"

        content = f"Title: {title}\n\n"
        content += f"Date: 2026-02-27\n\n"
        content += "Introduction:\nIn today's fast-paced digital landscape, understanding market position is crucial.\n\n"
        content += "Key Takeaways:\n"
        for insight in insights:
            content += f"- {insight}\n"

        return {"generated_content": content}
