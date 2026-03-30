from .base_agent import BaseAgent, Blackboard

class HealthCheckAgent(BaseAgent):
    def __init__(self):
        super().__init__("HealthCheckAgent", provides=["health_report"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Running Health Check...")

        report = {
            "status": "PASS",
            "checks": []
        }

        if not data:
            report["status"] = "FAIL"
            report["checks"].append("Data is empty.")
        else:
            report["checks"].append(f"Data contains {len(data)} records.")

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
