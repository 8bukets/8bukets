import os
import aiohttp
from datetime import datetime
from .base_agent import BaseAgent, Blackboard

class NotificationAgent(BaseAgent):
    """
    Asynchronously notifies stakeholders via Slack/Discord webhooks
    about the completion of autonomous cycles.
    """
    def __init__(self):
        super().__init__("NotificationAgent",
                         dependencies=["documentation_status", "system_evolution", "sigma_performance_report"],
                         provides=["notification_status"])
        self.webhook_url = os.environ.get("NOTIFICATION_WEBHOOK")

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        if not self.webhook_url:
            self.logger.warning("NOTIFICATION_WEBHOOK not set. Skipping notification.")
            return {"notification_status": "SKIPPED"}

        evolution = blackboard.get("system_evolution", {})
        sigma = blackboard.get("sigma_performance_report", {})
        version = evolution.get("parameter_shifts", {}).get("current_version", "1.0")

        message = (
            f"🚀 **Autonomous Cycle Complete: v{version}**\n"
            f"- **Sigma Status:** {sigma.get('average_impact_score', 0):.2f} Impact\n"
            f"- **Evolution:** {evolution.get('status', 'STABLE')}\n"
            f"- **Timestamp:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )

        try:
            async with aiohttp.ClientSession() as session:
                payload = {"text": message} if "slack.com" in self.webhook_url else {"content": message}
                async with session.post(self.webhook_url, json=payload) as response:
                    if response.status < 400:
                        self.logger.info("Notification sent successfully.")
                        return {"notification_status": "SENT"}
                    else:
                        self.logger.error(f"Failed to send notification: HTTP {response.status}")
                        return {"notification_status": f"FAILED_HTTP_{response.status}"}
        except Exception as e:
            self.logger.error(f"Error sending notification: {e}")
            return {"notification_status": f"ERROR_{str(e)}"}
