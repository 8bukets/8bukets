from .base_agent import BaseAgent
import random

class BidAgent(BaseAgent):
    def __init__(self):
        super().__init__("Bid Agent")
        self.base_bid = 1.00

    def run(self, data: dict) -> dict:
        """
        Calculates optimal bids.
        Input: dict containing 'monetization' and 'ads' results.
        """
        ads_out = data.get('ads', {})
        campaigns = ads_out.get('ad_campaigns', [])

        bids = []

        # Load historical bid performance
        mem = self.memory.load_memory()
        bid_multiplier = mem.get("learnings", {}).get("bid_multiplier", 1.1)

        for camp in campaigns:
            # Simple logic: more keywords = higher bid
            kw_count = len(camp.get('keywords', []))
            bid_amount = self.base_bid + (kw_count * 0.5) * bid_multiplier

            bids.append({
                "campaign": camp.get('headline'),
                "suggested_bid": round(bid_amount, 2),
                "strategy": "Maximize Clicks" if bid_amount < 2.0 else "Target CPA"
            })

        return {
            "bid_strategy": bids
        }
