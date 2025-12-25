from .base import Agent
import random

class CreativeAgent(Agent):
    def __init__(self):
        super().__init__("CreativeAgent")

    def perform_task(self, context=None):
        # 1. Standard Content Brainstorming
        ideas = [
            "Interview a designer",
            "Behind the scenes video",
            "User generated content contest",
            "History of a brand",
            "Color theory in modern design"
        ]
        self.results['brainstorm'] = random.sample(ideas, 2)

        # 2. High Solution Interest Ideas (Coding/System Integration)
        # Uses context from CuriosityAgent if available
        curiosity_findings = context.get('curiosity_findings', []) if context else []
        exploration_query = context.get('exploration_query', "General Tech") if context else "General Tech"

        system_ideas = []

        # Generate idea based on exploration
        if curiosity_findings:
            system_ideas.append(f"Build a scraper to monitor '{exploration_query}' trends specifically.")
            system_ideas.append(f"Create an automated newsletter summarizing '{curiosity_findings[0]}'.")
        else:
            system_ideas.append(f"Integrate a new API related to {exploration_query}.")

        # "Google Antigravity" / Moonshot ideas
        moonshots = [
            "Implement a Reinforcement Learning model to optimize bid prices.",
            "Create a visual dashboard using Streamlit for real-time monitoring.",
            "Develop a browser extension to auto-save wishlist items.",
            "Use GANs to generate unique design images for blog headers."
        ]
        system_ideas.append(random.choice(moonshots))

        self.results['system_improvement_ideas'] = system_ideas
