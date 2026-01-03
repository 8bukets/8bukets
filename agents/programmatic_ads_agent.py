from .base_agent import BaseAgent
from typing import Dict, List

class ProgrammaticAdsAgent(BaseAgent):
    def __init__(self):
        super().__init__("Programmatic Ads Agent")

    def process(self, keywords: List[tuple]) -> Dict:
        self.log("Configuring programmatic ads...")

        dna = self.load_dna()
        ads_params = dna.get('agents', {}).get('programmatic_ads', {})
        bid_aggro = ads_params.get('bid_aggressiveness', 0.5)

        top_keywords = [w[0] for w in keywords[:5]]

        bid_strategy = "Target CPA" if bid_aggro > 0.7 else "Maximize Conversions"

        return {
            "targeting": {
                "keywords": top_keywords,
                "audience": ["IT Decision Makers", "Cloud Architects", "DBAs"],
                "platforms": ["LinkedIn", "Google Display Network"]
            },
            "bid_strategy": bid_strategy,
            "bid_multiplier": bid_aggro,
            "frequency_cap": ads_params.get('ad_frequency', 0.5) * 10
        }
