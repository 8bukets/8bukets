from agents.base import BaseAgent
import logging

logger = logging.getLogger(__name__)

class MonetizationAgent(BaseAgent):
    def __init__(self):
        super().__init__("MonetizationAgent")

    def run(self, data):
        logger.info(f"[{self.name}] Analyzing for monetization opportunities...")
        commercial_keywords = ['sale', 'discount', 'offer', 'price', 'buy', 'shop', 'deal', 'promo', 'coupon']
        affiliate_domains = ['amazon', 'ebay', 'aliexpress', 'booking.com', 'skimresources']

        opportunities = []
        for p in data:
            title = p.get('title', '').lower()
            link = p.get('external_link', '') or ''

            # Check keywords
            if any(kw in title for kw in commercial_keywords):
                opportunities.append({
                    'type': 'keyword_match',
                    'post': p.get('title'),
                    'url': p.get('post_url')
                })
                continue # Don't double count

            # Check domains
            if any(dom in link for dom in affiliate_domains):
                opportunities.append({
                    'type': 'affiliate_domain',
                    'post': p.get('title'),
                    'url': p.get('post_url'),
                    'domain': link
                })

        return opportunities
