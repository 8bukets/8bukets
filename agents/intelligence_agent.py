from .base_agent import BaseAgent, AgentContext
from typing import List

class IntelligenceAgent(BaseAgent):
    def __init__(self, agents: List[BaseAgent]):
        super().__init__("IntelligenceAgent 🧠")
        self.agents = agents

    def run(self, context: AgentContext):
        self.log(context, "Orchestrating autonomous cycle...")
        self.log(context, "Integrating development environment and coordinating agents...")

        # Decide the order of execution dynamically (simple version: sequential)
        # In a more advanced version, this agent would look at context and decide who needs to run.

        for agent in self.agents:
            if agent is not self: # Don't run self inside self loop
                try:
                    agent.run(context)
                except Exception as e:
                    self.log(context, f"❌ Error running {agent.name}: {e}")

        self.log(context, "Cycle complete. Analyzing performance...")
        health = context.get("system_health", "UNKNOWN")
        self.log(context, f"System Status: {health}")

        # Google Antigravity "Colab"
        self.log(context, "🚀 collaborating with Google Antigravity concepts: Gravity defied, creativity maximized.")
