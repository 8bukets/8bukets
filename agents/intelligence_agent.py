from .base_agent import BaseAgent, Blackboard
import os
import json

class IntelligenceAgent(BaseAgent):
    def __init__(self):
        super().__init__("IntelligenceAgent", dependencies=["analysis_stats", "research_data", "google_edge_knowledge", "google_innovation_ai_knowledge", "google_models_research_knowledge"], provides=["intelligence_insights", "synchronization_level"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Running Intelligence Synchronization & External World Collaboration...")

        analysis = blackboard.get("analysis_stats", {})
        research = blackboard.get("research_data", {})

        insights = []

        # 1. Internal Logic
        top_cats = analysis.get("top_categories", {})
        if "Ad Ads Advertise" in top_cats:
            insights.append("High concentration of advertising-related content.")

        # 2. Synchronize with Research (Blackboard Collaboration)
        market_trends = research.get("market_trends", [])
        for trend in market_trends:
            insights.append(f"Synchronized Trend: {trend}")

        # 3. Synchronize with Telemetry (External Investigation Collaboration)
        # In a more advanced system, we'd query the TelemetryManager directly or use a shared event bus.
        # Here we check the research results which already integrated the telemetry-derived investigations.
        for investigation in research.get("external_investigations", []):
            if investigation.get("world_context") == "GOOGLE_WORLD":
                insights.append(f"External World Insight: {investigation['domain']} is an active node in the Google World.")

        competitors = research.get("competitor_analysis", {})
        if competitors:
            top_comp = max(competitors.values(), key=lambda x: x['relevance'] == 'High', default=None)
            if top_comp:
                insights.append(f"Strategic Focus: {top_comp['findings']}")

        # 4. Integrate Google Edge Knowledge
        edge_knowledge = blackboard.get("google_edge_knowledge", {})
        if edge_knowledge and "sections" in edge_knowledge:
            insights.append(f"Google Edge Knowledge Integrated: {len(edge_knowledge['sections'])} sections extracted.")
            if len(edge_knowledge["sections"]) > 0:
                first_heading = edge_knowledge["sections"][0].get("heading", "N/A")
                insights.append(f"Top Edge AI Insight: {first_heading}")

        # 5. Integrate Innovation & AI Knowledge
        innovation_knowledge = blackboard.get("google_innovation_ai_knowledge", {})
        if innovation_knowledge and "articles" in innovation_knowledge:
            insights.append(f"Innovation & AI Knowledge Integrated: {len(innovation_knowledge['articles'])} articles found.")
            if len(innovation_knowledge["articles"]) > 0:
                top_article = innovation_knowledge["articles"][0].get("title", "N/A")
                insights.append(f"Top Innovation Insight: {top_article}")

        # 6. Integrate Models & Research Knowledge
        research_knowledge = blackboard.get("google_models_research_knowledge", {})
        if research_knowledge and "articles" in research_knowledge:
            insights.append(f"Models & Research Knowledge Integrated: {len(research_knowledge['articles'])} articles found.")
            if len(research_knowledge["articles"]) > 0:
                top_research = research_knowledge["articles"][0].get("title", "N/A")
                insights.append(f"Top Research Insight: {top_research}")

        return {
            "intelligence_insights": insights,
            "synchronization_level": "ADVANCED_COLABORATIVE"
        }
