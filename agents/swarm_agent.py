from .base_agent import BaseAgent, Blackboard
import random
import asyncio

class SwarmAgent(BaseAgent):
    """A lightweight agent part of a 50-agent swarm for SEO micro-tasks."""
    def __init__(self, agent_id: int, phase: str, tasks: list):
        name = f"SwarmAgent_{agent_id:02d}_{phase}"
        # All swarm agents in a phase provide data for that phase
        # and might depend on data from previous phases
        provides = [f"swarm_data_{agent_id}"]
        # Simple dependency: swarm depends on the phase's primary data
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

        # Simulate work
        await asyncio.sleep(0.01)

        return {f"swarm_data_{self.name}": {
            "task": task,
            "result": "OPTIMIZED",
            "impact_score": random.uniform(0.1, 0.9)
        }}
