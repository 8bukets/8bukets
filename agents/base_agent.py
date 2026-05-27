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

    def escape_markdown(self, text: str) -> str:
        """Escape Markdown special characters to prevent injection."""
        if not text:
            return ""
        # Characters that have special meaning in Markdown
        escape_chars = r"_*[]()~`>#+-=|{}.!<" + "\\"
        return "".join(f"\\{char}" if char in escape_chars else char for char in text)
