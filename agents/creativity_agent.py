import random
from .base_agent import BaseAgent, AgentContext

class CreativityAgent(BaseAgent):
    def __init__(self):
        super().__init__("CreativityAgent 🎨")

    def run(self, context: AgentContext):
        trends = context.get("top_trends", [])
        if not trends:
            trends = ["General Tech", "AI", "Future"]

        self.log(context, "Brainstorming ideas based on trends...")

        ideas = []
        for trend in trends:
            idea = f"Article about the future of {trend} and its impact on autonomous systems."
            ideas.append(idea)

        # Add a "Google Antigravity" inspired idea
        ideas.append("Concept: A zero-gravity UI interface for data visualization.")

        context.set("creative_ideas", ideas)
        self.log(context, f"Generated {len(ideas)} ideas.")
