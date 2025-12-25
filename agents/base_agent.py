import logging
from abc import ABC, abstractmethod

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class BaseAgent(ABC):
    def __init__(self, name):
        self.name = name
        self.logger = logging.getLogger(name)
        self.knowledge_base = {}

    @abstractmethod
    def run(self, context):
        """
        Execute the agent's main task based on the provided context.
        Returns the result of the task.
        """
        pass

    def log(self, message):
        self.logger.info(message)

    def learn(self, key, value):
        """Simple learning mechanism: update internal knowledge."""
        self.knowledge_base[key] = value
        self.log(f"Learned: {key}")
