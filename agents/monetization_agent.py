import random
from .base_agent import BaseAgent, AgentContext

class MonetizationAgent(BaseAgent):
    def __init__(self):
        super().__init__("MonetizationAgent 💰")

    def run(self, context: AgentContext):
        content_file = context.get("generated_content_file")
        if not content_file:
            self.log(context, "No content to monetize.")
            return

        self.log(context, f"Analyzing {content_file} for revenue potential...")

        # Simulate value analysis
        value_score = random.randint(100, 500)
        context.set("estimated_value", value_score)

        strategies = ["Affiliate Links", "Sponsored Sections", "Premium Access"]
        strategy = random.choice(strategies)
        context.set("monetization_strategy", strategy)

        self.log(context, f"Estimated Value: ${value_score}. Strategy: {strategy}")
