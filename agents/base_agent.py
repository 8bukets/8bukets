from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional

class BaseAgent(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    async def process(self, data: List[Dict], shared_context: Dict[str, Any], knowledge_base: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process the data and return a dictionary of results.

        Args:
            data: The scraped data list.
            shared_context: A dictionary for agents to share real-time insights during this run.
            knowledge_base: A persistent dictionary for long-term learning and evolution.

        Returns:
            A dictionary of results for the report.
        """
        pass

    def format_report(self, results: Dict[str, Any]) -> str:
        """
        Default formatter for the report. Can be overridden.
        """
        report = [f"### {self.name} Report"]
        for key, value in results.items():
            report.append(f"- **{key}**: {value}")
        return "\n".join(report)
