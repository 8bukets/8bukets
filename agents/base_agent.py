from abc import ABC, abstractmethod
from typing import Dict, List, Any

class BaseAgent(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass

    def log(self, message: str):
        # Using print allows streaming to stdout, which is then captured by the user or terminal.
        # But we could also use logging.
        import logging
        logger = logging.getLogger(__name__)
        # If logger has handlers, use them (which might be colored)
        if logger.hasHandlers() or logging.getLogger().hasHandlers():
            logger.info(f"[{self.name}] {message}")
        else:
            print(f"[{self.name}] {message}")
