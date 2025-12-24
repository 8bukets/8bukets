from agents.base_agent import BaseAgent
import random

class AntigravityAgent(BaseAgent):
    def __init__(self):
        super().__init__("Antigravity")

    async def run(self, context: dict):
        self.log("Applying Google Antigravity logic...")

        # Google Antigravity is about breaking expectations.
        # This agent will look for "outliers" or unexpected connections.

        data = context.get("raw_data", [])
        if not data:
            return

        # Find the longest title vs shortest title
        sorted_by_len = sorted(data, key=lambda x: len(x.get("title", "")))
        shortest = sorted_by_len[0].get("title", "N/A")
        longest = sorted_by_len[-1].get("title", "N/A")

        # "Defy Gravity" - Random shuffle recommendation
        # Suggest a random post that might be overlooked (bottom of the list)
        hidden_gem = random.choice(data)

        context["antigravity"] = {
            "shortest_title": shortest,
            "longest_title": longest,
            "hidden_gem": hidden_gem.get("title", "Unknown"),
            "fun_fact": "Gravity is just a theory here."
        }
        self.log("Antigravity checks complete.")
