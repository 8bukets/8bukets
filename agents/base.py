import logging
from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

# Configure logging for agents
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

class BaseAgent(ABC):
    def __init__(self, name: str):
        self.name = name
        self.logger = logging.getLogger(name)

    @abstractmethod
    async def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the agent's task.
        :param context: Shared dictionary containing data from previous agents.
        :return: Result dictionary to be merged into the context.
        """
        pass

    def log(self, message: str):
        self.logger.info(message)
