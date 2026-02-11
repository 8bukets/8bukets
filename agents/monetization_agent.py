from .base_agent import BaseAgent

class MonetizationAgent(BaseAgent):
    def __init__(self):
        super().__init__("Monetization Agent")

    def run(self, data):
        self.log("Analyzing monetization opportunities...")

        ad_keywords = ['ads', 'advertising', 'affiliate', 'revenue', 'monetize', 'shop', 'store']
        opportunities = 0

        for p in data:
            # Check title or categories for monetization keywords
            text = (p.get('title', '') + ' ' + ' '.join(p.get('categories', []))).lower()
            if any(k in text for k in ad_keywords):
                opportunities += 1

        report = "### Monetization Potential\n"
        report += f"- **Identified Opportunities:** {opportunities} links related to ads/revenue.\n"
        report += "- **Recommendation:** Review these links for potential affiliate partnerships or ad network research.\n"

        self.log("Monetization analysis complete.")
        return report
