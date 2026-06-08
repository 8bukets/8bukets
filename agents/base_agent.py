import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)

class Blackboard(dict):
    pass

class BaseAgent(ABC):
    def __init__(self, name, dependencies=None, provides=None):
        self.name = name
        self.dependencies = dependencies or []
        self.provides = provides or []
        self.logger = logging.getLogger(f"Agent.{name}")

    @abstractmethod
    async def run(self, context: dict):
        """
        Execute the agent's task.
        :param context: A shared dictionary containing data and state.
        """
        pass

    def log(self, message):
        self.logger.info(message)
