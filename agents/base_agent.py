from abc import ABC, abstractmethod
import logging

class BaseAgent(ABC):
    def __init__(self, name):
        self.name = name
        self.logger = logging.getLogger(name)
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    @abstractmethod
    def run(self, data: list, context: dict) -> dict:
        """
        Run the agent's task.
        :param data: The raw scraped data (list of dicts).
        :param context: A dictionary containing results from previous agents.
        :return: A dictionary containing this agent's output.
        """
        pass
