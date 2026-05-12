from .base_agent import BaseAgent, Blackboard

class TargetingAgent(BaseAgent):
    def __init__(self):
        super().__init__("TargetingAgent", dependencies=["analysis_stats", "intelligence_insights"], provides=["targeting_profile"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Building Audience Personas...")

        insights = blackboard.get("intelligence_insights", [])
        categories = blackboard.get("analysis_stats", {}).get("top_categories", {})

        primary_persona = "General Tech Enthusiast"

        if any("advertising" in str(cat).lower() for cat in categories):
            primary_persona = "AdTech Professional"

        if any("Google ecosystem" in str(insight) for insight in insights):
            primary_persona += " (Google Stack Focus)"

        last_persona = self.get_agent_memory("last_primary_persona")
        if last_persona and last_persona != primary_persona:
            self.logger.info(f"EVOLUTION: Audience shifted from {last_persona} to {primary_persona}")

        self.update_agent_memory("last_primary_persona", primary_persona)

        return {
            "targeting_profile": {
                "primary_persona": primary_persona,
                "keywords": list(categories.keys())[:5],
                "intent": "Research & Optimization"
            }
        }
