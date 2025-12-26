import json
import logging
from abc import ABC, abstractmethod

# Remove basicConfig to allow root logger configuration to take precedence
logger = logging.getLogger(__name__)

class BaseAgent(ABC):
    def __init__(self, name: str, data_path: str = "links.json"):
        self.name = name
        self.data_path = data_path
        self.data = self._load_data()
        self.results = {}

    def _load_data(self):
        try:
            with open(self.data_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"Data file not found at {self.data_path}")
            return []
        except json.JSONDecodeError:
            logger.error(f"Error decoding JSON from {self.data_path}")
            return []

    @abstractmethod
    def run(self):
        """Execute the agent's main logic."""
        pass

    def get_results(self):
        return self.results

    def log(self, message):
        logger.info(f"[{self.name}] {message}")
