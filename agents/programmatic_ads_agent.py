from .base_agent import BaseAgent
from typing import Dict, List
import random

class ProgrammaticAdsAgent(BaseAgent):
    def __init__(self):
        super().__init__("Programmatic Ads Agent")

    def process(self, keywords: List[tuple], iq_score: float = 25.0) -> Dict:
        self.log("Configuring programmatic ads...")

        top_keywords = [w[0] for w in keywords[:5]]

        # Dynamic bid calculation based on IQ (smarter agents bid more efficiently)
        base_bid = 2.50
        bid_modifier = min(1.5, iq_score / 100.0)
        optimized_bid = base_bid * bid_modifier

        return {
            "targeting": {
                "keywords": top_keywords,
                "audience": ["IT Decision Makers", "Cloud Architects", "DBAs"],
                "platforms": ["LinkedIn", "Google Display Network"]
            },
            "bid_strategy": "Maximize Conversions",
            "autonomous_bid_amount": round(optimized_bid, 2),
            "intelligence_factor": iq_score
        }
