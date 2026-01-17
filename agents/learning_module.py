import json
import os
import logging
from typing import Dict, Any

class LearningModule:
    """
    Handles persistent memory and learning for agents.
    Stores data in the memory/ directory.
    """
    def __init__(self, agent_name: str):
        self.agent_name = agent_name
        self.memory_file = f"memory/{agent_name.lower().replace(' ', '_')}_memory.json"
        self._ensure_memory_exists()

    def _ensure_memory_exists(self):
        if not os.path.exists("memory"):
            os.makedirs("memory")
        if not os.path.exists(self.memory_file):
            self.save_memory({"history": [], "learnings": {}, "stats": {}})

    def load_memory(self) -> Dict[str, Any]:
        try:
            with open(self.memory_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            logging.error(f"Failed to load memory for {self.agent_name}: {e}")
            return {"history": [], "learnings": {}, "stats": {}}

    def save_memory(self, data: Dict[str, Any]):
        try:
            with open(self.memory_file, 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            logging.error(f"Failed to save memory for {self.agent_name}: {e}")

    def update_learning(self, key: str, value: Any):
        """Update a specific learning point."""
        data = self.load_memory()
        data["learnings"][key] = value
        self.save_memory(data)

    def log_run(self, run_data: Dict[str, Any]):
        """Log a run execution."""
        data = self.load_memory()
        if "history" not in data:
            data["history"] = []
        data["history"].append(run_data)
        # Keep history manageable
        if len(data["history"]) > 50:
            data["history"] = data["history"][-50:]
        self.save_memory(data)
