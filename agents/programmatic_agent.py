from .base_agent import BaseAgent

class ProgrammaticAgent(BaseAgent):
    def __init__(self):
        super().__init__("Programmatic Agent")

    def run(self, data: dict) -> dict:
        """
        Collaborates and packages ads, targeting, and bids.
        Input: dict containing 'ads', 'targeting', 'bid'.
        """
        ads = data.get('ads', {}).get('ad_campaigns', [])
        targeting = data.get('targeting', {}).get('audience_segments', [])
        bids = data.get('bid', {}).get('bid_strategy', [])

        full_campaigns = []

        # Match them up (simple 1-to-1 or round robin)
        for i, ad in enumerate(ads):
            target = targeting[i % len(targeting)] if targeting else {}
            bid = bids[i % len(bids)] if bids else {}

            full_campaigns.append({
                "campaign_name": f"Auto-Campaign-{i+1}",
                "creative": ad,
                "target_audience": target.get("name"),
                "bid": bid.get("suggested_bid"),
                "status": "Ready to Launch"
            })

        return {
            "programmatic_campaigns": full_campaigns,
            "system_status": "Online"
        }
