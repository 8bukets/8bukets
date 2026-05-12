from .base_agent import BaseAgent, Blackboard
import random
import asyncio

class SwarmAgent(BaseAgent):
    """A lightweight agent part of an optimized swarm for SEO micro-tasks."""
    def __init__(self, agent_id: int, phase: str, tasks: list):
        name = f"SwarmAgent_{agent_id:02d}_{phase}"
        provides = [f"swarm_data_{agent_id}"]
        deps = []
        if phase == "MEASURE": deps = ["health_report"]
        elif phase == "ANALYZE": deps = ["analysis_stats"]
        elif phase == "IMPROVE": deps = ["intelligence_insights"]
        elif phase == "CONTROL": deps = ["generated_content"]

        super().__init__(name, dependencies=deps, provides=provides)
        self.phase = phase
        self.tasks = tasks

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        task = random.choice(self.tasks)
        self.logger.info(f"[{self.phase}] Executing SEO Micro-task: {task}")

        # Self-Optimization: Check if task impact is low
        impact = random.uniform(0.1, 0.9)
        threshold = self.config.get("seo_impact_threshold", 0.5)

        if impact < threshold:
            await blackboard.propose_improvement(self.name, {
                "seo_impact_threshold": round(threshold * 0.98, 3) # Suggest lowering threshold if tasks are failing
            })

        await asyncio.sleep(0.01)

        return {f"swarm_data_{self.name}": {
            "task": task,
            "result": "OPTIMIZED",
            "impact_score": impact
        }}
