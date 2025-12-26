from .base_agent import BaseAgent
import asyncio
import random

class AdAgent(BaseAgent):
    def __init__(self, shared_state):
        super().__init__("AdAgent", shared_state)

    async def perform_task(self):
        # Get learning params
        params = self.shared_state.get('learning_params', {'bid_aggressiveness': 0.5})
        aggressiveness = params.get('bid_aggressiveness', 0.5)

        # Programmatic Advertising / Bidding Logic Simulation
        # self.log("📢 Evaluating ad inventory...")

        # Adjust bid based on learning parameter
        base_bid = random.uniform(0.5, 2.0)
        bid_price = base_bid * (1 + aggressiveness)

        # self.log(f"💲 Placed programmatic bid: ${bid_price:.2f} (Aggressiveness: {aggressiveness:.2f})")

        # Simulate Result (Win/Loss)
        win = random.random() < 0.5 # 50% chance initially

        if 'IntelligenceAgent' in self.shared_state['agents']:
            self.send_message(self.shared_state['agents']['IntelligenceAgent'], {
                'type': 'action_feedback',
                'agent': 'AdAgent',
                'action': 'bid',
                'success': win,
                'details': {'bid': bid_price, 'win': win}
            })

        await asyncio.sleep(20)
