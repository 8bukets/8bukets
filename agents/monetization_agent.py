from .base_agent import BaseAgent, Blackboard

class MonetizationAgent(BaseAgent):
    def __init__(self):
        super().__init__("MonetizationAgent", dependencies=["analysis_stats", "bid_strategy"], provides=["monetization_plan"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Running Monetization Analysis...")

        stats = blackboard.get("analysis_stats", {})
        bid = blackboard.get("bid_strategy", {})

        plan = {
            "projected_revenue": stats.get("total_posts", 0) * 0.05,
            "cpm_target": bid.get("recommended_cpm", 0.0),
            "channels": ["Direct", "Programmatic"]
        }

        return {"monetization_plan": plan}
