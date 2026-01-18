import logging
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

# Configure logging for agents
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)

class BaseAgent(ABC):
    def __init__(self, name: str):
        self.name = name
        self.logger = logging.getLogger(f"Agent-{name}")
        self.memory: Dict[str, Any] = {}

    def log(self, message: str, level: str = "info"):
        if level == "info":
            self.logger.info(message)
        elif level == "warning":
            self.logger.warning(message)
        elif level == "error":
            self.logger.error(message)
        elif level == "debug":
            self.logger.debug(message)

    @abstractmethod
    async def process(self, data: Any) -> Any:
        """
        Process input data and return a result.
        Must be implemented by subclasses.
        """
        pass

    def update_memory(self, key: str, value: Any):
        self.memory[key] = value

    def get_memory(self, key: str) -> Optional[Any]:
        return self.memory.get(key)
