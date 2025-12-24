import random
from .base_agent import BaseAgent

class CreativityAgent(BaseAgent):
    def __init__(self):
        super().__init__("Creativity Agent")

    def run(self, data: dict) -> dict:
        """
        Generates new ideas by mixing topics.
        Expects `data` to contain 'research' output.
        """
        trends = data.get('research', {}).get('trending_keywords', [])
        if len(trends) < 2:
            return {"ideas": ["Not enough data for creative synthesis."]}

        ideas = []
        for _ in range(5):
            t1, t2 = random.sample(trends, 2)
            ideas.append(f"The Intersection of {t1.title()} and {t2.title()}: A New Perspective")
            ideas.append(f"Why {t1.title()} is the Future of {t2.title()}")

        return {
            "creative_hooks": ideas[:5]
        }
