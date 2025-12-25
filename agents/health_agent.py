from .base_agent import BaseAgent
import requests

class HealthAgent(BaseAgent):
    def __init__(self):
        super().__init__("HealthAgent")

    def run(self, context):
        url = context.get('target_url', 'https://malubeach.wordpress.com')
        self.log(f"Checking health of {url}...")

        status = "Unknown"
        try:
            response = requests.get(url, timeout=10)
            status = response.status_code
            is_healthy = response.status_code == 200
        except Exception as e:
            is_healthy = False
            self.log(f"Health check failed: {e}")

        result = {"status_code": status, "is_healthy": is_healthy}
        self.learn("health_status", result)
        return result
