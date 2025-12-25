from .base_agent import BaseAgent
import asyncio

class IntelligenceAgent(BaseAgent):
    def __init__(self, shared_state):
        super().__init__("IntelligenceAgent", shared_state)

    async def process_message(self, message):
        self.log(f"🧠 Received intelligence: {message}")
        if message.get('type') == 'research_complete':
            self.log("Deciding next steps: Trigger Analysis.")
            # Analysis is actually triggered by shared state flag, but we could also message them.

        if message.get('type') == 'health_alert':
            self.log(f"⚠️ HEALTH ALERT: {message['status']}")

    async def perform_task(self):
        # High level decision making
        await asyncio.sleep(5)
