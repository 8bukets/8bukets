from .base_agent import BaseAgent, AgentContext
import random

class AdAgent(BaseAgent):
    def __init__(self):
        super().__init__("AdAgent 📢")

    def run(self, context: AgentContext):
        trends = context.get("top_trends", ["General"])

        self.log(context, "Initiating Programmatic Ad Simulation...")

        # Simulate Bidding
        bids = []
        for trend in trends:
            bid_amount = round(random.uniform(0.50, 5.00), 2)
            bids.append({"keyword": trend, "bid": bid_amount})

        best_bid = max(bids, key=lambda x: x['bid'])

        context.set("ad_campaigns", bids)
        self.log(context, f"Placed bids. Winning bid: {best_bid['keyword']} at ${best_bid['bid']}")

        # Simulate targeting optimization
        self.log(context, "Optimizing targeting parameters based on user engagement signals...")
