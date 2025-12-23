from .base_agent import BaseAgent
import requests

class HealthCheckAgent(BaseAgent):
    def __init__(self):
        super().__init__("HealthCheck")

    def perform_task(self, data):
        url = "https://informaticmagazine.data.blog"
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return {"status": "healthy", "code": 200}
            else:
                return {"status": "unhealthy", "code": response.status_code}
        except Exception as e:
            return {"status": "down", "error": str(e)}
