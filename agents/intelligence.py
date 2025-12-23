from .base import Agent

class IntelligenceAgent(Agent):
    def __init__(self):
        super().__init__("IntelligenceAgent")

    def perform_task(self):
        # In a real scenario, this would digest data from Analyst and Researcher
        # For now, it provides heuristic advice.
        self.results['strategy'] = "Focus on content consistency."
        self.results['trend_alert'] = "No major market shifts detected."
