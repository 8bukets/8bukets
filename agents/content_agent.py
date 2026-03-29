from .base_agent import BaseAgent
import random

class ContentAgent(BaseAgent):
    def __init__(self):
        super().__init__("Content Agent")

    def run(self, data):
        self.log("Drafting content...")

        # Pick a random interesting article to feature
        if not data:
            return "No data to generate content."

        featured = random.choice(data)
        title = featured.get('title', 'Unknown Title')
        link = featured.get('external_link', '#')

        report = "### Content Draft: Bi-Weekly Highlight\n"
        report += f"**Title:** Spotlight on {title}\n\n"
        report += f"**Draft Snippet:** In this bi-weekly digest, we are highlighting an interesting piece: '{title}'. "
        report += "This aligns with our ongoing analysis of digital trends. "
        report += f"Check it out here: {link}\n"

        self.log("Content drafted.")
        return report
