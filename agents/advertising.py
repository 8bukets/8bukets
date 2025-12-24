from .base_agent import BaseAgent
import random

class AdvertisingAgent(BaseAgent):
    def __init__(self):
        super().__init__("Advertising")

    def perform_task(self, data):
        # Data comes from Analyzer (top_keywords, top_categories)
        keywords = data.get("top_keywords", [])
        categories = data.get("top_categories", [])

        # 1. Targeting
        target_audience = "General Audience"
        if categories:
            primary_cat = categories[0][0].lower()
            if "tech" in primary_cat or "code" in primary_cat:
                target_audience = "Software Developers, Tech Enthusiasts (18-45)"
            elif "finance" in primary_cat:
                target_audience = "Investors, Business Owners (25-55)"
            elif "info" in primary_cat:
                target_audience = "Information Seekers, Students"

        # 2. Keyword Bidding Simulation
        # Simulate "Google Antigravity" logic: Finding keywords that defy the norm (high value, low competition)
        bid_suggestions = []
        for word, count in keywords[:5]:
            # Simulated logic: rarer words might have lower competition but high specificity
            # We assign a fake CPC value based on word length (just as a heuristic)
            simulated_cpc = round(random.uniform(0.5, 5.0) + (len(word) * 0.1), 2)
            competition = "High" if count > 5 else "Low"

            # "Antigravity" pick: Low competition, Decent CPC
            antigravity_score = "Standard"
            if competition == "Low" and simulated_cpc > 2.0:
                antigravity_score = "Antigravity Opportunity (High Value/Low Comp)"

            bid_suggestions.append({
                "keyword": word,
                "suggested_bid": f"${simulated_cpc}",
                "competition": competition,
                "strategy": antigravity_score
            })

        # 3. Ad Placement Strategy
        placements = [
            "Top Banner - High Visibility",
            "In-Article Native - Better Engagement",
            "Sidebar - Passive Awareness"
        ]

        return {
            "target_audience": target_audience,
            "bid_strategy": bid_suggestions,
            "recommended_placements": placements
        }
