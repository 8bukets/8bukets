from .base import Agent
import random

class CreativeAgent(Agent):
    def __init__(self):
        super().__init__("CreativeAgent")

    def perform_task(self):
        ideas = [
            "Interview a designer",
            "Behind the scenes video",
            "User generated content contest",
            "History of a brand",
            "Color theory in modern design"
        ]
        self.results['brainstorm'] = random.sample(ideas, 2)
