from .base import BaseAgent

class HealthAgent(BaseAgent):
    def act(self):
        # Check system memory and status
        facts_count = len(self.memory.data["facts"])
        experiences_count = len(self.memory.data["experiences"])
        self.log(f"System Health Check: OK. Memory Usage: {facts_count} facts, {experiences_count} experiences.")

        if experiences_count > 100:
            self.log("Suggestion: Prune old memories.")

class IntelligenceAgent(BaseAgent):
    def act(self):
        # Coordinate high-level goals
        # In a real system, this would be more complex.
        # Here, it simply triggers a research cycle if idle.
        import random
        if random.random() < 0.1:
            self.log("Triggering new research cycle.")
            self.publish("request_research", {"query": "Next Gen AI Agents"})

    def learn(self):
        # Override to perform system-wide learning
        super().learn()
        self.log("Analyzing overall system efficiency...")
