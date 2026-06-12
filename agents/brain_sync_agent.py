import os
import json
from .base_agent import BaseAgent, Blackboard

class BrainSyncAgent(BaseAgent):
    """
    The Brain-Sync Bridge: Synchronizes Jules' (TS) cognitive memory with the Python Intelligence Swarm.
    Allows high-scale collaboration by making Jules' decisions actionable for Python agents.
    """
    def __init__(self):
        super().__init__("BrainSyncAgent",
                         dependencies=[],
                         provides=["jules_cognitive_state", "autonomous_tasks"])
        # In sync_repo, .jules_memory.json is at root
        self.memory_path = ".jules_memory.json"

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Synchronizing with Jules' cognitive brain state...")

        if not os.path.exists(self.memory_path):
            self.logger.warning(f"Jules memory not found at {self.memory_path}. Synchronizing in isolation.")
            return {"jules_cognitive_state": "ISOLATED"}

        try:
            with open(self.memory_path, 'r') as f:
                memory = json.load(f)

            decisions = memory.get("architecturalDecisions", {})
            tasks = memory.get("autonomousTasks", [])
            
            # Inject decisions into blackboard as constraints/goals
            for key, val in decisions.items():
                await blackboard.update("JulesDecision", {key: val})

            # Look for specific triggers
            if decisions.get("knowledgeSource") == "Google Cloud + GMP Patterns":
                self.logger.info("High-Scale Google Cloud sync detected. Escalating Edge strategies.")
                await blackboard.update_consensus("scaling_factor", 2.0)

            return {
                "jules_cognitive_state": "SYNCHRONIZED",
                "autonomous_tasks": tasks,
                "preferred_patterns": memory.get("preferredPatterns", [])
            }
        except Exception as e:
            self.logger.error(f"Brain Sync failed: {e}")
            return {"jules_cognitive_state": "ERROR"}
