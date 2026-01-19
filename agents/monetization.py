from .base_agent import BaseAgent

class MonetizationAgent(BaseAgent):
    def __init__(self):
        super().__init__("Monetization")

    def sanitize_input(self, text):
        """Sanitize text to prevent Markdown injection."""
        if not text:
            return "Untitled"
        # Escape markdown special characters to prevent injection in reports
        return text.replace('[', '\\[').replace(']', '\\]').replace('(', '\\(').replace(')', '\\)')

    def perform_task(self, data):
        # Data is raw posts
        if not data:
            return {"revenue_opportunities": []}

        opportunities = []
        for post in data:
            content = post.get('content', '').lower()
            if 'adsense' not in content and 'affiliate' not in content:
                safe_title = self.sanitize_input(post.get('title'))
                opportunities.append(f"Post '{safe_title}' has no obvious monetization terms.")

        # Simple heuristic
        if len(opportunities) > 5:
            summary = "Many posts lack monetization keywords."
        else:
            summary = "Monetization seems active."

        return {"summary": summary, "details": opportunities[:5]}
