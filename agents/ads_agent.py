from agents.base_agent import BaseAgent
import random

class AdsAgent(BaseAgent):
    def __init__(self):
        super().__init__("Ads")

    async def run(self, context: dict):
        self.log("Running ads analysis and targeting...")

        analysis = context.get("analysis", {})
        monetization = context.get("monetization_ops", [])
        top_cats = analysis.get("top_categories", [])

        ad_strategies = []

        # 1. Category-based Targeting (Broad)
        if top_cats:
            for cat, count in top_cats[:2]:
                base_bid = 0.50
                popularity_multiplier = min(count / 10, 2.0)
                suggested_bid = round(base_bid * popularity_multiplier, 2)

                strategy = {
                    "type": "Category",
                    "target": cat,
                    "suggested_bid": suggested_bid,
                    "ad_copy": self.generate_ad_copy(cat),
                    "potential_reach": count * 100
                }
                ad_strategies.append(strategy)

        # 2. Keyword-based Targeting (High Value from Monetization Agent)
        # Deep collaboration: Use found commercial keywords to target high-intent users
        if monetization:
            high_value_keywords = set()
            for op in monetization:
                high_value_keywords.update(op.get("keywords", []))

            # Select top 3 keywords
            for kw in list(high_value_keywords)[:3]:
                # Commercial keywords command higher bids
                suggested_bid = 1.50
                strategy = {
                    "type": "Keyword",
                    "target": kw,
                    "suggested_bid": suggested_bid,
                    "ad_copy": self.generate_keyword_copy(kw),
                    "potential_reach": "High Intent"
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

    def generate_keyword_copy(self, keyword):
        templates = [
            f"Looking for {keyword}? Best deals here.",
            f"Exclusive offers on {keyword}.",
            f"Don't miss out on {keyword} discounts."
        ]
        return random.choice(templates)
