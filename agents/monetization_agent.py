from agents.base_agent import BaseAgent

class MonetizationAgent(BaseAgent):
    def __init__(self):
        super().__init__("Monetization")

    async def run(self, context: dict):
        self.log("Scanning for monetization opportunities...")
        data = context.get("raw_data", [])

        commercial_keywords = ["buy", "shop", "store", "sale", "price", "deal", "discount", "amazon", "ebay", "course", "premium"]

        opportunities = []
        for post in data:
            title = (post.get("title") or "").lower()
            link = (post.get("external_link") or "").lower()

            # Simple keyword matching
            matched_keywords = [k for k in commercial_keywords if k in title or k in link]

            if matched_keywords:
                opportunities.append({
                    "title": post.get("title"),
                    "link": post.get("external_link"),
                    "keywords": matched_keywords
                })

        context["monetization_ops"] = opportunities
        self.log(f"Found {len(opportunities)} potential monetization opportunities.")
