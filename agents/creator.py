from .base import Agent
import random

class CreatorAgent(Agent):
    def __init__(self):
        super().__init__("CreatorAgent")

    def perform_task(self):
        templates = [
            "Top 5 {} Trends for 2025",
            "Why {} is making a comeback",
            "The ultimate guide to {}"
        ]
        # In a real system, this would use keywords from AnalystAgent
        topic = "Sustainable Fashion"
        title = random.choice(templates).format(topic)
        self.results['draft_title'] = title
        self.results['draft_content'] = f"Here is a draft for {title}..."
