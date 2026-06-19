from agents.base_agent import BaseAgent, Blackboard
import random

class CreativityAgent(BaseAgent):
    def __init__(self):
        super().__init__("CreativityAgent",
                         dependencies=["long_term_visions"],
                         provides=["creative_ideas"])

    async def run(self, data: list, blackboard: Blackboard):
        self.log("Brainstorming creative content ideas...")
        analysis = blackboard.get("analysis", {})
        top_cats = [c[0] for c in analysis.get("top_categories", [])]

        ideas = []
        if top_cats:
            # Idea 1: Top list
            ideas.append(f"Top 10 {top_cats[0]} Trends You Missed")

            # Idea 2: Combination
            if len(top_cats) >= 2:
                ideas.append(f"How {top_cats[0]} Intersects with {top_cats[1]}")

            # Idea 3: Deep Dive
            ideas.append(f"The Ultimate Guide to {random.choice(top_cats)}")

        # Incorporate long-term visions from DreamBuilderAgent
        visions = blackboard.get("long_term_visions", [])
        for vision in visions:
            ideas.append(f"Content Strategy for: {vision['title']}")

        self.log(f"Generated {len(ideas)} ideas.")
        return {"creative_ideas": ideas}
