from abc import ABC, abstractmethod
from typing import Any, Dict
from .learning_module import LearningModule

class BaseAgent(ABC):
    """
    Abstract base class for all autonomous agents.
    Each agent must implement the `run` method.
    Includes built-in Learning Module.
    """
    def __init__(self, name: str):
        self.name = name
        self.memory = LearningModule(name)

    @abstractmethod
    def run(self, data: Any) -> Dict[str, Any]:
        """
        Execute the agent's logic.

        Args:
            data: The input data necessary for the agent to function.

        Returns:
            A dictionary containing the agent's output/findings.
        """
        pass

    def collaborate(self, other_agent_output: Dict[str, Any]) -> Dict[str, Any]:
        """
        Optional method to process data from other agents.
        """
        return {}
