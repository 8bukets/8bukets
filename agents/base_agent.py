from abc import ABC, abstractmethod
from typing import Dict, List, Any

class BaseAgent(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass

    def log(self, message: str):
        print(f"[{self.name}] {message}")

    def load_dna(self) -> Dict:
        """Loads the system DNA configuration."""
        import json
        try:
            with open("system_dna.json", 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
