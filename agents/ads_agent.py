"""
Ads Agent module.
Responsible for programmatic advertising, bidding, and cookie management.
"""
import random
from .base_agent import BaseAgent

class AdsAgent(BaseAgent):
    """
    AdsAgent manages cookies and places bids on content.
    """
    def __init__(self):
        super().__init__("AdsAgent")
        self.cookies = {} # 1st party cookies

    def manage_cookies(self, user_id, data):
        """Simulate cookie management for targeting."""
        if user_id not in self.cookies:
            self.cookies[user_id] = {}
        self.cookies[user_id].update(data)
        # Simulate 3rd party sync
        self.log_activity(f"Synced cookies for user {user_id}: {data}")

    def place_bids(self, content_items):
        """
        Places bids on the generated content items.
        """
        aggressiveness = self.get_parameter("bid_aggressiveness")
        targeting = self.get_parameter("ad_targeting_precision")

        bids = []
        for item in content_items:
            # Simulate bidding logic
            base_value = item['quality'] * 10
            bid_amount = base_value * aggressiveness * random.uniform(0.9, 1.1)

            # Simulate targeting check
            matched_audience = random.random() < targeting

            if matched_audience:
                bid_amount *= 1.5 # Premium for matched audience

            bids.append({
                "content": item['topic'],
                "bid": bid_amount,
                "targeted": matched_audience
            })
            self.log_activity(
                f"Placed bid ${bid_amount:.2f} for {item['topic']} (Targeted: {matched_audience})"
            )

        return bids
