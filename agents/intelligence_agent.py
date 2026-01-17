from .base_agent import BaseAgent, AgentContext
from typing import List
from .knowledge import KnowledgeBase

class IntelligenceAgent(BaseAgent):
    def __init__(self, agents: List[BaseAgent]):
        super().__init__("IntelligenceAgent 🧠")
        self.agents = agents
        self.knowledge = KnowledgeBase()

    def run(self, context: AgentContext):
        current_iq = self.knowledge.get_iq()
        context.set("system_iq", current_iq)
        context.set("knowledge_base", self.knowledge)

        self.log(context, f"Orchestrating autonomous cycle... (Current IQ: {current_iq})")
        self.log(context, "Integrating development environment and coordinating agents...")

        # Decide the order of execution dynamically
        for agent in self.agents:
            if agent is not self:
                try:
                    agent.run(context)
                except Exception as e:
                    self.log(context, f"❌ Error running {agent.name}: {e}")

        # Calculate Cycle Performance (Daily Score)
        score = 0

        # 1. Health Score
        if context.get("system_health") == "HEALTHY":
            score += 1

        # 2. Research Score
        total_posts = context.get("total_posts", 0)
        score += min(total_posts * 0.1, 5) # Cap at 5 points for volume

        # 3. Monetization Score
        value = context.get("estimated_value", 0)
        score += min(value * 0.01, 10) # Cap at 10 points for value

        self.log(context, f"Cycle Performance Score: {score:.2f}")

        # Learn and Evolve
        iq_gain = self.knowledge.learn(score)
        new_iq = self.knowledge.get_iq()

        self.log(context, f"🧠 Self-Learning Complete. IQ increased by +{iq_gain:.4f}")
        self.log(context, f"📈 New System IQ: {new_iq}")

        # Google Antigravity "Colab"
        self.log(context, "🚀 collaborating with Google Antigravity concepts: Gravity defied, creativity maximized.")
        self._create_antigravity_artifact(context)

    def _create_antigravity_artifact(self, context: AgentContext):
        """Creates a fun artifact as part of the Google Antigravity collaboration."""
        content = """
<!DOCTYPE html>
<html>
<head>
<title>Google Antigravity Collaboration</title>
<style>
body { font-family: sans-serif; text-align: center; margin-top: 50px; }
h1 { color: #4285F4; transform: rotate(180deg); }
p { font-size: 1.2em; color: #555; }
</style>
</head>
<body>
<h1>Google Antigravity</h1>
<p>Collaborating with autonomous agents to defy expectations.</p>
<p>IQ Level: """ + str(context.get("system_iq", "Unknown")) + """</p>
<script>
console.log("Antigravity loaded.");
</script>
</body>
</html>
"""
        with open("antigravity.html", "w") as f:
            f.write(content)
        self.log(context, "🌌 Generated antigravity.html artifact.")
