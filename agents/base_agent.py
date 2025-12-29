from abc import ABC, abstractmethod
from typing import Dict, List, Any
import sys
import os

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def colorize(text: str, color: str) -> str:
        if sys.stdout.isatty() or os.environ.get('FORCE_COLOR'):
            return f"{color}{text}{Colors.ENDC}"
        return text

class BaseAgent(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass

    def log(self, message: str):
        # Color the agent name in Cyan
        agent_name = Colors.colorize(f"[{self.name}]", Colors.CYAN)
        print(f"{agent_name} {message}")
