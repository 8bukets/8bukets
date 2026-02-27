from .base_agent import BaseAgent

class IntelligenceAgent(BaseAgent):
    def __init__(self):
        super().__init__("IntelligenceAgent")

    async def run(self, data: list, context: dict) -> dict:
        self.logger.info("Running Intelligence Synchronization...")

        # Synthesize findings from Analysis and Research
        analysis = context.get("analysis_stats", {})
        research = context.get("research_data", {})

        insights = []

        # Insight 1: Dominance
        top_cats = analysis.get("top_categories", {})
        if "Ad Ads Advertise" in top_cats:
            insights.append("High concentration of advertising-related content.")

        # Insight 2: Synchronization with Research
        market_trends = research.get("market_trends", [])
        for trend in market_trends:
            insights.append(f"Synchronized Trend: {trend}")

        # Insight 3: Competitor Intelligence
        competitors = research.get("competitor_analysis", {})
        if competitors:
            top_comp = max(competitors.values(), key=lambda x: x['relevance'] == 'High', default=None)
            if top_comp:
                insights.append(f"Strategic Focus: {top_comp['findings']}")

        return {
            "intelligence_insights": insights,
            "synchronization_level": "ADVANCED"
        }
