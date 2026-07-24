from agents.base_agent import BaseAgent

class IntelligenceAgent(BaseAgent):
    def __init__(self):
        super().__init__("Intelligence")

    async def run(self, data_or_context, blackboard=None) -> dict:
        self.log("Generating intelligence insights...")
        if blackboard is not None:
            context = blackboard
        else:
            context = data_or_context

        # Safe dictionary access
        is_dict = isinstance(context, dict)
        analysis = context.get("analysis", {}) if is_dict else {}

        insights = []

        # Dominance checks
        if isinstance(analysis, dict):
            if analysis.get("top_domains"):
                top_domain = analysis["top_domains"][0]
                insights.append(f"Domain Dominance: '{top_domain[0]}' accounts for {top_domain[1]} links.")

            if analysis.get("top_categories"):
                top_cat = analysis["top_categories"][0]
                insights.append(f"Content Focus: The primary category is '{top_cat[0]}' ({top_cat[1]} posts).")

            # Author checks
            if analysis.get("top_authors"):
                top_author = analysis["top_authors"][0]
                insights.append(f"Key Contributor: {top_author[0]} is the most active author.")

            # Temporal Intelligence
            date_stats = analysis.get("date_stats", {})
            if isinstance(date_stats, dict) and date_stats.get("year_counts"):
                latest_year = date_stats["year_counts"][0]
                insights.append(f"Activity Trend: Peak activity observed in {latest_year[0]}.")

        # Ecosystem / AI Agent checks
        has_ai_agent_knowledge = False
        if is_dict:
            if "ai_agent_knowledge" in context or "KnowledgeAgent" in context or "ai_agents_definitions" in context:
                has_ai_agent_knowledge = True

        if has_ai_agent_knowledge:
            insights.append("AI Agent Knowledge Base Integrated: Ecosystem architecture aligns with ReAct framework and Google Cloud AI Agent definitions.")
            insights.append("System utilizes multi-tiered memory architecture (short-term, long-term, episodic, consensus).")

        # Backward compatibility / mutation
        if is_dict:
            context["intelligence_insights"] = insights
            context["synchronization_level"] = "ADVANCED_COLABORATIVE"

        self.log("Intelligence generation complete.")

        return {
            "intelligence_insights": insights,
            "synchronization_level": "ADVANCED_COLABORATIVE"
        }
