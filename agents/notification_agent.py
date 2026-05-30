import os
import aiohttp
import json
from .base_agent import BaseAgent, Blackboard

class NotificationAgent(BaseAgent):
    """Sends autonomous system updates to Discord/Slack webhooks."""
    def __init__(self):
        super().__init__("NotificationAgent", 
                         dependencies=["system_evolution", "sync_status"], 
                         provides=["notification_status"])
        self.webhook_url = os.environ.get("NOTIFICATION_WEBHOOK_URL")

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        if not self.webhook_url:
            self.logger.info("No notification webhook URL configured. Skipping.")
            return {"notification_status": "SKIPPED"}

        evolution = blackboard.get("system_evolution", {})
        sync = blackboard.get("sync_status", "")
        version = evolution.get("parameter_shifts", {}).get("current_version", "1.x")

        message = {
            "content": f"🚀 **Autonomous System Cycle Complete** (v{version})\n"
                       f"📊 **Sync Status:** {sync}\n"
                       f"🔧 **Evolution:** {evolution.get('status', 'STABLE')}\n"
                       f"📈 **Parameters Adjusted:** {len(evolution.get('parameter_shifts', {}))}"
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(self.webhook_url, json=message) as response:
                    if response.status in [200, 204]:
                        self.logger.info("Notification sent successfully.")
                        return {"notification_status": "SENT"}
                    else:
                        self.logger.error(f"Failed to send notification: {response.status}")
                        return {"notification_status": f"FAILED_{response.status}"}
        except Exception as e:
            self.logger.error(f"Error during notification: {e}")
            return {"notification_status": f"ERROR: {str(e)}"}
