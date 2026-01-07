from .base_agent import BaseAgent
import asyncio
import random

class CreativityAgent(BaseAgent):
    def __init__(self, shared_state):
        super().__init__("CreativityAgent", shared_state)

    async def perform_task(self):
        # Adds "flare"
        ideas = ["Optimize headings", "Add more emojis", "Use AI for summary"]
        idea = random.choice(ideas)
        # self.log(f"🎨 Creative spark: {idea}")
        await asyncio.sleep(30)
