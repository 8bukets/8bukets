from .base_agent import BaseAgent
import os
import json

class HealthCheckAgent(BaseAgent):
    def __init__(self):
        super().__init__("HealthCheckAgent")

    def run(self, data: list, context: dict) -> dict:
        self.logger.info("Running Health Check...")

        report = {
            "status": "PASS",
            "checks": []
        }

        # Check 1: Data is not empty
        if not data:
            report["status"] = "FAIL"
            report["checks"].append("Data is empty.")
        else:
            report["checks"].append(f"Data contains {len(data)} records.")

        # Check 2: Basic schema validation (sample first 5)
        required_keys = ["title", "external_link", "post_url"]
        valid_count = 0
        for item in data[:5]:
            if all(k in item for k in required_keys):
                valid_count += 1

        if valid_count == min(len(data), 5):
            report["checks"].append("Schema validation passed for sample.")
        else:
            report["status"] = "WARN"
            report["checks"].append("Schema validation failed for some items.")

        return {"health_report": report}
