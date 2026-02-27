from .base_agent import BaseAgent, Blackboard

class IntelligenceAgent(BaseAgent):
    def __init__(self):
        super().__init__("IntelligenceAgent", dependencies=["analysis_stats", "research_data"], provides=["intelligence_insights", "synchronization_level"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Running Intelligence Synchronization...")

        analysis = blackboard.get("analysis_stats", {})
        research = blackboard.get("research_data", {})

        insights = []

        top_cats = analysis.get("top_categories", {})
        if "Ad Ads Advertise" in top_cats:
            insights.append("High concentration of advertising-related content.")

        market_trends = research.get("market_trends", [])
        for trend in market_trends:
            insights.append(f"Synchronized Trend: {trend}")

        competitors = research.get("competitor_analysis", {})
        if competitors:
            top_comp = max(competitors.values(), key=lambda x: x['relevance'] == 'High', default=None)
            if top_comp:
                insights.append(f"Strategic Focus: {top_comp['findings']}")

        return {
            "intelligence_insights": insights,
            "synchronization_level": "ADVANCED"
        }
