from .base import Agent
import random

class AdManagerAgent(Agent):
    def __init__(self):
        super().__init__("AdManagerAgent")

    def perform_task(self, context=None):
        """
        Context is expected to contain 'keywords' from AnalystAgent
        and 'opportunities' from MonetizationAgent.
        """
        keywords = context.get('keywords', []) if context else []
        opportunities = context.get('top_opportunities', []) if context else []

        # 1. Targeting
        self.results['targeting'] = self.define_targeting(keywords)

        # 2. Bidding Strategy
        self.results['bidding_strategy'] = self.calculate_bids(keywords)

        # 3. Ad Creatives (Ads)
        self.results['campaigns'] = self.create_campaigns(keywords, opportunities)

    def define_targeting(self, keywords):
        # Infer audience from keywords
        audience = "General Interest"
        if any("fashion" in k[0] for k in keywords):
            audience = "Fashion Enthusiasts, 18-35, Urban"
        elif any("design" in k[0] for k in keywords):
            audience = "Home Decor & Design Professionals"

        return {
            "primary_audience": audience,
            "locations": ["US", "UK", "EU"],
            "devices": ["Mobile", "Desktop"]
        }

    def calculate_bids(self, keywords):
        # Simulate bid calculation based on "competition" (frequency)
        bids = []
        for kw, freq in keywords:
            # Higher freq = higher competition = higher CPC
            cpc = round(0.5 + (freq * 0.1), 2)
            bids.append({"keyword": kw, "suggested_bid": cpc})
        return bids

    def create_campaigns(self, keywords, opportunities):
        campaigns = []

        # Campaign 1: Keyword based
        if keywords:
            top_kw = keywords[0][0]
            campaigns.append({
                "name": f"Search-{top_kw.capitalize()}",
                "headline": f"Best {top_kw.capitalize()} Trends",
                "description": f"Discover the latest in {top_kw}. Shop now!",
                "type": "Search"
            })

        # Campaign 2: Opportunity based
        for opp in opportunities:
            campaigns.append({
                "name": f"Affiliate-{opp['title'][:10]}",
                "headline": f"Deal: {opp['title']}",
                "description": "Limited time offer. Don't miss out.",
                "type": "Display"
            })

        return campaigns
