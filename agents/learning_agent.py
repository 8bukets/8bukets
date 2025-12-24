from agents.base_agent import BaseAgent
import json
import os

class LearningAgent(BaseAgent):
    def __init__(self):
        super().__init__("Learning")
        self.memory_file = "agent_memory.json"

    async def run(self, context: dict):
        self.log("Learning from cycle execution...")

        memory = self.load_memory()

        # Analyze current run
        health = context.get("health", {})
        is_healthy = health.get("healthy", False)

        # Update run stats
        memory["total_runs"] = memory.get("total_runs", 0) + 1
        if is_healthy:
            memory["successful_runs"] = memory.get("successful_runs", 0) + 1
        else:
            memory["failed_runs"] = memory.get("failed_runs", 0) + 1

        # Evolve parameters
        # Example: If healthy, potentially increase limit slightly?
        # Or just track stability.
        current_limit = context.get("limit", 5)

        if is_healthy:
            # "Evolve" by suggesting optimization (mock)
            self.log("Run was healthy. Reinforcing current parameters.")
        else:
            # "Correct" by suggesting reduction
            self.log("Run issues detected. Suggesting parameter review.")

        self.save_memory(memory)
        context["learning_status"] = {
            "total_runs": memory["total_runs"],
            "success_rate": f"{(memory.get('successful_runs', 0) / memory['total_runs']) * 100:.1f}%"
        }

    def load_memory(self):
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, 'r') as f:
                    return json.load(f)
            except:
                pass
        return {}

    def save_memory(self, memory):
        with open(self.memory_file, 'w') as f:
            json.dump(memory, f, indent=4)
