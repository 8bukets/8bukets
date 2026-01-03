from .base_agent import BaseAgent
from typing import Dict, Any
import random

class MarketSimulationAgent(BaseAgent):
    def __init__(self):
        super().__init__("Market Simulation Agent")

    def process(self, content_data: Any, ads_config: Dict) -> Dict:
        self.log("Simulating market response...")

        # Simulate a market score based on content and ad config
        base_score = random.uniform(50, 80)

        # Boost score if keywords match high value targets (simulated)
        keywords = ads_config.get("targeting", {}).get("keywords", [])
        if "Cloud" in keywords:
            base_score += 10
        if ads_config.get("bid_strategy") == "Maximize Conversions":
            base_score += 5

        engagement_rate = base_score / 1000.0
        revenue_projection = base_score * 12.5

        return {
            "market_score": base_score,
            "estimated_engagement": f"{engagement_rate:.2%}",
            "projected_revenue": revenue_projection,
            "feedback": "Increase bid aggressiveness for better reach." if base_score < 70 else "Maintain current strategy."
        }
