from .base_agent import BaseAgent

class IntelligenceAgent(BaseAgent):
    def __init__(self):
        super().__init__("IntelligenceAgent")

    async def run(self, data: list, context: dict) -> dict:
        self.logger.info("Running Intelligence...")

        # Synthesize findings
        analysis = context.get("analysis_stats", {})
        research = context.get("research_notes", [])

        insights = []

        # Insight 1: Dominance
        top_cats = analysis.get("top_categories", {})
        if "Ad Ads Advertise" in top_cats:
            insights.append("High concentration of advertising-related content.")

        # Insight 2: Context
        if any("google" in note.lower() for note in research):
            insights.append("Google ecosystem is a primary focus area.")

        return {"intelligence_insights": insights}
