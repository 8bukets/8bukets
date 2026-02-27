from .base_agent import BaseAgent, Blackboard

class AutonomousIntelligenceAgent(BaseAgent):
    def __init__(self):
        super().__init__("AutonomousIntelligenceAgent", dependencies=["health_report", "generated_ads", "bid_strategy", "targeting_profile", "robots_txt"], provides=["autonomous_status", "ecosystem_health"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Overseeing Ecosystem...")

        checks = {
            "has_ads": blackboard.get("generated_ads") is not None,
            "has_bids": blackboard.get("bid_strategy") is not None,
            "has_persona": blackboard.get("targeting_profile") is not None,
            "has_robots": blackboard.get("robots_txt") is not None
        }

        status = "OPTIMAL"
        issues = []
        for k, v in checks.items():
            if not v:
                status = "DEGRADED"
                issues.append(f"Missing context: {k}")

        if status == "DEGRADED":
            self.logger.warning(f"System degraded: {issues}")
            self.update_agent_memory("system_health", "degraded")
        else:
            self.update_agent_memory("system_health", "healthy")

        return {
            "autonomous_status": status,
            "ecosystem_health": "Healthy" if status == "OPTIMAL" else "Needs Attention"
        }
