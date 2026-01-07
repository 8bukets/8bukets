from .base_agent import BaseAgent
import asyncio
import os

class HealthAgent(BaseAgent):
    def __init__(self, shared_state):
        super().__init__("HealthAgent", shared_state)

    async def perform_task(self):
        self.log("❤️ Checking system health...")
        # Check if critical files exist
        critical_files = ["scraper.py", "analytics.py"]
        status = "OK"
        for f in critical_files:
            if not os.path.exists(f):
                status = f"MISSING {f}"
                break

        if status != "OK":
            if 'IntelligenceAgent' in self.shared_state['agents']:
                self.send_message(self.shared_state['agents']['IntelligenceAgent'], {
                    'type': 'health_alert',
                    'status': status
                })

        await asyncio.sleep(60)
