from .base_agent import BaseAgent
from typing import Dict, List

class ProgrammaticAdsAgent(BaseAgent):
    def __init__(self):
        super().__init__("Programmatic Ads Agent")

    def process(self, keywords: List[tuple], iq: int = 25) -> Dict:
        self.log(f"Configuring programmatic ads (IQ: {iq})...")

        top_keywords = [w[0] for w in keywords[:5]]

        # IQ-driven optimization
        platforms = ["LinkedIn", "Google Display Network"]
        bid_strategy = "Maximize Conversions"
        audience = ["IT Decision Makers", "Cloud Architects", "DBAs"]

        if iq >= 30:
            platforms.append("Programmatic Video (CTV)")
            bid_strategy = "Target ROAS (Return On Ad Spend)"
        if iq >= 50:
            audience.append("Competitor Conquesting")
            bid_strategy = "Predictive LTV Bidding"

        return {
            "targeting": {
                "keywords": top_keywords,
                "audience": audience,
                "platforms": platforms
            },
            "bid_strategy": bid_strategy,
            "system_iq_used": iq
        }
