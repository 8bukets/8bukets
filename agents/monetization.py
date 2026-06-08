from .base_agent import BaseAgent
from .utils import sanitize_markdown

class MonetizationAgent(BaseAgent):
    def __init__(self):
        super().__init__("Monetization")

    def perform_task(self, data):
        # Data is raw posts
        if not data:
            return {"revenue_opportunities": []}

        opportunities = []
        for post in data:
            content = post.get('content', '').lower()
            if 'adsense' not in content and 'affiliate' not in content:
                safe_title = sanitize_markdown(post.get('title'))
                opportunities.append(f"Post '{safe_title}' has no obvious monetization terms.")

        # Simple heuristic
        if len(opportunities) > 5:
            summary = "Many posts lack monetization keywords."
        else:
            summary = "Monetization seems active."

        return {"summary": summary, "details": opportunities[:5]}
