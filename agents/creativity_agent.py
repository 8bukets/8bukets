from .base_agent import BaseAgent
import random

class CreativityAgent(BaseAgent):
    def __init__(self):
        super().__init__("CreativityAgent")

    def run(self, context):
        keywords = context.get('top_keywords', [])
        self.log("Brainstorming creative content ideas...")

        ideas = []
        if keywords:
            for _ in range(3):
                kw = random.choice(keywords)
                ideas.append(f"The Future of {kw.capitalize()} in 2025")
                ideas.append(f"Top 10 {kw.capitalize()} Tips You Need to Know")
        else:
            ideas.append("Why Consistency is Key for Blogging")

        # Deduplicate
        ideas = list(set(ideas))[:5]
        self.learn("creative_ideas", ideas)
        return {"ideas": ideas}
