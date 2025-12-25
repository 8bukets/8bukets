from .base_agent import BaseAgent
import random

class AdsAgent(BaseAgent):
    def __init__(self):
        super().__init__("AdsAgent")

    def run(self, context):
        keywords = context.get('top_keywords', [])
        self.log("Calculating autonomous ad targeting bids...")

        # Simulate programmatic bidding logic
        ad_campaigns = []
        for kw in keywords:
            bid = round(random.uniform(0.5, 5.0), 2)
            relevance = random.randint(1, 10)
            campaign = {
                "keyword": kw,
                "suggested_bid": bid,
                "relevance_score": relevance,
                "strategy": "Maximize Conversions" if relevance > 8 else "Maximize Clicks"
            }
            ad_campaigns.append(campaign)

        # Sort by relevance
        ad_campaigns.sort(key=lambda x: x['relevance_score'], reverse=True)
        top_campaigns = ad_campaigns[:5]

        self.learn("ad_strategy", top_campaigns)
        return {"campaigns": top_campaigns}
