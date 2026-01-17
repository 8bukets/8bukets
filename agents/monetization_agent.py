from .base_agent import BaseAgent

class MonetizationAgent(BaseAgent):
    def __init__(self):
        super().__init__("Monetization Agent")
        self.high_value_keywords = {
            "hosting": 50,
            "software": 40,
            "finance": 60,
            "crypto": 50,
            "insurance": 80,
            "marketing": 30,
            "cloud": 45,
            "vpn": 55
        }

    def run(self, data: list) -> dict:
        """
        Scans titles and categories for high-value keywords to identify monetization opportunities.
        """
        if not data:
            return {}

        opportunities = []
        potential_score = 0

        for post in data:
            text = (post.get('title') or "") + " " + " ".join(post.get('categories') or [])
            text_lower = text.lower()

            matched = []
            score = 0
            for kw, val in self.high_value_keywords.items():
                if kw in text_lower:
                    matched.append(kw)
                    score += val

            if matched:
                opportunities.append({
                    "title": post.get('title'),
                    "keywords": matched,
                    "score": score,
                    "link": post.get('external_link')
                })
                potential_score += score

        # Sort by score desc
        opportunities.sort(key=lambda x: x['score'], reverse=True)

        return {
            "total_value_score": potential_score,
            "top_opportunities": opportunities[:5]
        }
