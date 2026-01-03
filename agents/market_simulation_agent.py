from typing import List, Dict, Any
from .base_agent import BaseAgent
import random

class MarketSimulationAgent(BaseAgent):
    def __init__(self):
        super().__init__("Market Simulation Agent")

    def run(self, data: List[Dict[str, Any]], dna: Dict[str, Any] = None, agent_outputs: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Simulates market reaction to the content and ads.
        Returns a 'feedback' dictionary.
        """
        # Quality score based on content analysis (mocked)
        content_quality = random.uniform(0.6, 1.0)

        # Ads Effectiveness
        ads_output = agent_outputs.get("Programmatic Ads Agent", {})
        aggressiveness = ads_output.get("aggressiveness_level", 0.5)

        # Market Logic:
        # Too aggressive might annoy users (lower score)
        # Too passive might miss opportunities
        # Optimal point is dynamic, let's simulate a 'current trend'
        market_trend_aggressiveness = random.uniform(0.4, 0.8)

        ad_performance = 1.0 - abs(aggressiveness - market_trend_aggressiveness)

        overall_score = (content_quality * 0.4) + (ad_performance * 0.6)

        return {
            "market_score": overall_score,
            "engagement_score": content_quality,
            "ad_performance": ad_performance,
            "market_feedback": "Market responded well." if overall_score > 0.7 else "Market was lukewarm."
        }
