import logging
import json
import os
from abc import ABC, abstractmethod

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class BaseAgent(ABC):
    def __init__(self, name):
        self.name = name
        self.logger = logging.getLogger(name)
        self.memory_file = f"autonomous_agents/{name.lower()}_memory.json"
        self.knowledge = self.load_memory()

    def load_memory(self):
        """Loads agent 'knowledge' from a JSON file to simulate persistent learning."""
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                self.logger.error(f"Failed to load memory: {e}")
        return {"experience_points": 0, "logs": []}

    def save_memory(self):
        """Saves agent 'knowledge'."""
        try:
            with open(self.memory_file, 'w') as f:
                json.dump(self.knowledge, f, indent=4)
        except Exception as e:
            self.logger.error(f"Failed to save memory: {e}")

    def log_activity(self, activity):
        """Logs an activity to memory."""
        self.logger.info(activity)
        self.knowledge["logs"].append(activity)
        self.knowledge["experience_points"] += 1
        self.save_memory()

    @abstractmethod
    def run(self, context):
        """Main execution method for the agent. Context is a shared dictionary."""
        pass

    def learn(self, insight):
        """Simulates learning by storing insights."""
        if "insights" not in self.knowledge:
            self.knowledge["insights"] = []
        self.knowledge["insights"].append(insight)
        self.log_activity(f"Learned new insight: {insight}")
