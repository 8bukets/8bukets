from agents.base_agent import BaseAgent

class IntelligenceAgent(BaseAgent):
    def __init__(self):
        super().__init__("Intelligence")

    async def run(self, context: dict):
        self.log("Generating intelligence insights...")
        analysis = context.get("analysis", {})

        insights = []

        # Dominance checks
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
        if date_stats.get("year_counts"):
            latest_year = date_stats["year_counts"][0]
            insights.append(f"Activity Trend: Peak activity observed in {latest_year[0]}.")

        context["intelligence_insights"] = insights
        self.log("Intelligence generation complete.")
