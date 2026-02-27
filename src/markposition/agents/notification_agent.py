from .base_agent import BaseAgent
import os
import aiohttp

class NotificationAgent(BaseAgent):
    execution_stage = 9 # Run after oversight
    def __init__(self):
        super().__init__("NotificationAgent")

    async def run(self, data: list, context: dict) -> dict:
        self.logger.info("Running Notification Agent...")

        report_status = context.get("autonomous_status", "UNKNOWN")
        health = context.get("ecosystem_health", "UNKNOWN")
        evolution = context.get("evolution_notes", [])

        message = {
            "text": f"🚀 *Autonomous Cycle Complete*\n"
                    f"*Status:* {report_status}\n"
                    f"*Health:* {health}\n"
                    f"*Evolution:* {len(evolution)} changes made."
        }

        # Actual Webhook delivery
        webhook_url = os.getenv("NOTIFY_WEBHOOK_URL")
        if webhook_url and self.session:
            try:
                self.logger.info(f"Sending daily report summary to webhook: {webhook_url}")
                async with self.session.post(webhook_url, json=message) as resp:
                    if resp.status < 300:
                        self.logger.info("Notification delivered successfully.")
                    else:
                        self.logger.warning(f"Failed to deliver notification (Status: {resp.status})")
            except Exception as e:
                self.logger.error(f"Error sending notification: {e}")
        else:
            self.logger.info("No webhook or session available. Skipping external notification.")

        return {"notification_sent": True if webhook_url else False}
