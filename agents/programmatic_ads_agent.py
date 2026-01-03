from typing import List, Dict, Any
from .base_agent import BaseAgent
import random

class ProgrammaticAdsAgent(BaseAgent):
    def __init__(self):
        super().__init__("Programmatic Ads Agent")

    def run(self, data: List[Dict[str, Any]], dna: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Generates ad campaigns, targeting strategies, and bids based on DNA and Data.
        """
        if not dna:
            dna = {} # Fallback

        bid_strategy = dna.get("bid_strategy", {})
        aggressiveness = bid_strategy.get("aggressiveness", 0.5)
        budget_split = bid_strategy.get("budget_allocation", {})

        # Analyze content to find targeting keywords
        keywords = set()
        for post in data[:10]: # Analyze top 10 recent posts
            title_words = post.get("title", "").split()
            keywords.update([w for w in title_words if len(w) > 4])

        # Simulate Campaign Creation
        campaigns = []
        platforms = ["Search", "Display", "Video"]

        for platform in platforms:
            allocation = budget_split.get(platform.lower(), 0.33)
            base_bid = 1.0 * aggressiveness

            # Smart Bidding Logic
            if platform == "Search":
                final_bid = base_bid * 1.5 # Search usually higher CPC
            elif platform == "Video":
                final_bid = base_bid * 1.2
            else:
                final_bid = base_bid

            campaigns.append({
                "platform": platform,
                "budget_allocation": f"{allocation*100:.1f}%",
                "target_bid": round(final_bid, 2),
                "targeting_keywords": list(keywords)[:5],
                "strategy": "Maximize Conversions" if aggressiveness > 0.7 else "Target CPA"
            })

        return {
            "campaigns": campaigns,
            "total_keywords_identified": len(keywords),
            "aggressiveness_level": aggressiveness
        }
