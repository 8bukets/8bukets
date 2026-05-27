import random
from .base_agent import BaseAgent

class CreativityAgent(BaseAgent):
    def __init__(self):
        super().__init__("Creativity Agent")

    def run(self):
        self.log("Brainstorming...")

        adjectives = ["Revolutionary", "Data-Driven", "Seamless", "Integrated", "AI-Powered"]
        nouns = ["Platform", "Solution", "Insight", "Strategy", "Campaign"]

        # Simple creative generator
        idea = f"{random.choice(adjectives)} {random.choice(nouns)}"

        self.results = {
            "daily_concept": idea,
            "campaign_angle": f"Focus on how {idea} can transform the digital advertising landscape.",
            "target_audience": "Marketing Executives and AdTech Specialists"
        }
        self.log("Creative concept generated.")
