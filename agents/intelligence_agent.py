from .base_agent import BaseAgent, Blackboard
import os
import json

class IntelligenceAgent(BaseAgent):
    def __init__(self):
        super().__init__("IntelligenceAgent", dependencies=["analysis_stats", "research_data", "google_edge_knowledge", "google_innovation_ai_knowledge", "google_models_research_knowledge"], provides=["intelligence_insights", "synchronization_level", "strategic_outlook", "categorized_knowledge"])

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

        # 5. Categorize and Synthesize Google AI Knowledge
        google_knowledge_sources = [
            blackboard.get("google_innovation_ai_knowledge", {}),
            blackboard.get("google_models_research_knowledge", {}),
            blackboard.get("google_edge_knowledge", {})
        ]

        all_articles = []
        for source in google_knowledge_sources:
            if "articles" in source:
                all_articles.extend(source["articles"])
            elif "sections" in source: # Edge knowledge format
                for section in source["sections"]:
                    all_articles.append({
                        "title": section.get("heading", ""),
                        "snippet": section.get("content", "")
                    })

        categories = {
            "Models & Gemini": [],
            "Research & DeepMind": [],
            "Infrastructure & Cloud": [],
            "Products & Tools": [],
            "Safety & Privacy": []
        }

        keywords = {
            "Models & Gemini": ["gemini", "gemma", "llm", "embedding", "multimodal", "token"],
            "Research & DeepMind": ["research", "deepmind", "agi", "quantum", "science", "framework"],
            "Infrastructure & Cloud": ["infrastructure", "cloud", "network", "energy", "compute", "global"],
            "Products & Tools": ["app", "developer", "tool", "notebooklm", "search", "api", "vibe"],
            "Safety & Privacy": ["safety", "security", "privacy", "protecting", "compliance", "policy"]
        }

        for article in all_articles:
            text = (article.get("title", "") + " " + article.get("snippet", "")).lower()
            categorized = False
            for cat, kws in keywords.items():
                if any(kw in text for kw in kws):
                    categories[cat].append(article.get("title"))
                    categorized = True
                    break
            if not categorized:
                # Default to General Innovation
                if "General Innovation" not in categories:
                    categories["General Innovation"] = []
                categories["General Innovation"].append(article.get("title"))

        for cat, titles in categories.items():
            if titles:
                insights.append(f"Strategic Node [{cat}]: Found {len(titles)} relevant updates.")
                insights.append(f"  - Lead insight: {titles[0]}")

        # 6. Strategic Risk & Opportunity Assessment
        assessment = "Positive outlook on multimodal scaling and autonomous research agents."
        if len(categories["Safety & Privacy"]) > 0:
            assessment += " Strategic focus on privacy-preserving AI and security frameworks detected."
        if len(categories["Infrastructure & Cloud"]) > 0:
            assessment += " Infrastructure expansion indicates preparation for massive-scale deployment."

        return {
            "intelligence_insights": insights,
            "strategic_outlook": assessment,
            "synchronization_level": "ADVANCED_COLABORATIVE",
            "categorized_knowledge": {k: v for k, v in categories.items() if v}
        }
