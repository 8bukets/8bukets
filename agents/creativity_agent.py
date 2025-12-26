import random
from .base_agent import BaseAgent, AgentContext

class CreativityAgent(BaseAgent):
    def __init__(self):
        super().__init__("CreativityAgent 🎨")

    def run(self, context: AgentContext):
        trends = context.get("top_trends", [])
        if not trends:
            trends = ["General Tech", "AI", "Future"]

        # Self-Improvement: Use IQ to determine creativity depth
        knowledge = context.get("knowledge_base")
        creativity_level = 1.0
        if knowledge:
            creativity_level = knowledge.get_strategy_param("creativity_level", 1.0)

        self.log(context, f"Brainstorming ideas based on trends (Creativity Level: {creativity_level:.2f})...")

        ideas = []
        for trend in trends:
            if creativity_level > 3.0:
                idea = f"Deep Dive: The synergistic evolution of {trend} in high-frequency autonomous trading systems."
            else:
                idea = f"Article about the future of {trend} and its impact on autonomous systems."
            ideas.append(idea)

        # Add a "Google Antigravity" inspired idea
        ideas.append("Concept: A zero-gravity UI interface for data visualization.")

        if creativity_level > 5.0:
             ideas.append("Abstract: Quantum-entangled neural networks for instantaneous ad bidding.")

        context.set("creative_ideas", ideas)
        self.log(context, f"Generated {len(ideas)} ideas.")
