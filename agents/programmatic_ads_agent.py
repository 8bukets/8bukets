from core.base_agent import BaseAgent
import random

class ProgrammaticAdsAgent(BaseAgent):
    def __init__(self):
        super().__init__("ProgrammaticAdsAgent")

    def run_cycle(self, context):
        strategy = context.get('strategy', {})
        aggressiveness = self.get_parameter('bid_aggressiveness')

        self.log(f"Configuring programmatic ad campaigns (Aggressiveness: {aggressiveness})...")

        # Simulate Targeting
        targeting_criteria = {
            "keywords": [strategy.get('focus_area', 'Tech')],
            "geo": "Global",
            "device": "Mobile" if random.random() > 0.5 else "Desktop"
        }

        # Simulate Bidding
        base_bid = 0.50
        final_bid = base_bid * (1 + aggressiveness)

        campaign = {
            "targeting": targeting_criteria,
            "bid_amount": final_bid,
            "ad_format": "display_banner"
        }

        context['ad_campaign'] = campaign
        self.log(f"Campaign configured with bid: ${final_bid:.2f}")
