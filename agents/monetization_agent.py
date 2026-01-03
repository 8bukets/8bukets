from core.base_agent import BaseAgent
import random

class MonetizationAgent(BaseAgent):
    def __init__(self):
        super().__init__("MonetizationAgent")

    def run_cycle(self, context):
        self.log("Managing AdSense monetization simulation...")

        # Calculate simulated revenue based on content quality and ad bids
        content = context.get('produced_content', {})
        ads_performance = context.get('ad_campaign_results', {})

        base_revenue = 0.01 # Daily baseline

        # Revenue from content quality
        if content:
            base_revenue += content.get('quality_potential', 0) * 10.0

        # Revenue from successful ad bids
        clicks = ads_performance.get('clicks', 0)
        cpc = ads_performance.get('avg_cpc', 0.5)
        ad_revenue = clicks * cpc

        total_cycle_revenue = base_revenue + ad_revenue

        context['financials'] = {
            "cycle_revenue": total_cycle_revenue,
            "source": "AdSense_Simulation"
        }

        self.log(f"Cycle Revenue Generated: ${total_cycle_revenue:.2f}")
