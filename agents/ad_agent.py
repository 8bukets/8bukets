from agents.base_agent import BaseAgent
import random

class AdAgent(BaseAgent):
    def __init__(self, name: str = "Ad/Targeting"):
        super().__init__(name)

    async def process(self, data: dict) -> dict:
        """
        Simulates programmatic advertising logic.
        Expects 'insights' from AnalysisAgent or 'content' from ContentAgent.
        """
        self.log("Calculating ad targeting parameters...")

        # Simulate targeting based on categories
        insights = data.get("insights", {})
        bid_aggressiveness = data.get("bid_aggressiveness", 1.0) # Default to 1.0 if not provided

        top_cats = [c[0] for c in insights.get("top_categories", [])]

        target_segments = top_cats if top_cats else ["General Audience"]

        # Simulate Real-Time Bidding (RTB)
        bid_floor = 0.50
        bid_ceiling = 5.00

        # Apply intelligence aggressiveness to the bid calculation
        raw_bid = random.uniform(bid_floor, bid_ceiling)
        calculated_bid = round(raw_bid * bid_aggressiveness, 2)

        ad_campaign = {
            "target_segments": target_segments,
            "bid_strategy": "CPC",
            "suggested_bid": calculated_bid,
            "platform": "Google AdManager (Simulated)",
            "status": "Ready to Deploy"
        }

        self.log(f"Ad campaign prepared: Bid ${calculated_bid} (Aggressiveness: {bid_aggressiveness}) for {target_segments}")
        return {"status": "success", "campaign": ad_campaign}

class MonetizationAgent(BaseAgent):
    def __init__(self, name: str = "Monetization"):
        super().__init__(name)

    async def process(self, data: dict) -> dict:
        """
        Projects revenue.
        Expects 'campaign' from AdAgent.
        """
        campaign = data.get("campaign", {})
        bid = campaign.get("suggested_bid", 0)

        self.log("Projecting revenue...")

        # Simple simulation
        estimated_clicks = random.randint(100, 10000)
        estimated_cost = estimated_clicks * bid
        estimated_revenue = estimated_cost * random.uniform(1.2, 2.0) # ROI 20-100%
        roi = ((estimated_revenue - estimated_cost) / estimated_cost) * 100 if estimated_cost > 0 else 0

        financial_report = {
            "estimated_cost": round(estimated_cost, 2),
            "estimated_revenue": round(estimated_revenue, 2),
            "projected_roi": f"{round(roi, 1)}%",
            "verdict": "PROFITABLE" if roi > 0 else "REVIEW NEEDED"
        }

        self.log(f"Financial projection: ROI {financial_report['projected_roi']}")
        return {"status": "success", "financials": financial_report}
