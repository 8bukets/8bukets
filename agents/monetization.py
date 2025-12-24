from .base import BaseAgent
from typing import Any, Dict

class MonetizationAgent(BaseAgent):
    def __init__(self):
        super().__init__("MonetizationAgent")

    async def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        data = context.get("scraped_data", [])
        if not data:
            return {"monetization": {}}

        self.log("Identifying monetization opportunities...")

        affiliate_keywords = ['amazon', 'referral', 'coupon', 'deal', 'sale', 'discount', 'shop', 'buy', 'price']
        ad_keywords = ['ads', 'advertising', 'sponsored', 'promotion']

        opportunities = []

        for p in data:
            title = p.get('title') or ''
            link = p.get('external_link') or ''
            text = (title + ' ' + link).lower()

            # Check for affiliate potential
            is_affiliate = any(k in text for k in affiliate_keywords)
            # Check for ad potential
            is_ad = any(k in text for k in ad_keywords)

            if is_affiliate or is_ad:
                opportunities.append({
                    "title": p.get('title'),
                    "link": p.get('external_link'),
                    "type": "Affiliate" if is_affiliate else "Ad Network"
                })

        # Summarize
        return {
            "monetization": {
                "opportunity_count": len(opportunities),
                "top_opportunities": opportunities[:10] # Top 10
            }
        }
