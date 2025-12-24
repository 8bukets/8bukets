from .base_agent import BaseAgent
from typing import List, Dict, Any
from collections import Counter

class AdsAgent(BaseAgent):
    def __init__(self):
        super().__init__("Ads & Targeting Agent")

    async def process(self, data: List[Dict], shared_context: Dict[str, Any], knowledge_base: Dict[str, Any]) -> Dict[str, Any]:

        # Analyze Categories for Targeting segments
        categories = []
        for p in data:
            if p.get('categories'):
                categories.extend(p['categories'])

        segments = Counter(categories).most_common(3)
        targeting_segments = [s[0] for s in segments]

        # Share targeting info
        shared_context['targeting_segments'] = targeting_segments

        # Identify Ad Networks (simple heuristic)
        networks = []
        ad_keywords = ['google', 'amazon', 'doubleclick', 'facebook', 'criteo']

        link_domains = [p.get('domain') for p in data if p.get('domain')]
        for domain in link_domains:
            for kw in ad_keywords:
                if kw in domain.lower():
                    networks.append(kw.capitalize())

        network_counts = Counter(networks).most_common(3)

        results = {}
        results['Identified Ad Networks'] = ", ".join([f"{n} ({c})" for n, c in network_counts])
        results['Inferred Targeting Segments'] = ", ".join(targeting_segments)

        return results
