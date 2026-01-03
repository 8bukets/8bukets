"""
Market Agent module.
Responsible for simulating market feedback (revenue, engagement).
"""
import random
from .base_agent import BaseAgent

class MarketAgent(BaseAgent):
    """
    MarketAgent simulates the external environment's response to the system's actions.
    """
    def __init__(self):
        super().__init__("MarketAgent")

    def simulate_market_response(self, bids):
        """Simulates the market's reaction to the content and ads."""
        total_revenue = 0
        total_engagement = 0

        for bid in bids:
            # Simulate random market fluctuation
            market_factor = random.uniform(0.5, 1.5)

            # Revenue depends on bid amount and market factor
            revenue = bid['bid'] * market_factor

            # Engagement
            engagement = revenue * 0.1

            total_revenue += revenue
            total_engagement += engagement

        self.log_activity(
            f"Market Simulation Results: Revenue=${total_revenue:.2f}, Engagement={total_engagement:.2f}"
        )

        return {
            "revenue": total_revenue,
            "engagement": total_engagement
        }
