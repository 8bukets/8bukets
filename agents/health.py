import aiohttp
from .base import BaseAgent
from typing import Any, Dict

class HealthCheckAgent(BaseAgent):
    def __init__(self, target_url: str):
        super().__init__("HealthCheckAgent")
        self.target_url = target_url

    async def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        self.log(f"Checking health of {self.target_url}...")
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.target_url, timeout=10) as response:
                    status = response.status
                    is_healthy = 200 <= status < 400
                    self.log(f"Status: {status}, Healthy: {is_healthy}")
                    return {
                        "health_status": {
                            "url": self.target_url,
                            "status_code": status,
                            "is_healthy": is_healthy
                        }
                    }
        except Exception as e:
            self.log(f"Health check failed: {e}")
            return {
                "health_status": {
                    "url": self.target_url,
                    "error": str(e),
                    "is_healthy": False
                }
            }
