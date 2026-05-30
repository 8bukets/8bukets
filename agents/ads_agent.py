from agents.base_agent import BaseAgent
import random

class AdsAgent(BaseAgent):
    def __init__(self):
        super().__init__("Ads")

    async def run(self, context: dict):
        self.log("Running ads analysis and targeting...")

        analysis = context.get("analysis", {})
        top_cats = analysis.get("top_categories", [])

        if not top_cats:
            self.log("No category data for targeting.")
            return

        # Simple bidding strategy simulation
        # Determine bid based on category popularity
        ad_strategies = []
        for cat, count in top_cats[:3]:
            # Mock CPC (Cost Per Click) calculation
            base_bid = 0.50
            popularity_multiplier = min(count / 10, 2.0)
            suggested_bid = round(base_bid * popularity_multiplier, 2)

            strategy = {
                "target_category": cat,
                "suggested_bid": suggested_bid,
                "ad_copy": self.generate_ad_copy(cat),
                "potential_reach": count * 100 # Mock reach metric
            }
            ad_strategies.append(strategy)

        context["ad_strategies"] = ad_strategies
        self.log(f"Generated {len(ad_strategies)} ad strategies.")

    def generate_ad_copy(self, category):
        templates = [
            f"Discover the best {category} secrets now!",
            f"Unlock your potential in {category} today.",
            f"Top rated {category} resources just for you."
        ]
        return random.choice(templates)
