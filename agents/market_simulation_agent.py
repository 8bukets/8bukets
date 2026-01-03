from core.base_agent import BaseAgent
import random

class MarketSimulationAgent(BaseAgent):
    def __init__(self):
        super().__init__("MarketSimulationAgent")

    def run_cycle(self, context):
        self.log("Simulating market reaction to content and ads...")

        # Simulate user interaction
        campaign = context.get('ad_campaign', {})
        creative = context.get('ad_creative', {})
        content = context.get('produced_content', {})

        # Determine success probability
        bid = campaign.get('bid_amount', 0.5)
        quality = content.get('quality_potential', 0.5)

        # Market logic: Higher bid + Higher quality = More clicks
        impressions = int(bid * 1000)
        ctr = (quality * 0.05) + (random.random() * 0.02)
        clicks = int(impressions * ctr)

        market_feedback = {
            "impressions": impressions,
            "clicks": clicks,
            "avg_cpc": bid * 0.8, # Second price auction simulation
            "quality_score": quality + (random.random() * 0.1) # Feedback for learning
        }

        context['ad_campaign_results'] = market_feedback
        context['market_feedback'] = market_feedback # For global feedback loop

        self.log(f"Market Simulation Results: {clicks} clicks from {impressions} impressions.")
