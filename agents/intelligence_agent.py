from agents.base_agent import BaseAgent, Blackboard


class IntelligenceAgent(BaseAgent):
    """
    Synthesizes insights from the data other agents have already placed on the
    shared Blackboard: scraped-content analysis, live research findings, and
    the ecosystem's AI-agent knowledge base.
    """

    def __init__(self):
        super().__init__(
            "Intelligence",
            dependencies=[],
            provides=["intelligence_insights", "strategic_outlook", "categorized_knowledge"],
        )

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.log("Generating intelligence insights...")

        analysis = blackboard.get("analysis_stats", {}) or {}
        research = blackboard.get("research_data", {}) or {}
        edge_knowledge = blackboard.get("google_edge_knowledge", {}) or {}
        innovation_knowledge = blackboard.get("google_innovation_ai_knowledge", {}) or {}
        models_knowledge = blackboard.get("google_models_research_knowledge", {}) or {}
        definitions = blackboard.get("ai_agents_definitions", {}) or {}
        react_details = blackboard.get("react_framework_details", {}) or {}
        tools_list = blackboard.get("google_cloud_tools_list", []) or []

        insights = []

        # Dominance / content-focus checks from the scraped-content analysis.
        top_domains = analysis.get("top_domains") or {}
        if top_domains:
            top_domain = max(top_domains, key=top_domains.get)
            insights.append(f"Domain Dominance: '{top_domain}' accounts for {top_domains[top_domain]} links.")

        top_categories = analysis.get("top_categories") or {}
        if top_categories:
            top_category = max(top_categories, key=top_categories.get)
            insights.append(f"Content Focus: The primary category is '{top_category}' ({top_categories[top_category]} posts).")
            if any("ad" in str(cat).lower() for cat in top_categories):
                insights.append("High concentration of advertising-related content.")

        # Live research findings synchronized from the ResearchAgent.
        for trend in research.get("market_trends", []):
            insights.append(f"Synchronized Trend: {trend}")

        # External knowledge integration.
        if edge_knowledge.get("sections"):
            insights.append("Google Edge Knowledge Integrated")
        if innovation_knowledge.get("articles"):
            insights.append(f"Google Innovation AI Knowledge Integrated ({len(innovation_knowledge['articles'])} articles).")
        if models_knowledge.get("articles"):
            insights.append(f"Google Models Research Knowledge Integrated ({len(models_knowledge['articles'])} articles).")

        # Ecosystem architecture insights derived from the AI-agent knowledge base.
        react_content = react_details.get("react-agent-deployment-logic") or definitions.get("react-agent-deployment-logic")
        if react_content:
            insights.append("Ecosystem architecture aligns with ReAct framework for reasoning and acting.")

        if definitions.get("memory_definition"):
            insights.append("Verified Multi-tiered Memory across short-term, long-term, episodic and consensus stores.")

        if tools_list:
            insights.append(f"Google Cloud AI Agent definitions synchronized across {len(tools_list)} cataloged tools.")

        strategic_outlook = {
            "top_domain": next(iter(top_domains), None),
            "top_category": next(iter(top_categories), None),
            "market_trends": research.get("market_trends", []),
        }

        categorized_knowledge = {
            "analysis": analysis,
            "research": research,
            "external_knowledge": {
                "google_edge": edge_knowledge,
                "google_innovation_ai": innovation_knowledge,
                "google_models_research": models_knowledge,
            },
            "ai_agent_definitions": definitions,
        }

        self.log("Intelligence generation complete.")

        return {
            "intelligence_insights": insights,
            "strategic_outlook": strategic_outlook,
            "categorized_knowledge": categorized_knowledge,
        }
