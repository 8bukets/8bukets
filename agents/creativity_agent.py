from .base_agent import BaseAgent
from typing import List, Dict, Any
import random

class CreativityAgent(BaseAgent):
    def __init__(self):
        super().__init__("Creativity Agent")

    async def process(self, data: List[Dict]) -> Dict[str, Any]:
        titles = [p.get('title') for p in data if p.get('title')]
        if not titles:
            return {"Ad Copy": "No input data for creativity."}

        # Pick a random title to remix
        inspiration = random.choice(titles)

        ad_templates = [
            f"Discover why '{inspiration}' is trending now!",
            f"The secret behind '{inspiration}' revealed.",
            f"Boost your strategy with insights from '{inspiration}'.",
            f"Don't miss out on '{inspiration}' - read more!"
        ]

        results = {}
        results['Inspiration'] = inspiration
        results['Generated Ad Copy'] = random.choice(ad_templates)

        return results
