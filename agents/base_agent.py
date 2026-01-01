import sys
import os
# Add parent directory to path to import colors if needed, but since we run from root, it should be fine.
# If this fails, we can do a relative import or assume run from root.
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
        # Make the agent name bold and colored (e.g., cyan/info)
        # We can use a different emoji for each agent later if we want, but for now just color the name.
        prefix = Colors.bold(Colors.info(f"[{self.name}]"))
        print(f"{prefix} {message}")
