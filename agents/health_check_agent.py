from .base_agent import BaseAgent
from typing import Dict, List

class HealthCheckAgent(BaseAgent):
    def __init__(self):
        super().__init__("Health Check Agent")

    def process(self, data: List[Dict]) -> Dict:
        self.log("Verifying data integrity...")

        issues = []
        for item in data:
            if not item.get('title'):
                issues.append(f"Missing title for item: {item}")
            if not item.get('external_link'):
                issues.append(f"Missing link for item: {item}")

        status = "Healthy" if not issues else "Issues Found"
        return {
            "status": status,
            "issues": issues,
            "record_count": len(data)
        }
