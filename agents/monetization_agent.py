from .base_agent import BaseAgent
from typing import List, Dict, Any
import re

class MonetizationAgent(BaseAgent):
    def __init__(self):
        super().__init__("Monetization Agent")

    async def process(self, data: List[Dict], shared_context: Dict[str, Any], knowledge_base: Dict[str, Any]) -> Dict[str, Any]:
        affiliate_patterns = ['amazon', 'clickbank', 'shareasale', 'rakuten', 'cj.com', 'partner', 'affiliate']

        found_opportunities = []
        for p in data:
            link = p.get('external_link', '')
            if not link:
                continue

            for pat in affiliate_patterns:
                if pat in link.lower():
                    found_opportunities.append(link)
                    break

        results = {}
        results['Potential Affiliate Links Identified'] = len(found_opportunities)
        if found_opportunities:
            results['Sample Opportunity'] = found_opportunities[0]
        else:
            results['Sample Opportunity'] = "None detected"

        return results
