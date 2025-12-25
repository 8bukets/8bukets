from .base_agent import BaseAgent

class MonetizationAgent(BaseAgent):
    def __init__(self):
        super().__init__("Monetization Agent")

    def run(self):
        self.log("Identifying revenue opportunities...")

        affiliate_keywords = ["hosting", "vpn", "seo tool", "email marketing"]
        opportunities = []

        for p in self.data:
            title = p.get('title', '').lower()
            for kw in affiliate_keywords:
                if kw in title:
                    opportunities.append({
                        "keyword": kw,
                        "source": p.get('title'),
                        "action": "Add affiliate link"
                    })

        self.results = {
            "potential_revenue_streams": len(opportunities),
            "top_opportunities": opportunities[:5]
        }
        self.log("Monetization check complete.")
