from abc import ABC, abstractmethod
from typing import Any, Dict

class BaseAgent(ABC):
    """
    Abstract base class for all autonomous agents.
    Each agent must implement the `run` method.
    """
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def run(self, data: Any) -> Dict[str, Any]:
        """
        Execute the agent's logic.

        Args:
            data: The input data necessary for the agent to function (e.g., list of posts).

        Returns:
            A dictionary containing the agent's output/findings.
        """
        pass
