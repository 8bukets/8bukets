from .base_agent import BaseAgent

class TargetingAgent(BaseAgent):
    execution_stage = 4
    def __init__(self):
        super().__init__("TargetingAgent")

    async def run(self, data: list, context: dict) -> dict:
        self.logger.info("Building Audience Personas...")

        # Collaborate with Intelligence Agent
        insights = context.get("intelligence_insights", [])
        categories = context.get("analysis_stats", {}).get("top_categories", {})

        # Default persona
        primary_persona = "General Tech Enthusiast"

        # Dynamic persona building
        if any("advertising" in str(cat).lower() for cat in categories):
            primary_persona = "AdTech Professional"

        if "Google ecosystem" in str(insights):
            primary_persona += " (Google Stack Focus)"

        # Evolution: Check if persona changed from last run
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
