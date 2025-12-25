from .base_agent import BaseAgent
import asyncio
import random

class AdAgent(BaseAgent):
    def __init__(self, shared_state):
        super().__init__("AdAgent", shared_state)

    async def perform_task(self):
        # Programmatic Advertising / Bidding Logic Simulation
        # self.log("📢 Evaluating ad inventory...")
        bid_price = random.uniform(0.5, 2.0)
        # self.log(f"💲 Placed programmatic bid: ${bid_price:.2f}")
        await asyncio.sleep(20)
