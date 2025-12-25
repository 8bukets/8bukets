from abc import ABC, abstractmethod
import logging
import json
import os

MEMORY_FILE = "data/memory.json"

class BaseAgent(ABC):
    def __init__(self, name):
        self.name = name
        self.logger = logging.getLogger(name)
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def load_memory(self) -> dict:
        """Load global memory from disk."""
        if not os.path.exists(MEMORY_FILE):
            return {}
        try:
            with open(MEMORY_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            self.logger.error(f"Failed to load memory: {e}")
            return {}

    def save_memory(self, memory: dict):
        """Save global memory to disk."""
        try:
            with open(MEMORY_FILE, 'w', encoding='utf-8') as f:
                json.dump(memory, f, indent=4)
        except Exception as e:
            self.logger.error(f"Failed to save memory: {e}")

    def update_agent_memory(self, key: str, value: any):
        """Update a specific key in this agent's memory section."""
        full_mem = self.load_memory()
        if self.name not in full_mem:
            full_mem[self.name] = {}
        full_mem[self.name][key] = value
        self.save_memory(full_mem)

    def get_agent_memory(self, key: str, default=None):
        """Retrieve a specific key from this agent's memory."""
        full_mem = self.load_memory()
        return full_mem.get(self.name, {}).get(key, default)

    @abstractmethod
    def run(self, data: list, context: dict) -> dict:
        """
        Run the agent's task.
        :param data: The raw scraped data (list of dicts).
        :param context: A dictionary containing results from previous agents.
        :return: A dictionary containing this agent's output.
        """
        pass
