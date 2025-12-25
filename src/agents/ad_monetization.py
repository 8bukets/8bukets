from .base import BaseAgent
import random

class AdAgent(BaseAgent):
    def setup(self):
        self.bus.subscribe("content_enhanced", self.place_ads)

    def place_ads(self, topic, message):
        content_title = message["content"].get("title")
        self.log(f"Calculating ad placements for: {content_title}")

        # Simulate targeting and bidding
        bid_price = round(random.uniform(0.5, 5.0), 2)
        target_audience = random.choice(["Tech Enthusiasts", "Marketers", "Developers"])

        ad_strategy = {
            "target": target_audience,
            "bid": bid_price,
            "format": "Native"
        }

        self.log(f"Placed bid ${bid_price} for audience '{target_audience}'")
        self.memory.data["ad_campaigns"].append(ad_strategy)
        self.publish("ads_placed", ad_strategy)
        self.memory.log_experience(self.name, "place_bid", "success", 0.8)

    def act(self):
        # Optimize existing campaigns
        if random.random() < 0.4:
            self.log("Optimizing programmatic ad bids...")
            # Simulate optimization
            self.memory.update_metric("ctr", round(random.uniform(1.5, 3.5), 2))

class MonetizationAgent(BaseAgent):
    def setup(self):
        self.bus.subscribe("ads_placed", self.track_revenue)

    def track_revenue(self, topic, message):
        bid = message["content"].get("bid")
        # Simulate revenue generation
        revenue = bid * random.uniform(1.1, 1.5)
        self.log(f"Projected revenue from campaign: ${revenue:.2f}")
        current_revenue = self.memory.data.get("performance_metrics", {}).get("total_revenue", 0)
        self.memory.update_metric("total_revenue", current_revenue + revenue)

    def act(self):
        pass
