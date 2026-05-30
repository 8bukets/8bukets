import logging
from abc import ABC, abstractmethod
from typing import Dict, List, Any

class Blackboard(dict):
    pass

class BaseAgent(ABC):
    def __init__(self, name: str, dependencies=None, provides=None):
        self.name = name
        self.dependencies = dependencies or []
        self.provides = provides or []
        self.logger = logging.getLogger(name)

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass

    def log(self, message: str):
        print(f"[{self.name}] {message}")
