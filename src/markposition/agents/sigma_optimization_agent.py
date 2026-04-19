import statistics
from .base_agent import BaseAgent, Blackboard

class SigmaOptimizationAgent(BaseAgent):
    """
    Performs DMAIC variance analysis (Six Sigma) on system-wide impact scores
    and proposes optimizations to reduce logic drift.
    """
    def __init__(self):
        super().__init__("SigmaOptimizationAgent",
                         dependencies=["sigma_performance_report", "optimization_proposal"],
                         provides=["sigma_optimization_metrics"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Executing Sigma Variance Analysis (DMAIC)...")

        # 1. Measure (Get history from memory)
        history = self.get_agent_memory("impact_history", [])
        current_report = blackboard.get("sigma_performance_report", {})
        current_impact = current_report.get("average_impact_score", 0.5)

        history.append(current_impact)
        if len(history) > 30: history.pop(0) # Keep last 30 cycles
        self.update_agent_memory("impact_history", history)

        # 2. Analyze Variance
        variance = statistics.variance(history) if len(history) > 1 else 0
        sigma_level = 6 if variance < 0.001 else 3 if variance < 0.05 else 1

        self.logger.info(f"DMAIC Analysis: Variance={variance:.4f}, Sigma Level={sigma_level}")

        # 3. Improve (Propose tightening if variance is high)
        if variance > 0.1:
            await blackboard.propose_improvement(self.name, {
                "evolution_rate": max(0.01, self.config.get("evolution_rate", 0.05) - 0.005)
            })

        return {
            "sigma_optimization_metrics": {
                "sigma_level": sigma_level,
                "variance": variance,
                "cycle_history_count": len(history)
            }
        }
