import random
from agents.base_agent import BaseAgent

class MarketSimulationAgent(BaseAgent):
    """Simulates market reaction to the system's output."""

    def __init__(self):
        super().__init__("MarketSimulation")

    def process(self, system_output: dict, dna: dict) -> dict: # pylint: disable=unused-argument
        """
        Simulates market reaction to the system's output.
        Returns a 'profit' or 'score' metric.
        """
        self.log("Simulating market reaction...")

        # Extract parameters from DNA
        ads_params = dna['agents']['programmatic_ads']
        content_params = dna['agents']['content_creation']

        # Simulate User Engagement based on Content Quality
        # Higher creativity + moderate length = better engagement
        engagement_score = (content_params['creativity_temperature'] * 0.6) + \
                           (min(content_params['length_preference'], 1.5) * 0.4)

        # Simulate Revenue based on Ads
        # Higher aggressiveness = more revenue but potentially lower engagement (churn)
        ad_revenue = ads_params['bid_aggressiveness'] * ads_params['ad_frequency'] * 1000

        # Churn factor: if ads are too frequent, engagement drops
        churn = ads_params['ad_frequency'] * 0.8

        net_score = (engagement_score * 100) + ad_revenue - (churn * 50)

        # Add some randomness (market volatility)
        net_score += random.uniform(-10, 10)

        feedback = {
            "engagement_score": engagement_score,
            "ad_revenue": ad_revenue,
            "net_score": net_score,
            "feedback_text": "Market reacted positively." if net_score > 50 else "Market reaction was tepid."
        }

        self.log(f"Market Feedback: {feedback}")
        return feedback
