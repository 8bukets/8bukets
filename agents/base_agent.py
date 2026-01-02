from abc import ABC, abstractmethod
from typing import Dict, List, Any
from colors import Colors

class BaseAgent(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass

    def log(self, message: str):
        print(f"{Colors.CYAN}[{self.name}]{Colors.ENDC} {message}")
