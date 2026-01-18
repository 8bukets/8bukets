from .base import BaseAgent
import urllib.request

class HealthAgent(BaseAgent):
    def __init__(self):
        super().__init__("HealthMonitor")

    def run(self, context):
        try:
            status = urllib.request.urlopen("https://software-online-review.com/").getcode()
            health = "Good" if status == 200 else "Degraded"
        except:
            health = "Offline"

        context['system_health'] = health
        self.log_activity(f"System Health: {health}")
