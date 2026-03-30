from .base_agent import BaseAgent, Blackboard

class BidAgent(BaseAgent):
    def __init__(self):
        super().__init__("BidAgent", dependencies=["targeting_profile"], provides=["bid_strategy"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Calculating Bid Strategy...")

        targeting = blackboard.get("targeting_profile", {})
        persona = targeting.get("primary_persona", "")

        base_cpm = 3.50
        if "AdTech" in persona:
            base_cpm += 1.00
        if "Google" in persona:
            base_cpm *= 1.1

        # Evolution: Learn from previous cycle
        adj_factor = self.get_agent_memory("adjustment_factor", 1.0)
        final_cpm = round(base_cpm * adj_factor, 2)

        # Self-optimization
        new_adj = adj_factor * 1.01
        self.update_agent_memory("adjustment_factor", new_adj)

        return {
            "bid_strategy": {
                "strategy": "Automated Value-Based",
                "recommended_cpm": final_cpm,
                "adjustment_factor": round(adj_factor, 3)
            }
        }
