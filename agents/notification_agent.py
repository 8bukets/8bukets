from .base_agent import BaseAgent
import os

class NotificationAgent(BaseAgent):
    execution_stage = 7 # Last stage
    def __init__(self):
        super().__init__("NotificationAgent")

    async def run(self, data: list, context: dict) -> dict:
        self.logger.info("Running Notification Agent...")

        report_status = context.get("autonomous_status", "UNKNOWN")

        # Simulate sending notifications
        webhook_url = os.getenv("NOTIFY_WEBHOOK_URL")
        if webhook_url:
            self.logger.info(f"Sending daily report summary to webhook: {webhook_url}")
            # Simulation: await self.session.post(webhook_url, json={"status": report_status})
        else:
            self.logger.info("No webhook configured. Skipping external notification.")

        return {"notification_sent": True}
